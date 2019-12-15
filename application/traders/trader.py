import datetime, pytz, random
from time import gmtime, strftime
import api_controller
import traders.stockpickr as stockpickr
import json
import alpaca_trade_api as tradeapi


def authentication_header():
    with open('key.json', 'r') as file:
        header = json.load(file)
    return header


def api():
    auth_header = authentication_header()
    APCA_API_KEY_ID = str(auth_header["APCA-API-KEY-ID"])
    APCA_API_SECRET_KEY = str(auth_header["APCA-API-SECRET-KEY"])
    # Open the API connection
    api = tradeapi.REST(
        APCA_API_KEY_ID,
        APCA_API_SECRET_KEY,
        'https://paper-api.alpaca.markets'
    )
    # Get account info
    account = api.get_account()
    return api


def nasdaq_open():
    """ returns if nasdaq is open """
    clock = api().get_clock()
    return clock.is_open


def order(sym, qty, beh):
    """ submit order and is a
    template for order """
    order = api().submit_order(
        symbol=sym,
        qty=qty,
        side=beh,
        type='market',
        time_in_force='gtc')

    return order


def buy(qty, sym):
    """ buys a stock.
    takes int qty and a string sym """
    order = order(sym, qty, 'buy')
    tim = strftime("%Y-%m-%d %H:%M", gmtime())
    log(format_log_action('buy',sym, qty, tim))
    return order


def sell(qty, sym):
    """ sells a stock.
    takes int qty and a string sym"""
    order = order(sym, qty, 'sell')
    tim = strftime("%Y-%m-%d %H:%M", gmtime())
    log(format_log_action('sell',sym, qty, tim))
    return order


def short(sym):
    """Short a stock, will need more investigation """
    if is_shortable(sym):
        pass


def is_shortable(sym):
    asset = api().get_asset(sym)
    return asset.shortable


def value_of_stock(sym):
    """ takes a string sym.
    Gets and returns the stock value at close """
    barset = api().get_barset(sym, 'day', limit=1)
    value  = barset[sym][0].c # get stock at close
    return value


def get_week_pl_change(sym):
    """ """
    barset = api.get_barset(sym, 'day', limit=5)
    bars = barset[sym]

    week_open = bars[0].o
    week_close = bars[-1].c
    return (week_close - week_open) / week_open


def get_position():
    portfolio = api().list_positions()
    portfolio_lst = []
    for position in portfolio:
        position_dict = clean_position(position)
        portfolio_lst.append(position_dict)
    return portfolio_lst


def is_tradable(sym):
    asset = api().get_asset(sym)
    return asset.tradable


def nasdaq_assets():
    active_assets = api().list_assets(status='active')
    # Filter the assets to NASDAQ
    return [a for a in active_assets if a.exchange == 'NASDAQ']


def stock_position(sym):
    return api().get_position(sym)


def ownd_stock_qty(sym):
    position = clean_position(stock_position(sym))
    return position['qty']


def ownd_stocks():
    lst = get_position()
    stock_lst = []
    for dict_ in lst:
        stock_lst.append(dict_['symbol'])
    return stock_lst


def clean_position(position):
    raw_position = vars(position)['_raw']
    position_dict = {}
    for key in raw_position.keys():
        try:
            position_dict[key] = float(raw_position.key)
        except ValueError:
            continue
    return position_dict


def stock_today_plpc(sym):
    dict_ = clean_position(stock_position(sym))
    return dict_['unrealized_intraday_plpc']


def stock_plpc(sym):
    dict_ = clean_position(stock_position(sym))
    return dict_['unrealized_plpc']


def nuclear_bomb():
    print(" [*] --> NUCLEAR BOMB has been droped (!) ")
    endpoint = "v2/positions"
    response = api_controller.delete_request(endpoint)
    return response


def nuclear_bomb_2():
    print(" [*] --> NUCLEAR BOMB has been droped (!) ")
    stocks_sym = ownd_stocks()
    for sym in stocks_sym:
        qty = ownd_stock_qty(sym)
        order = sell(qty, sym)


def sell_list(lst):
    print(lst)
    for sym in lst:
        qty = int(ownd_stock_qty(sym))
        response = sell(qty, sym)
        #print(response.text)


def format_log_action(act, sym, qty, time_):
    log_str = ""
    log_data = [act, sym, qty, time_]
    for data in log_data:
        log_str += str(data) + ","
    log_str = log_str[:-1]
    return log_str


def log(log_data):
    file_path = "traders/log/log.csv"
    with open(file_path, 'a') as fd:
        fd.write(log_data)

    """
    file_path = 'application/traders/log/log.json'
    data = json.load(open(file_pathp))
    if type(data) is dict:
        data = [data]

    data.append(log_data)

    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)
    """
