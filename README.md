---
Class: ENV700
Author: John.Fay@duke.edu
Date: Fall 2026
---

# Python Dashboards

This workspace demonstrates the development of Python-based dashboard using Python/Shiny. 

To run this code, you'll need to create a specific Conda environment. 

```conda
conda create --name arcccoh_shiny python=3.9.18 -y
activate arcccoh_shiny 
conda install -c esri arcgis=2.2.0.1 -y
jupyter nbextension enable arcgis --py --sys-prefix
conda.exe install -c esri scipy -y
pip install geopandas
conda install -c esri ipyleaflet -y
conda install -c bioconda epiweeks -y
conda install -c esri mapclassify -y
conda install -c esri folium
conda install -c conda-forge shiny -y
pip install shinylive
pip install shinywidgets
pip install rsconnect-python
```
