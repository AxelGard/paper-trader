import random
import time
import csv

"""
[*]==========================================================[*]
    This file is shuld not be used any more,
    its left for backward compatibility with v1.0 function.
[*]==========================================================[*]
"""

def buy_dict():
    """ holds dict for buy """
    dict_ = {
    "symbol": "",
    "qty": 1,
    "side": "buy",
    "type": "market",
    "time_in_force": "day"
    }
    return dict_

def buy_payload(qty, sym):
    """ builds payload buy """
    dict_ = buy_dict()
    dict_["symbol"] = sym
    dict_["qty"] = qty
    return dict_

def stock_list():
    """ gets stocks from local stock list file
    and returns them in a list  """
    stock_list = []
    stock_file = 'traders/lists/stock_list.csv'
    with open(stock_file, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            stock_list.append(row[0])
    return stock_list
