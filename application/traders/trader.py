import datetime, pytz, random
import api_controller
import traders.stockpickr as stockpickr


def ownd_stock():
    global ownd_stock
    return ownd_stock

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
    buy_response = api_controller.post_request(endpoint, payload)
    #if sym not in ownd_stock:
        #ownd_stock.append(sym)
    return buy_response


def sell(qty, sym):
    global ownd_stock
    endpoint = "positions/"+ sym
    sell_response = api_controller.delete_request(endpoint)
    #if sym in ownd_stock:
        #ownd_stock.remove(sym)
    return sell_response
