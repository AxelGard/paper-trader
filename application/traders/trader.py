import datetime, pytz, random
import api_controller
import traders.stockpickr as stockpickr
import json

def ownd_stock():
    """ keeps ownd stocks i memmory """
    global ownd_stock
    return ownd_stock

def nasdaq_time_old():
    """ gets the time in us Eastern for nasdaq """
    nyc_datetime = datetime.datetime.now(pytz.timezone('US/Eastern'))
    fmt = '%H:%M:%S'
    hour = nyc_datetime.strftime('%H')
    min = nyc_datetime.strftime('%M')
    time_set = (int(hour), int(min))
    return(time_set)


def nasdaq_open():
    """ returns if nasdaq is open """
    link = "v2/clock"
    response = api_controller.get_request(link)
    dict_ = json.loads(response.text)
    return dict_["is_open"]


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
    yesterday = today - datetime.timedelta(days=1)
    payload = {
        "symbols": sym,
        "limit": 1,
        "start": yesterday.strftime("%Y-%m-%d"),
        "end": today.strftime("%Y-%m-%d")
    }
    response = api_controller.get_data(payload)
    dict_ = json.loads(response.text)
    #{"GOOG":[{"t":1571803200,"o":1242.36,"h":1259.89,"l":1242.36,"c":1259.28,"v":814768}]}

    return dict_

def get_position():
    response = api_controller.get_request("v2/positions").text
    lst = json.loads(response)
    for dict_ in lst:
        for key in dict_.keys():
            try:
                dict_[key] = float(dict_[key])
            except ValueError:
                continue
    return lst

def stock_position(sym):
    url = "v2/positions" + str(sym)
    response = api_controller.get_request(url).text
    return json.loads(response)

def get_ownd_stocks():
    lst = get_position()
    stock_lst = []
    for dict_ in lst:
        stock_lst.append(dict_['symbol'])
    return stock_lst

def stock_today_plpc(sym):
    dict_ = stock_position(sym)
    for key in dict_.keys():
        try:
            dict_[key] = float(dict_[key])
        except ValueError:
            continue
    return float(dict_["unrealized_intraday_plpc"])


"""
{'asset_id': '762eca63-f335-4d9c-bfc5-83607ad4d8e9', 'symbol': 'WYNN', 'exchange': 'NASDAQ', 'asset_class': 'us_equity', 'qty': '24', 'avg_entry_price': '115.86', 'side': 'long', 'market_value': '2784.48', 'cost_basis': '2780.64', 'unrealized_pl': '3.84',
'unrealized_plpc': '0.0013809770412567', 'unrealized_intraday_pl': '7.68', 'unrealized_intraday_plpc': '0.0027657735522904', 'current_price': '116.02', 'lastday_price': '115.7', 'change_today': '0.0027657735522904'}
"""
