import xarray as xr
import geoviews as gv
import holoviews as hv
import cartopy.crs as ccrs
hv.extension('bokeh')

# Load dataset
path = "/Users/sarialue/g.e23_a17.G_IAF_JRA.f19_g17.MISO.Spinup.t02.pop.h.0268.ann.nc"
ds = xr.open_dataset(path)

# Extract and convert variable
mp = ds.MP_NB_PAC[0, 0] * 1000 / 0.000067
mp.name = "MP"

# Mask Arctic (region 10)
region = ds.REGION_MASK
mp_masked = mp.where(region == 10)

# Use QuadMesh for curvilinear grids
mesh = gv.QuadMesh((ds.TLONG, ds.TLAT, mp_masked),
                   crs=ccrs.PlateCarree()).opts(
    cmap='Spectral_r', colorbar=True,
    width=800, height=700,
    tools=['hover'], title="NB MPs — Beaufort Gyre",
    clabel="pieces/m³", color_levels=20
)

mesh
# can only use in Jupyter