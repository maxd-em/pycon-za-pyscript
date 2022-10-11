# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import js
import json
import csv
import plotly
import plotly.express as px

## Get the data
from pyodide.http import open_url

with open("programming-languages.csv") as f:
    df = pd.read_csv(f)


def plot(chart):
    fig = px.line(df, x="Week", y=chart, width=1024, height=400)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    js.plot(graphJSON, "chart1")


from js import document
from pyodide import create_proxy


def selectChange(event):
    choice = document.getElementById("select").value
    plot(choice)


def setup():
    # Create a JsProxy for the callback function
    change_proxy = create_proxy(selectChange)

    e = document.getElementById("select")
    e.addEventListener("change", change_proxy)


setup()

plot("Python: (South Africa)")
