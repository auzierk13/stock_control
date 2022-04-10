from datetime import datetime
import investpy
import pandas as pd

from stock_data import StockData

# https://readthedocs.org/projects/investpy/downloads/pdf/latest/


class StockControl:
    def __init__(self, stocks_names):
        self.stocks_names = stocks_names
        self.day_now = datetime.now().strftime("%d/%m/%Y")
        self.stocks_list = []
        self.stocks_average = {"IRBR3": 2.3, "CIEL3": 2.5, "TAEE11": 36.15}  # TODO next step search in db
        self.load()

    def load(self):
        for name in self.stocks_names:
            self.search(name)
            print(f"Search {name} success")

    def search(self, name):
        try:
            search_results = investpy.search_quotes(text=name, products=["stocks"], countries=["brazil"], n_results=50)
        except Exception as e:
            print(f"Error: {e}")
        else:
            search_result = search_results[0]
            name = search_result.name
            code = search_result.symbol
            try:
                average = self.stocks_average[code]
            except KeyError:
                print(f"Warring: Add new average {code}")
                average = 2.0
            stock_data = StockData(name, code, average)
            self.stocks_list.append(stock_data)

    @staticmethod
    def get_historical(name="PETR4", from_date="01/01/2022", to_date="01/04/2022", country="brazil"):
        """

        :param name:
        :param from_date:
        :param to_date:
        :param country:
        :return:
        """
        try:
            petro = investpy.get_stock_historical_data(name, country, from_date, to_date)
        except Exception as e:
            print(f"Error {e}")
        else:
            points = pd.to_numeric(petro["Close"], errors="coerce")
            return points
