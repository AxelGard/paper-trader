import datetime, pytz, random
import api_controller
import traders.stockpickr as stockpickr


def ownd_stock():
    """ keeps ownd stocks i memmory """
    global ownd_stock
    return ownd_stock

def nasdaq_time():
    """ gets the time in us Eastern for nasdaq """
    nyc_datetime = datetime.datetime.now(pytz.timezone('US/Eastern'))
    fmt = '%H:%M:%S'
    hour = nyc_datetime.strftime('%H')
    min = nyc_datetime.strftime('%M')
    time_set = (int(hour), int(min))
    return(time_set)


def nasdaq_open():
    """ returns if nasdaq is open """
    return 10 <= nasdaq_time()[0] <= 16


def buy(qty, sym):
    """ buys a stock.
    takes int qty and a string sym """
    endpoint = "v2/orders"
    payload = stockpickr.buy_payload(qty, sym)
    buy_response = api_controller.post_request(endpoint, payload)
    #if sym not in ownd_stock:
        #ownd_stock.append(sym)
    return buy_response


def sell(qty, sym):
    """ sells a stock.
    takes int qty and a string sym"""
    global ownd_stock
    endpoint = "v2/positions/"+ sym
    sell_response = api_controller.delete_request(endpoint)
    #if sym in ownd_stock:
        #ownd_stock.remove(sym)
    return sell_response


def value_of_stock(sym):
    """ """
    #https://data.alpaca.markets/
    #v1/bars/day?
    today = datetime.date.today()
    payload = {
        "symbols": sym,
        "limit": 1,
        "start": today.strftime("%Y-%m-%d"),
        "end": today.strftime("%Y-%m-%d")
    }
    request = api_controller.get_data(payload)
    return request
