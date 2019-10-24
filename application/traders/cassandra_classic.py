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


def made_profit(sym):
    plpc = traders.trader.stock_today_plpc(sym)
    profit_margen = 0.002
    return plpc > profit_margen


def run_cassandra():
    """ runs Cassandra """
    hour = 60 * 60
    while True:
        time.sleep(2)
        if traders.trader.nasdaq_open():
            stock_profits = find_profit()
            traders.trader.sell_list(sym)
            traders.randy_random.random_buy()
