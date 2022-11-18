from dash import Dash, html, dcc
from . import ids
from dash.dependencies import Input, Output
import plotly.express as px
from ..api import data_api
import numpy as np


def render(app: Dash) -> html.Div:
    df = data_api.fetch_data(
        "././data/transcriptomics_data.csv")
    df = df.drop(columns=["colour", "cell_type"])
    fig = px.imshow(df.corr(), width=800, height=800, text_auto=True)

    return html.Div(dcc.Graph(figure=fig, hoverData={'points': [{'customdata': 'Japan'}]}), id=ids.GENES_HEATMAP)
