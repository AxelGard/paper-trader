import random
import datetime
import time
import traders.stockpickr as stockpickr
import traders.trader as trader

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

def run_randy():
    while (True):
        print(" [*] randy random is running ")
        time.sleep(random.randint(10, 120))
        #time.sleep(5)
        print(trader.nasdaq_time())
        print("is nasdaq open : ", trader.nasdaq_open())
        if trader.nasdaq_open():
            print(random_buy().text)
            time.sleep(random.randint(5, 50))
            print(random_sell().text)
