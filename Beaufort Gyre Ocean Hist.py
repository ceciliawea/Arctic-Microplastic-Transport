import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy.ma as ma

# Load dataset
base_path = "/Users/sarialue"
case_name = "g.e23_a17.G_IAF_JRA.f19_g17.MISO.Spinup.t02"
path = f"{base_path}/{case_name}.pop.h.0268.ann.nc"
ds = xr.open_dataset(path)

tlat = ds.TLAT
tlon = ds.TLONG
region = ds.REGION_MASK
mp_nb = ds.MP_NB_PAC[0, 0, :, :] * 1000 / 0.000067  # Convert to pieces/m³

# Mask Arctic region
mp_nb_mask = np.where(region == 10, mp_nb, np.nan)
print("Arctic NB MP min %.5f" % np.nanmin(mp_nb_mask), "max %.5f" % np.nanmax(mp_nb_mask))

# Plot setup
fig = plt.figure(figsize=(7, 7))
ax = plt.axes(projection=ccrs.NorthPolarStereo())
ax.set_extent([-160, -120, 70, 85], crs=ccrs.PlateCarree())

ax.coastlines()
ax.add_feature(cfeature.LAND, facecolor="lightgray")
ax.gridlines(draw_labels=False, linestyle="--", linewidth=0.5)

masked_data = ma.masked_invalid(mp_nb_mask)

p = ax.pcolormesh(
    tlon, tlat, masked_data,
    vmin=0, vmax=0.006,
    cmap="plasma",
    shading="nearest",
    transform=ccrs.PlateCarree()
)

# Colorbar
axins = inset_axes(ax, width="80%", height="4%",
                   loc='lower left',
                   bbox_to_anchor=(0.1, -0.12, 0.8, 1.0),
                   bbox_transform=ax.transAxes,
                   borderpad=0)

cbar = fig.colorbar(p, cax=axins, orientation="horizontal", extend="max")
cbar.set_label("OCN NB MP (pieces/m³)", fontsize=12, labelpad=5)
axins.xaxis.set_ticks_position("bottom")

# Title and layout
plt.title("Surface NB Microplastics in Beaufort Gyre (T02)", fontsize=13, y=1.08)
fig.subplots_adjust(bottom=0.15, top=0.9, left=0.1, right=0.95)

plt.show()
