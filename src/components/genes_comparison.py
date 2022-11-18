from dash import Dash, html, dcc
from dash.dependencies import Output, Input
from . import ids
import plotly.express as px
from icecream import ic


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.GENES_COMPARISON, "children"),
        Input(ids.GENES_HEATMAP, 'hoverData')

    )
    def update_genes_comparison(_) -> html.Div:
        ic(_)
        return html.Div("hover_data")

    return html.Div("It works... I mean kinda..")
