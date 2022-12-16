from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from . import graph_2d
from . import graph_3d


def create_layout(app) -> html.Div:
    return html.Div(
        className="app-div",
        children=[

            # navbar.render(),
            html.Div([
                html.H2("Overview"),
                dbc.Row([
                    dbc.Col(graph_2d.render(app), width=6),
                    dbc.Col(graph_3d.render(app), width=6)
                    # dbc.Col(dropdown.render(app)),
                    # dbc.Col(kmeans.render(app)),
                    # dbc.Col(clustergram.render(app))
                    # dbc.Col(heatmap.render(app), width=3),
                    # dbc.Col(mini_heatmap.render(app), width=2)
                ], align="center", style={"margin": "10px"}),
                # dbc.Row([
                #    dbc.Col(pca_scatter_plot.render(app)),
                #    dbc.Col(genes_comparison.render(app))
                # html.Div("t", style={"background-color": "blue"})
                # ], align="center", style={"margin": "10px"})
            ], style={"margin": "10px"})

        ],
    )
