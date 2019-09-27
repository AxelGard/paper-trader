import datetime
import time
import random
from traders import randy_random, trader, stockpickr

#trader.buy(5, "GOOGL")
#trader.sell(5, "GOOGL")

if __name__ == '__main__':
    print(stockpickr.stock_list())
    while (True):
        time.sleep(random.randint(10, 120))
        #time.sleep(5)
        print(trader.nasdaq_time())
        print("is nasdaq open : ", trader.nasdaq_open())
        if trader.nasdaq_open():
            print(randy_random.random_buy().text)
            time.sleep(random.randint(5, 50))
            print(randy_random.random_sell().text)
