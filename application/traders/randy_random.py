import random
import datetime
import time
import traders.stockpickr as stockpickr
import traders.trader as trader

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
    sym = random_pickr()
    response = trader.sell(qty, sym)
    return response

def run_randy():
    """ runs randy random for ever """
    while (True):
        #print(" [*] randy random is running ")
        time.sleep(random.randint(10, 120))
        #time.sleep(5)
        trader.nasdaq_time()
        #print("is nasdaq open : ", trader.nasdaq_open())
        if trader.nasdaq_open():
            random_buy()
            time.sleep(random.randint(5, 50))
            random_sell()
