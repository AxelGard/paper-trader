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
    ownd_stocks = trader.get_ownd_stocks()
    sym = ownd_stocks[random.randint(0, len(ownd_stocks)-1)]
    response = trader.sell(qty, sym)
    return response

def run_randy():
    """ runs randy random for ever """
    print(" [*] randy random is running ")
    while (True):
        hour = 60*60
        time.sleep(random.randint(hour, hour*3))
        #time.sleep(hour)
        trader.nasdaq_time()
        #print("is nasdaq open : ", trader.nasdaq_open())
        if trader.nasdaq_open():
            buy = random_buy()
            time.sleep(random.randint(5, 50))
            sell = random_sell()
        print("BUY : ", buy.text, "\n\n\n SELL : ", sell.text)
        print("-"*30)
