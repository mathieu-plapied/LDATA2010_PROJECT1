from dash import Dash, html
from . import heatmap
from . import genes_comparison


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            heatmap.render(app),
            genes_comparison.render(app)
        ]
    )


"""
html.Div(className="dropdown-container",
                     children=[
                         dropdown.render_cells(app),

                     ]),
"""
