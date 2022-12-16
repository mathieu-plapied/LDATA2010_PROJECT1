import time

from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from . import ids
import dash_daq as daq
import dash_bootstrap_components as dbc
import plotly.express as px
import functools
import src.api.data_api as data_api
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


def render(app: Dash) -> html.Div:
    @functools.lru_cache(maxsize=32)
    def call_dr(dr_type):
        df = data_api.get_dataframe()
        X_train = df.loc[:, "gene_0":"gene_299"]
        true_labels = df.loc[:, "cell_type"]

        # X_train = StandardScaler().fit_transform(X_train)
        pca_50 = PCA(n_components=20)
        pca_result_50 = pca_50.fit_transform(X_train)
        tsne = TSNE(n_components=2, verbose=0, perplexity=40, n_iter=400).fit_transform(pca_result_50)
        return tsne, df

    @app.callback(
        Output("collapse", "is_open"),
        [Input("collapse-button", "n_clicks")],
        [State("collapse", "is_open")],
    )
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
        Output("3d-graph", "children"),
        Input(ids.TOGGLE_SWITCH_DIMENSION, "value")
    )
    def update_3dgraph(value):
        print(value)
        if value:
            fig = px.scatter_3d(x=[1, 2, 3], y=[1, 2, 3], z=[1, 2, 3])
        else:
            fig = px.scatter(x=[1, 2, 3], y=[1, 2, 3])

        return html.Div(dcc.Graph(figure=fig))

    return html.Div([
        html.H4("TSE"),
        daq.ToggleSwitch(id=ids.TOGGLE_SWITCH_DIMENSION, value=False, label=["2D", "3D"], labelPosition="bottom",
                         style={"margin": "10px"}),
        dbc.Spinner(id="loading-icon", children=[html.Div(id="3d-graph")], color="success"),

        html.Div([html.H5("Dimension reduction options")
                     , html.P("Number of dimension reduction with PCA:", style=dict(display="inline-block")),
                  dbc.Input(id="pca-input", type="number", min=10, max=50, step=5,
                            style={"width": "100px"})], style={"margin": "10px"}),
        html.H5("Clustering options"),
        dbc.Button(
            "Open Informations",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
            style=dict(marginTop="10px")
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(
                [
                    dbc.Alert([
                        html.H6("Essential informations about options on this graph", className="card-title"),
                        html.Ul([
                            html.Li("The graph is a 3D scatter plot"),
                            html.Li("The graph is a 3D scatter plot"),
                            html.Li("The graph is a 3D scatter plot"),
                        ]),

                    ], color="primary"),

                ]
            )),
            id="collapse",
            is_open=True,
        ),
    ])
