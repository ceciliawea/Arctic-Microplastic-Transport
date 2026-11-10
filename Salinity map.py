import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# === Load dataset ===
ds = xr.open_dataset("/Users/sarialue/g.e23_a17.G_IAF_JRA.f19_g17.MISO.Spinup.t02.pop.h.0268.ann.nc")

# Extract latitude, longitude, and NB MP concentration at surface
lat = ds.TLAT.values
lon = ds.TLONG.values
mp = ds.MP_NB_PAC[0, 0, :, :].values * 1000 / 0.000067  # Convert to pieces/m³

# Mask invalid or non-positive values
mp = np.where(np.isfinite(mp) & (mp > 0), mp, np.nan)

# Flatten arrays
lon_flat = lon.flatten()
lat_flat = lat.flatten()
mp_flat = mp.flatten()

# Filter to valid points
valid = ~np.isnan(mp_flat)
lon_flat = lon_flat[valid]
lat_flat = lat_flat[valid]
mp_flat = mp_flat[valid]

# === Subsample and add jitter to mimic station scatter ===
np.random.seed(42)
num_points = 300  # adjust as needed
indices = np.random.choice(len(mp_flat), size=num_points, replace=False)

lon_sub = lon_flat[indices] + np.random.normal(0, 0.2, size=num_points)
lat_sub = lat_flat[indices] + np.random.normal(0, 0.2, size=num_points)
mp_sub = mp_flat[indices]

# === Plot ===
fig = plt.figure(figsize=(7.5, 7.5))
ax = plt.axes(projection=ccrs.NorthPolarStereo())
ax.set_extent([-160, -120, 70, 85], crs=ccrs.PlateCarree())

ax.coastlines(resolution='110m', linewidth=0.8)
ax.add_feature(cfeature.LAND, facecolor="lightgray")
ax.gridlines(draw_labels=False, linestyle="--", linewidth=0.5)

# Scatter plot
sc = ax.scatter(
    lon_sub, lat_sub, c=mp_sub, s=70, cmap="plasma", edgecolor="k", linewidth=0.4,
    transform=ccrs.PlateCarree(), alpha=0.9
)

# Colorbar
cbar = plt.colorbar(sc, orientation="vertical", shrink=0.7, pad=0.05)
cbar.set_label("Surface NB Microplastics (pieces/m³)", fontsize=12)

# Title and layout
ax.set_title("Surface NB MPs — Spinup T02 (Subsampled)", fontsize=14, pad=10)
plt.tight_layout()
plt.show()
