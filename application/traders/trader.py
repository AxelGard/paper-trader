import datetime, pytz, random
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
    clock = api.get_clock()
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
    return order


def sell(qty, sym):
    """ sells a stock.
    takes int qty and a string sym"""
    order = order(sym, qty, 'sell')
    return order


def value_of_stock(sym):
    """ takes a string sym.
    Gets and returns the stock value at close """
    barset = api().get_barset(sym, 'day', limit=1)
    value  = barset[sym][0].c # get stock at close
    return value


def get_position():
    portfolio = api().list_positions()
    portfolio_lst = []
    for position in portfolio:
        raw_position = vars(position)['_raw']
        position_dict = {}
        for key in raw_position.keys():
            try:
                position_dict[key] = float(raw_position.key)
            except ValueError:
                continue
        portfolio_lst.append(position_dict)
    return portfolio_lst

def is_tradable(sym):
    asset = api().get_asset(sym)
    return aapl_asset.tradable


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

def clean_position(dict_):
    for key in dict_.keys():
        try:
            dict_[key] = float(dict_[key])
        except ValueError:
            continue
    return dict_

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


def sell_list(lst):
    print(lst)
    test_sell = 1
    for sym in lst:
        response = sell(1, sym)
        print(response.text)

"""dict_ = json.loads(response.text)
print(dict_['code'])
if dict_['code'] == not_avialabel_error_code:
    response = sell(test_sell, sym)
    print(response.text)
#print(response.text)"""

"""
{'asset_id': '762eca63-f335-4d9c-bfc5-83607ad4d8e9', 'symbol': 'WYNN', 'exchange': 'NASDAQ', 'asset_class': 'us_equity', 'qty': '24', 'avg_entry_price': '115.86', 'side': 'long', 'market_value': '2784.48', 'cost_basis': '2780.64', 'unrealized_pl': '3.84',
 'unrealized_plpc': '0.0013809770412567', 'unrealized_intraday_pl': '7.68', 'unrealized_intraday_plpc': '0.0027657735522904', 'current_price': '116.02', 'lastday_price': '115.7', 'change_today': '0.0027657735522904'}
"""
