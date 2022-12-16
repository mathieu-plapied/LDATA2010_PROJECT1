import dash
from dash import Dash, html, dcc
from src.components.layout import create_layout

from dash_bootstrap_components.themes import BOOTSTRAP


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# stylesheet_path = "assets/stylesheet.css"

def main():
    app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
    app.title = "LDATA2010 Project"
    app.layout = create_layout(app)
    app.run_server(debug=True)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
