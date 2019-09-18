import trader
import datetime
import time
import random

#trader.buy(5, "GOOGL")
#trader.sell(5, "GOOGL")

ownd_stock = []

if __name__ == '__main__':
    while (True):
        time.sleep(random.randint(10, 900))
        #time.sleep(5)
        print(trader.nasdaq_time())
        #print(trader.nasdaq_open())
        if trader.nasdaq_open():
            trader.random_buy()
