import datetime, pytz
import api_comunication
import stockpickr

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
    print(buy_response.text)


def sell(qty, sym):
    endpoint = "positions/"+ sym
    sell_response = api_comunication.delete_request(endpoint)
    print(sell_response.text)
