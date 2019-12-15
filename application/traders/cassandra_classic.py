import traders
import time
import math

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


def find_losing_stock():
    losing_stocks = find_market_loss()
    lost_lst = []
    for sym in losing_stocks:
        pl_change = traders.trader.get_week_pl_change(sym)
        lost_lst.append(tuple(sym, pl_changel))
    lost_lst = sorted(lost_lst, key=lambda l:l[1])
    stock_at_lost = lost_lst[int(len(lost_lst)/2)]
    return stock_at_lost[0]


def investment_qty_lossing_stock(sym):
    pl_change = traders.trader.get_week_pl_change(sym)
    qty = int(math.sqrt(int(pl_changel)))
    return qty


def oneinstence_cassandra():
    stock_profits = find_profit()
    if stock_profits:
        print(stock_profits)
        traders.trader.sell_list(stock_profits)
    losing_stock = find_losing_stock()
    losing_stock_invst = investment_qty_lossing_stock(losing_stock)
    print(losing_stock + " : " + losing_stock_invst)
    traders.trader.buy(losing_stock_invst, losing_stock)
    #traders.randy_random.random_buy()


def run_cassandra():
    """ runs Cassandra forever """
    hour = 60 * 60
    print(" [*] Cassandra Classic is running ")
    while True:
        time.sleep(hour)
        if traders.trader.nasdaq_open():
            oneinstence_cassandra()
