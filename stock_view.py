from dash import Dash
from dash.html import H1, H2, Div, P
from dash.dcc import Graph
from stock_control import StockControl
from stock_data import StockData


class StocksView:
    def __init__(self, stock_control: StockControl):
        self.external_stylesheets = [
            "https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css"]
        self.app = Dash(__name__, external_stylesheets=self.external_stylesheets)
        self.paper_bgcolor = "#222225"
        self.color_font = "#e8e9ed"
        self.size_font = 30
        self.control = stock_control

    def create_layout(self):
        # children = [
        #     H1("Grafico de ações"),
        #     H2("Ação abc")
        # ]
        children = self.create_graph()
        self.app.layout = Div(
            children
        )

    def create_figure(self, stock: StockData):
        # https://dash.plotly.com/layout
        points = self.control.get_historical(stock.code, to_date=self.control.day_now)

        new_data = {
            "data": [
                {
                    "x": points.axes[0].values,
                    "y": points.values,
                    "name":"Historical value"
                },
                {
                    "x": ['2022-01-01T00:00:00.000000000', f'2022-04-01T00:00:00.000000000'],
                    "y": [stock.average, stock.average],
                    "name": "Average value"
                }
            ],
            "layout": {
                "title": f"{stock.name}({stock.code})",
                "paper_bgcolor": self.paper_bgcolor,
                "titlefont":
                    {
                        "size": self.size_font,
                        "color": self.color_font
                    }

            }
        }
        return new_data

    def run_sever(self):
        self.create_layout()
        self.app.run_server(debug=True)

    def create_graph(self):
        graphs = []
        for stock in self.control.stocks_list:
            graphs.append(
                Graph(
                    figure=self.create_figure(stock)
                )
            )
        return graphs
