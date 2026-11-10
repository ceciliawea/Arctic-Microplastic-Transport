import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy.ma as ma

# === LOAD DATA ===
base_path = "/Users/sarialue"
case_name = "g.e23_a17.G_IAF_JRA.f19_g17.MISO.Spinup.t02"
path = f"{base_path}/{case_name}.pop.h.0268.ann.nc"
ds = xr.open_dataset(path, decode_timedelta=True)

tlat = ds.TLAT
tlon = ds.TLONG
region = ds.REGION_MASK
mp_nb = ds.MP_NB_PAC[0, 0, :, :] * 1000 / 0.000067  # pieces/m³

# === MASKING ===
mp_nb_mask = np.where(region == 10, mp_nb, np.nan)
masked_data = ma.masked_invalid(mp_nb_mask)

print("Arctic NB MP min %.5f" % np.nanmin(mp_nb_mask), "max %.5f" % np.nanmax(mp_nb_mask))

# === PLOTTING ===
fig, ax = plt.subplots(subplot_kw={"projection": ccrs.NorthPolarStereo()}, figsize=(7.5, 7.5))

# Microplastic pcolormesh
p = ax.pcolormesh(tlon, tlat, masked_data,
                  vmin=0, vmax=0.006,
                  cmap="plasma",
                  shading="nearest",
                  transform=ccrs.PlateCarree())

# Add features
ax.add_feature(cfeature.LAND, edgecolor="black", linewidth=0.5,
               facecolor=cfeature.COLORS["land_alt1"])
ax.add_feature(cfeature.BORDERS, linewidth=0.3, zorder=3)
ax.coastlines(linewidth=0.4, zorder=3)
ax.gridlines(draw_labels=False, color="gray", linestyle="--", linewidth=0.4)

# === ZOOM: Beaufort Gyre + Arctic Coastline ===
ax.set_extent([-170, -100, 65, 85], crs=ccrs.PlateCarree())

# === SWIRL: Clockwise arrows over BG ===
theta = np.linspace(0, 2 * np.pi, 100)
r = 2  # degrees
cx, cy = -135, 76  # BG center
x = cx + r * np.cos(theta)
y = cy + r * np.sin(theta)

# BG label
ax.text(cx, cy + 2.8, "Beaufort Gyre", fontsize=10, ha='center', color='navy',
        transform=ccrs.PlateCarree(), weight='bold')

# === COLORBAR ===
axins = inset_axes(ax, width="80%", height="4%",
                   loc='lower left',
                   bbox_to_anchor=(0.1, -0.12, 0.8, 1.0),
                   bbox_transform=ax.transAxes,
                   borderpad=0)

cbar = fig.colorbar(p, cax=axins, orientation="horizontal", extend="max")
cbar.set_label("OCN NB MP (pieces/m³)", fontsize=12, labelpad=5)
axins.xaxis.set_ticks_position("bottom")

# Mackenzie River label
ax.text(-132, 68.8, "Mackenzie River", fontsize=7, color='black',
        ha='center', transform=ccrs.PlateCarree(), weight='bold')

# Banks Island
ax.text(-122, 72.6, "Banks Island", fontsize=7, color='black',
        ha='center', transform=ccrs.PlateCarree(), weight='bold')

# North Slope, Alaska
ax.text(-150, 70.2, "North Slope", fontsize=7, color='black',
        ha='center', transform=ccrs.PlateCarree(), weight='bold')


# === TITLE ===
plt.title("Surface Neutrally Buoyant Microplastics in the Beaufort Gyre — Spinup T02", fontsize=13, y=1.08, ha = 'center')
fig.subplots_adjust(bottom=0.15, top=0.92, left=0.1, right=0.95)

plt.show()

