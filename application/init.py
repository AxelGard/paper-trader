import trader
import datetime

if __name__ == '__main__':
    print(trader.nasdaq_time())
    print(trader.nasdaq_open())
    if trader.nasdaq_open():
        trader.buy(5, "GOOGL")
        trader.sell(5, "GOOGL")
