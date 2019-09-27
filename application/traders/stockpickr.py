import random
import time
import csv

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
    stock_list = []
    with open('traders/stock_list.csv', 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            stock_list.append(row[0])
    return stock_list
