import random
import datetime
import time
from traders.trader import stockpickr
from traders.trader import trader

"""
Randy Random
"""


def random_pickr():
    """ picks a random stock form stock list """
    ran_pos = random.randint(0, len(stockpickr.stock_list())-1)
    return stockpickr.stock_list()[ran_pos]


def ownd_random():
    """ returns ownd stock """
    ran_pos = random.randint(0, len(trader.ownd_stock()))
    return stockpickr.stock_list()[ran_pos]


def random_buy():
    """ buy a random stock """
    qty = random.randint(1, 100)
    sym = random_pickr()
    response = trader.buy(qty, sym)
    return response


def random_sell():
    """ sells random stock """
    qty = random.randint(1, 100)
    ownd_stocks = trader.get_ownd_stocks()
    sym = ownd_stocks[random.randint(0, len(ownd_stocks)-1)]
    response = trader.sell(qty, sym)
    return response


def oneinstence_randy():
    buy = random_buy()
    time.sleep(random.randint(5, 50))
    sell = random_sell()


def run_randy():
    """ runs randy random for ever """
    print(" [*] randy random is running ")
    print(" [*] is NASDAQ open " + str(trader.exchange_open()))
    hour = 60*60
    while (True):
        if trader.exchange_open():
            oneinstence_randy()
        time.sleep(random.randint(hour, hour*3))
        #time.sleep(hour)
