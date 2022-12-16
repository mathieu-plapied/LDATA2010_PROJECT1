import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from . import ids
import plotly.express as px
import functools
import src.api.data_api as api
import plotly.graph_objects as go
from collections import Counter


def render(app: Dash) -> html.Div:
    all_dr = ["PCA", "SVD", "NMF", "ICA", "t-SNE", "UMAP"]
    all_cluster = ["KMeans", "DBSCAN", "AgglomerativeClustering", "Birch", "GaussianMixture"]
    df_pca = api.compute_pca()

    @app.callback(
        Output(ids.GRAPH_2D, "children"),
        Input(ids.KMEANS_SLIDER, "value")
    )
    def update_kmeans_graph(value):

        print("kmeans graph have been updated")
        print(value)
        labels = api.compute_kmeans(value, df_pca)

        if value == 1:
            fig = px.scatter(df_pca, x="x", y="y", color="cell_type",
                             title="KMeans with 1 cluster")
            count = Counter(df_pca["cell_type"])
        else:
            fig = px.scatter(df_pca, x="x", y="y", color=labels,
                             color_discrete_sequence=px.colors.qualitative.Dark2,
                             title="KMeans with {} clusters".format(value))
            count = Counter(labels)
        config = {
            "doubleClick": "reset",
            "displaylogo": False,
            "displayModeBar": True,
            "scrollZoom": True,
        }
        df = pd.DataFrame.from_dict(Counter(count), orient="index")
        bar = px.bar(df, color_discrete_sequence=px.colors.qualitative.Dark2, color=df.index,
                     labels=dict(x="Cells", y="Counts"), title="Number of cells per cluster")
        bar.update_layout(barmode="stack", xaxis={"categoryorder": "total descending"})
        return [html.H4("PCA"), dcc.Graph(figure=fig, config=config), dcc.Graph(figure=bar)]

    return html.Div([
        html.Div(id=ids.GRAPH_2D),
        dcc.Slider(id=ids.KMEANS_SLIDER, min=1, max=10, step=1, value=3),
    ])


"""
@functools.lru_cache(maxsize=32)
    def call_dr(dr_type):
        match dr_type:
            case "PCA":
                return api.compute_pca()
            case "SVD":
                return api.compute_pca()
            case _:
                print("default")
        print("slow function called")
        return "Input was {}".format(input)
"""
