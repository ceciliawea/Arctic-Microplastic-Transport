import numpy as np
import xarray as xr
import pandas as pd
from numpy import nan as NA
from netCDF4 import Dataset
import netCDF4
import glob
import xesmf as xe
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.lines import Line2D
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.util import add_cyclic_point
from matplotlib import gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
import metpy.calc as mpcalc

# ⭕ Create a circular mask for polar projection
theta = np.linspace(0, 2 * np.pi, 100)
map_circle = mpath.Path(np.vstack([np.sin(theta), np.cos(theta)]).T * 0.5 + [0.5, 0.5])

# ✅ Local data folder
base_path = "/Users/sarialue"

# CESM case names
case_name = [
    "g.e23_a17.G_IAF_JRA.f19_g17.MISO.Spinup.t02",
]

# Plot titles
ttl = ["kup=1", "kup=1, krelm=0.03"]

# Data storage
mod_lat = []
mod_lon = []
mp_nb_mod = []
mp_pb_mod = []

for case in case_name:
    path = f"{base_path}/{case}.pop.h.0268.ann.nc"
    pointer = xr.open_dataset(path, decode_timedelta=True)

    tlat = pointer.TLAT  # 2D latitude
    tlon = pointer.TLONG  # 2D longitude
    z_t = pointer.z_t * 0.01  # depth in meters
    region = pointer.REGION_MASK  # POP region mask

    # Surface MPs [0th time, 0th level]
    mp_nb = pointer.MP_NB_PAC[0, 0, :, :]
    mp_pb = pointer.MP_PB_PAC[0, 0, :, :]

    # Convert to pieces/m³
    mp_nb = (mp_nb * 1000) / 0.000067
    mp_pb = (mp_pb * 1000) / 0.000061

    # Mask for Arctic Basin only (region == 10)
    mp_nb_mask = np.where(region == 10, mp_nb, np.nan)
    mp_pb_mask = np.where(region == 10, mp_pb, np.nan)

    print("Arctic NB MP min %.5f" % np.nanmin(mp_nb_mask), "max %.5f" % np.nanmax(mp_nb_mask))
    print("Arctic PB MP min %.5f" % np.nanmin(mp_pb_mask), "max %.5f" % np.nanmax(mp_pb_mask))

    mod_lat.append(tlat.values)
    mod_lon.append(tlon.values)
    mp_nb_mod.append(mp_nb_mask)
    mp_pb_mod.append(mp_pb_mask)

# Convert to arrays
mod_lat = np.array(mod_lat)
mod_lon = np.array(mod_lon)
mp_nb_mod = np.array(mp_nb_mod)
mp_pb_mod = np.array(mp_pb_mod)

# Show final shape
print("Final PB MP array shape:", mp_pb_mod.shape)

fig, ax = plt.subplots(subplot_kw={"projection": ccrs.NorthPolarStereo()}, figsize=(6, 6))

p = ax.pcolormesh(tlon, tlat, mp_nb_mod[0, :, :],
                  vmin=0, vmax=0.006,
                  cmap="Spectral_r", shading="nearest",
                  transform=ccrs.PlateCarree())

ax.set_boundary(map_circle, transform=ax.transAxes)
ax.add_feature(cfeature.LAND, zorder=1, edgecolor="black",
               linewidth=0.5, facecolor=cfeature.COLORS["land_alt1"])
ax.set_extent([0, 360, 60, 90], crs=ccrs.PlateCarree())
ax.gridlines(draw_labels=False, color="gray", linestyle="--", linewidth=0.5)

# Colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Define colorbar box as full 4-tuple: (x0, y0, width, height)
axins = inset_axes(ax,
                   width="80%",  # % of parent axes
                   height="4%",
                   bbox_to_anchor=(0.1, -0.12, 0.8, 1.0),  # [left, bottom, width, height]
                   bbox_transform=ax.transAxes,
                   loc='lower left',
                   borderpad=0)

# Add colorbar
cbar = fig.colorbar(p, cax=axins, orientation="horizontal", extend="max")
cbar.set_label("OCN NB MP (pieces/m³)", fontsize=12, labelpad=5)
axins.xaxis.set_ticks_position("bottom")


plt.title("NB MPs — Spinup T02", fontsize=14, y=1.05)
fig.subplots_adjust(bottom=0.15, top=0.9, left=0.1, right=0.95)
plt.show()