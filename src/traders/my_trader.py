import time
import traders


"""
My Trader is for you to build and use 
"""


def one_instance():
    """ what you want the trader to do """
    pass 


def run_my_trader():
    """ runs  forever """
    hour = 60 * 60
    print(" [*] my_trader is running ")
    print(" [*] is exchange open " + str(traders.trader.exchange_open()))
    while True:
        if traders.trader.exchange_open():
            one_instance()
            time.sleep(hour) # sleep time  
