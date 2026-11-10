import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# === 1. Simulate example SSH-like background data ===
lon = np.linspace(-180, 180, 360)
lat = np.linspace(60, 90, 150)
lon2d, lat2d = np.meshgrid(lon, lat)
ssh = np.cos(np.radians(lat2d)) * np.sin(np.radians(lon2d / 2))  # just a dummy pattern

# === 2. Define Beaufort Gyre bounding region (approx) ===
# Dotted polygon shape like Timmermans et al.
bg_lon = [-140, -160, -170, -150, -130, -120, -140]
bg_lat = [70,   72,   76,   80,   80,   76,   70]

# === 3. Plot ===
fig = plt.figure(figsize=(8, 6))
ax = plt.axes(projection=ccrs.NorthPolarStereo())

# Background: SSH-style data
pc = ax.contourf(
        lon, lat, ssh, levels=20, cmap='coolwarm',
        transform=ccrs.PlateCarree()
)

# Add coastlines and gridlines
ax.coastlines()
ax.add_feature(cfeature.LAND, color='lightgray')
ax.set_extent([-180, 180, 65, 90], crs=ccrs.PlateCarree())
ax.gridlines(draw_labels=True)

# === 4. Plot BG boundary ===
ax.plot(bg_lon, bg_lat, linestyle='--', color='black', linewidth=2,
        transform=ccrs.PlateCarree(), label='Beaufort Gyre Region')

# Add legend and colorbar
plt.colorbar(pc, ax=ax, orientation='horizontal', pad=0.05, label='Simulated SSH')
ax.legend(loc='lower left')

plt.title('Example Arctic Map with Beaufort Gyre Dotted Boundary')
plt.tight_layout()
plt.show()