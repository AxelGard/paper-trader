import random
import stockpickr

def random_pickr():
    ran_pos = random.randint(0, len(stock_list()))
    return stockpickr.stock_list()[ran_pos]


def ownd_random():
    ran_pos = random.randint(0, len(ownd_stock()))
    return stockpickr.stock_list()[ran_pos]


def random_buy():
    qty = random.randint(1, 10)
    sym = random_pickr()
    response = trader.buy(qty, sym)
    return response.text
