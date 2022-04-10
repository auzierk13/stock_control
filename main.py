import configparser
import json

from stock_control import StockControl
from stock_view import StocksView

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("config.ini")
    config.sections()
    stocks = json.loads(config.get('stocks', "names"))
    stock_handled = StockControl(stocks)
    stock_view = StocksView(stock_handled)
    stock_view.run_sever()
    # stock_handled.search("IRBR3")
