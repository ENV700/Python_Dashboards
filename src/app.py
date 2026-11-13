"""Python Shiny dashboard for exploring USGS NWIS sites by North Carolina county.

Run from this directory with: shiny run --reload app.py
"""

#Import packages
from pathlib import Path
import io
import geopandas as gpd
import pandas as pd
import requests
from shiny import App, render, ui

#Set State FIPS code
state_FIPS = "37" 

# Set paths
APP_DIR = Path(__file__).resolve().parent
DATA_DIR = APP_DIR.parent / "data"
NWIS_DATA_FILE = DATA_DIR / f"NWIS_{state_FIPS}.geojson"
COUNTY_URL = "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_county_20m.zip"

# Function to load NWIS data as a geodataframe
def load_nwis_data():
    """Read the cached NWIS sites, downloading them if needed."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not NWIS_DATA_FILE.exists():
        response = requests.get(
            "https://api.waterdata.usgs.gov/ogcapi/v1/collections/monitoring-locations/items",
            params={
                "f": "csv",
                "limit": 50000,
                "properties": "district_code,basin_code,site_type,altitude,drainage_area",
                "offset": 0,
                "state_code": state_FIPS,
            },
            timeout=120,
        )
        response.raise_for_status()
        df_nwis = pd.read_csv(io.StringIO(response.text))
        points = gpd.points_from_xy(df_nwis["x"], df_nwis["y"])
        gdf_nwis = gpd.GeoDataFrame(df_nwis, geometry=points, crs="EPSG:4326")
        gdf_nwis.to_file(NWIS_DATA_FILE, driver="GeoJSON")
    return gpd.read_file(NWIS_DATA_FILE)

# Function to subset counties to North Carolina
def load_counties():
    """Read the Census county boundaries and keep North Carolina counties."""
    counties = gpd.read_file(COUNTY_URL)
    return counties.loc[counties["STATEFP"] == state_FIPS].to_crs("EPSG:4326")

# Execute the functions
gdf_nwis = load_nwis_data()
gdf_counties = load_counties()

# Create a list of county names
COUNTY_NAMES = sorted(gdf_counties["NAME"].dropna().unique().tolist())

# The plot function
def plot_nwis(county_name: str = "Durham"):
    """Plot NWIS monitoring locations inside the selected county."""
    county = gdf_counties.loc[gdf_counties["NAME"] == county_name]
    if county.empty:
        raise ValueError(f"Unknown North Carolina county: {county_name}")

    county_geometry = county.geometry.union_all()
    sites = gdf_nwis.loc[gdf_nwis.intersects(county_geometry)]

    ax = county.plot(color="lightgray", edgecolor="white", linewidth=0.7, figsize=(8, 6))
    if not sites.empty:
        sites.plot(markersize=8, color="blue", ax=ax)
    ax.set_title(f"NWIS monitoring locations — {county_name} County")
    ax.set_axis_off()
    return ax

# Create the user interface
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select(
            "county",
            "County",
            choices=COUNTY_NAMES,
            selected=COUNTY_NAMES[0],
        ),
        title="Select a county",
    ),
    ui.h2("USGS NWIS Monitoring Locations"),
    ui.output_plot("county_plot", height="600px"),
    title="NWIS County Explorer",
)

# Code for reactivity
def server(input, output, session):
    #Update the output plot widget using values in the county input widget
    @output
    @render.plot
    def county_plot():
        ax = plot_nwis(input.county())
        return ax.figure

# Create the app
app = App(app_ui, server)