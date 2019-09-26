import datetime, pytz, random
import api_comunication
import stockpickr
from main import ownd_stock
from traders import randy_random

def nasdaq_time():
    nyc_datetime = datetime.datetime.now(pytz.timezone('US/Eastern'))
    fmt = '%H:%M:%S'
    hour = nyc_datetime.strftime('%H')
    min = nyc_datetime.strftime('%M')
    time_set = (int(hour), int(min))
    return(time_set)


def nasdaq_open():
    return 10 <= nasdaq_time()[0] <= 16


def buy(qty, sym):
    endpoint = "orders"
    payload = stockpickr.buy_payload(qty, sym)
    buy_response = api_comunication.post_request(endpoint, payload)
    if sym not in ownd_stock:
        ownd_stock.append(sym)
    return buy_response.text


def sell(qty, sym):
    endpoint = "positions/"+ sym
    sell_response = api_comunication.delete_request(endpoint)
    if sym in ownd_stock:
        ownd_stock.remove(sym)
    return sell_response.text
