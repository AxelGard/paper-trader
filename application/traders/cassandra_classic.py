import traders
import time

"""
Cassandra Classic
"""


def find_profit():
    lst = []
    ownd_stocks = traders.trader.ownd_stocks()
    #print(ownd_stocks)
    for stock in ownd_stocks:
        if made_profit(stock):
            lst.append(stock)
    return lst


def made_profit(sym):
    plpc = traders.trader.stock_plpc(sym)
    profit_margen = 0.02
    return plpc > profit_margen


def find_loss():
    lst = []
    ownd_stocks = traders.trader.ownd_stocks()
    for stock in ownd_stocks:
        if made_loss(stock):
            lst.append(stock)
    return lst


def made_loss(sym):
    plpc = traders.trader.stock_plpc(sym)
    loss_margen = -0.065
    return plpc < loss_margen


def find_market_loss():
    market_assets = traders.trader.nasdaq_assets()
    loss_lst = []
    for asset in market_assets:
        sym = asset.symbol
        if market_made_loss(sym):
            loss_lst.append(sym)
    return loss_lst


def market_made_loss(sym):
    plpc = traders.trader.stock_plpc(sym)
    loss_margen = -0.1
    return plpc < loss_margen


def run_cassandra():
    """ runs Cassandra forever """
    hour = 60 * 60
    print(" [*] Cassandra Classic is running ")
    while True:
        time.sleep(hour)
        if traders.trader.nasdaq_open():
            stock_profits = find_profit()
            if stock_profits:
                print(stock_profits)
                traders.trader.sell_list(stock_profits)
            traders.randy_random.random_buy()
