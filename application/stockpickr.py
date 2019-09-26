import random
import time
from main import ownd_stock

def buy_dict():
    dict_ = {
    "symbol": "",
    "qty": 1,
    "side": "buy",
    "type": "market",
    "time_in_force": "day"
    }
    return dict_

def buy_payload(qty, sym):
    dict_ = buy_dict()
    dict_["symbol"] = sym
    dict_["qty"] = qty
    return dict_

def stock_list():
    stock_list = [
    "GOOGL",
    "AAPL",
    "CSCO",
    "AMD",
    "MSFT",
    "ULH",
    "QCOM",
    "SPI"
    ]
    return stock_list
