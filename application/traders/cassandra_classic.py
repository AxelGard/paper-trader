import traders
import time

"""
Cassandra Classic
"""

def find_profit():
    lst = []
    for stock in traders.trader.ownd_stocks():
        if made_profit(stock):
            lst.append(stock)
    return lst


def made_profit(sym):
    plpc = traders.trader.stock_plpc(sym)
    profit_margen = 0.02
    return plpc > profit_margen


def run_cassandra():
    """ runs Cassandra forever """
    hour = 60 * 60
    print(" [*] Cassandra Classic is running ")
    while True:
        time.sleep(hour)
        if traders.trader.nasdaq_open():
            stock_profits = find_profit()
            traders.trader.sell_list(stock_profits)
            traders.randy_random.random_buy()
