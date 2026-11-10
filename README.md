# Beaufort Gyre & Arctic Ocean Analysis

Python data processing and spatial visualization scripts developed to analyze microplastic concentrations, sea ice dynamics, ocean salinity, and circulation fields across the Beaufort Gyre and Arctic Ocean[cite: 4, 5, 7, 8, 10, 12].

## **ALSO WANT TO NOTE:**
These are Python scripts that helped me in my research; they are not finalized figures, and I only tested some coding in a small environment compiler to familiarize myself with the Ocean Modeling process. 

I used NCARS' Derecho Supercomputing system to code all of my findings for my research experience; those Notebooks, which are not public, are pending submission as papers with my co-authors. See the [Abstract](https://studio.m-anage.com/agu/agu25/meetingapp.cgi/Paper/1921907) of my findings from the AGU. 

## [POSTER LINK](https://ceee.colorado.edu/sites/default/files/2025-08/Cece%20Weaver%20-%20Poster%20Final.pdf)

---

## Features
* **Microplastic Mapping:** Visualizes neutrally buoyant microplastic fields ($pieces/m^3$) projected onto North Polar Stereographic coordinates[cite: 4, 7].
* **Beaufort Gyre Domain Analysis:** Isolates regional boundaries and overlays atmospheric/oceanic features centered on the Beaufort Gyre[cite: 6, 7].
* **Sea Ice Volume Dynamics:** Generates temporal heatmaps tracking sea ice volume shifts across months and years in the Bering Strait[cite: 5].
* **Hydrographic Diagnostics:** Maps barotropic stream functions and regional salinity distributions across Arctic domains[cite: 8, 12].
* **Interactive Data Exploration:** Renders interactive GeoViews QuadMesh maps for curvilinear grid datasets in Jupyter environments[cite: 10].

---

## Project Structure
* `BG Ocean Test 2.py` — Generates publication-ready polar plots of surface microplastics with geographic annotations[cite: 7, 12].
* `BG bounding box.py` — Defines and plots regional bounding polygons over ocean background fields[cite: 6, 12].
* `Beaufort Gyre Ocean Hist.py` — Maps Arctic ocean region-masked microplastic concentrations[cite: 4, 12].
* `Bering Strait Sea Ice change.py` — Builds monthly vertical heatmaps of regional sea ice volume[cite: 5, 12].
* `Dataset.py` — Computes and visualizes Barotropic Stream Function (BSF) fields across polar ocean domains[cite: 8, 12].
* `MP Ocean Hist.py` — Processes and visualizes microplastic distribution metrics across ocean grids[cite: 12].
* `Salinity map.py` — Maps spatial salinity fields across Arctic marine regions[cite: 12].
* `interactive BG map.py` — Interactive GeoViews QuadMesh renderer for curvilinear grid outputs[cite: 10, 12].
* `ROMS Ocean Model.iml` — Module configuration file for IDE project management[cite: 12].

---

## Tech Stack & Dependencies
* **Language:** Python 3.x[cite: 4, 5, 6, 7, 8, 10]
* **Data Handling:** `xarray`, `numpy`, `pandas`[cite: 4, 5, 6, 7, 8, 10]
* **Spatial & Graphics:** `cartopy`, `matplotlib`, `seaborn`, `geoviews`, `holoviews`[cite: 4, 5, 6, 7, 8, 10]

---

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
