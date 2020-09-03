import random
import time
from trader import stockpickr
from trader import trader
import cira 

"""
Randy Random
"""


def random_stock():
  """ returns a random stock from NASDAQ  """
  market_assets = cira.nasdaq_assets()
  return market_assets[random.randint(0, len(market_assets))].symbol


def random_buy():
  """ buy a random stock """
  qty = random.randint(1, 100)
  sym = random_stock()
  return cira.buy(qty, sym)


def random_sell():
    """ sells random stock """
    qty = random.randint(1, 100)
    ownd_stocks = cira.owned_stocks()
    sym = ownd_stocks[random.randint(0, len(ownd_stocks)-1)]
    return cira.sell(qty, sym)


def instance():
  """ This func is the main behavior """
  random_buy()
  random_sell()


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
