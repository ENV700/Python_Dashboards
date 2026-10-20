---
Class: ENV700
Author: John.Fay@duke.edu
Date: Fall 2026
---

# Python Dashboards

This workspace demonstrates the development of Python-based dashboard using Python/Shiny. 

To run this code, you'll need to create a specific Conda environment. For developing a Shiny for Python dashboard using Miniforge, VS Code, and Conda, I recommend creating a dedicated Conda environment using an `environment.yml` file.

### 1. Conda environment recipe

Save the following as `environment.yml` in your project directory.

```

name: shiny-dashboard

channels:
  - conda-forge

dependencies:
  - python=3.12
  - pip

  # Data manipulation
  - pandas
  - numpy

  # Visualization
  - matplotlib
  - seaborn
  - plotly

  # Jupyter and VS Code support
  - ipykernel
  - jupyterlab

  # Dashboard framework
  - pip:
      - shiny
      - shinyswatch
      - shinywidgets

```

Key packages:

- `shiny`: Core framework for building reactive Python dashboards.
- `shinyswatch`: Provides Bootstrap themes for Shiny applications.
- `shinywidgets`: Integrates interactive visualization libraries, including Plotly.
- `plotly`: Produces interactive charts with zooming, tooltips, and selection.
- `pandas`, `numpy`: Support data preparation and analysis.

### 2. Create and activate the environment

Open a Powershell terminal in VS Code and execute:

```
conda env create -f environment.yml
conda activate shiny-dashboard
```

Verify the installation:

```
shiny --version
```

### 3. Create your first dashboard

Create a file named `app.py`:

```python

from shiny import App, ui, render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
df = sns.load_dataset("penguins")

# Define the user interface
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select(
            "species",
            "Select species:",
            choices=["All", "Adelie", "Chinstrap", "Gentoo"]
        ),
    ),
    ui.h2("Penguin Data Explorer"),
    ui.output_plot("penguin_plot"),
    ui.output_data_frame("penguin_table"),
)

# Define server-side behavior
def server(input, output, session):

    @render.plot
    def penguin_plot():
        data = df if input.species() == "All" else (
            df[df["species"] == input.species()]
        )

        fig, ax = plt.subplots()
        sns.scatterplot(
            data=data,
            x="bill_length_mm",
            y="bill_depth_mm",
            hue="species",
            ax=ax
        )
        return fig

    @render.data_frame
    def penguin_table():
        data = df if input.species() == "All" else (
            df[df["species"] == input.species()]
        )
        return render.DataGrid(data)

app = App(app_ui, server)

```

### 4. Run the dashboard

From the terminal:

```
shiny run --reload app.py
```

Open `http://127.0.0.1:8000` in your browser.

The `--reload` option automatically restarts the application when you save changes to your Python code.

### 5. Recommended project structure

```
shiny-dashboard/
├── environment.yml
├── app.py
├── data/
│   └── observations.csv
├── modules/
│   └── analysis.py
├── www/
│   └── styles.css
├── notebooks/
│   └── exploration.ipynb
├── .gitignore
└── README.md
```

For an environmental data analysis dashboard, this structure lets you maintain exploratory analyses in Jupyter notebooks while developing the interactive dashboard separately.

One architectural recommendation: Use Shiny's reactive programming model to connect user controls to data filtering and visualization. This allows you to reuse much of your existing Pandas and Seaborn code without learning JavaScript.

For deployment, you can subsequently publish the dashboard to [shinyapps.io](https://www.shinyapps.io/?utm_source=chatgpt.com) or [Posit Connect Cloud](https://connect.posit.cloud/?utm_source=chatgpt.com). Deployment environments may require a separate Python dependency specification, typically `requirements.txt`, rather than relying directly on the Conda YAML file.