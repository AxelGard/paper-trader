import random
from traders import stockpickr
from traders import trader

def random_pickr():
    ran_pos = random.randint(0, len(stockpickr.stock_list())-1)
    return stockpickr.stock_list()[ran_pos]


def ownd_random():
    ran_pos = random.randint(0, len(trader.ownd_stock()))
    return stockpickr.stock_list()[ran_pos]


def random_buy():
    qty = random.randint(1, 10)
    sym = random_pickr()
    response = trader.buy(qty, sym)
    return response

def random_sell():
    qty = random.randint(1, 10)
    sym = random_pickr()
    response = trader.sell(qty, sym)
    return response
