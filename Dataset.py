import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load data
ds = xr.open_dataset("/Users/sarialue/g.e23_a17.G_IAF_JRA.f19_g17.MISO.Spinup.t02.pop.h.0268.ann.nc", decode_timedelta=True)

lon = ds['TLONG'].values
lat = ds['TLAT'].values
bsf = ds['BSF'].isel(time=0).values

# Mask invalid values
bsf = np.ma.masked_invalid(bsf)

# Plot
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection=ccrs.NorthPolarStereo())

# Set map extent for Arctic
ax.set_extent([-180, 180, 50, 90], crs=ccrs.PlateCarree())

# Plot BSF
c = ax.pcolormesh(lon, lat, bsf, transform=ccrs.PlateCarree(), cmap='viridis', shading='auto')
plt.colorbar(c, ax=ax, orientation='vertical', label='BSF [Sv]')

# Add coastlines and gridlines
ax.coastlines()
ax.gridlines(draw_labels=False, linestyle='--')

plt.title("Barotropic Stream Function (BSF) - Arctic View")
plt.tight_layout()
plt.show()
