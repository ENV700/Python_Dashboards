---
Class: ENV700
Author: John.Fay@duke.edu
Date: Fall 2026
---

# Python Dashboards

This workspace demonstrates the development and deployment of Python-based dashboard using Python/Shiny. 

## Conda Environment
To run this code, you'll need to create a specific Conda environment. Type these commands at a miniforge prompt:

```
conda create -n env700-shiny python=3.12
activate env700-shiny
conda install pandas geopandas shiny ipyleaflet seaborn ipykernel shinywidgets rsconnect-python pip
pip install shinyswatch
```

## Workspace setup
For the Shiny app to work, your app.py should be in the root folder and your data organized in a "data" sub-folder. 

This workspace contains a simple workflow that enables a user to view all the NWIS stream locations for a selected county in North Carolina. The `app_template.ipynb` was used to prototype the application code and then this was recoded as a Shiny app using the ChatGPT prompt: 
>From the code in the attached notebook, create a simple Python Shiny dashboard app with a dropdown of county names that executes the plot_nwis() function and displays the resulting plot in a display widget.

You will also see a **`requirements.txt`** file in the project `src` folder. This is a listing of all the 3rd party packages required to run your Shiny app. (These will be installed when the app is deployed.) If you are uncertain what should be included here, you can ask ChatGPT to create a requirements.txt file for you for the app.py file you provide it. 

## Publishing
After testing, the app.py file is published as follows:
1. Create a free account on Posit Cloud: <https://posit.cloud/> and log in
1. In VSCode, install the **Posit Publisher** extension. This will add a new item to your VS Code Activity Bar. 
1. Add your credentials to the Posit Publisher extension
    1. Activate the Posit Publisher interface, and select the **CREDENTIALS** tab. 
    1. Click on the **+** which will open a box to add a new credential.
    1. Select Posit Connect Cloud and follow the instructions to authorize VS code to access your Posit cloud account.
1. Deploy your app
    1. With the Posit Publisher active, select the **DEPLOYMENT** tab.
    1. Create a new deployment, navigating to your `app.py` file for the file to deploy
    1. Give you deployment a name; this will be used to identify this deployment within VS Code (e.g. if you have > 1)
    1. Select the credential used to upload this to Posit Connect Cloud
    1. Review the files that will be included in your deployment; the default should suffice. 
    1. Click the **Deploy Your Project** button. 

> If you update your code, simply re-deply your app.

## Viewing
If all goes well, the Posit Publisher will configure everything and upload your app to the Posit Cloud. 
1. Navigate to your posit cloud page; you should see your app there. 
1. Copy the link and share it with others. 
1. **Pro Tip**: Use <http://duke.is> to give your Shiny App URL a better link name

Here's my link: <https://connect.posit.cloud/johnpfay/content/01a1d69d-feca-fe9a-454a-d28241b918b4>