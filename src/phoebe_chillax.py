import time
from ..trader import trader


"""
Phoebe chillax
"""


def one_instance():
    """  """
    pass


def run_my_trader():
    """ runs  forever """
    hour = 60 * 60
    print(" [*] Phoebe is running ")
    print(" [*] is exchange open " + str(trader.exchange_open()))
    while True:
        if trader.exchange_open():
            one_instance()
            time.sleep(hour) # sleep time
