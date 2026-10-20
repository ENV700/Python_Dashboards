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