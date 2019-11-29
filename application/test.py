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
        'https://paper-api.alpaca.markets'
    )

    # Get account info
    account = api.get_account()

    active_assets = api.list_assets(status='active')
    # Filter the assets to NASDAQ
    nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']

    portfolio = api.list_positions()
    portfolio = portfolio[:1]
    for position in nasdaq_assets:
        #print("{} shares of {}".format(position.qty, position.unrealized_plpc))
        print(position.symbol)
        #print(vars(position)['_raw'].keys())
    print(vars(nasdaq_assets[0]))
