import alpaca_trade_api as tradeapi
import json

def authentication_header():
    with open('key.json', 'r') as file:
        header = json.load(file)
    return header


auth_header = authentication_header()
APCA_API_BASE_URL = "https://paper-api.alpaca.markets/"
APCA_API_KEY_ID = str(auth_header["APCA-API-KEY-ID"])
APCA_API_SECRET_KEY = str(auth_header["APCA-API-SECRET-KEY"])


if __name__ == '__main__':
    """
    With the Alpaca API, you can check on your daily profit or loss by
    comparing your current balance to yesterday's balance.
    """

    # First, open the API connection
    api = tradeapi.REST(
        APCA_API_KEY_ID,
        APCA_API_SECRET_KEY,
        'https://paper-api.alpaca.markets', api_version='v2'
    )

    # Get account info
    account = api.get_account()

    order = api.submit_order(symbol, 1, 'sell', 'market', 'day')
    print("Market order submitted.")


    symbol_bars = api.get_barset(symbol, 'minute', 1).df.iloc[0]
    symbol_price = symbol_bars[symbol]['close']


    order = api.submit_order(symbol, 1, 'sell', 'limit', 'day', symbol_price)
