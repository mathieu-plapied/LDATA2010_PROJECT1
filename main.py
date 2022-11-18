from dash import Dash, html, dcc
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP


def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "LDATA2010 Project"
    app.layout = create_layout(app)
    app.run()


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
