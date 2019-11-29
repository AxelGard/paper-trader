import alpaca_trade_api as tradeapi

APCA_API_BASE_URL = "https://paper-api.alpaca.markets/"
APCA_API_KEY_ID = "PK2BS2WDXP6ZGCH3E9D3"
APCA_API_SECRET_KEY = "Gkxe3Go7ArZ4z4mR8z928ePV3dKnvzSTRPzfF/SA"


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


    portfolio = api.list_positions()
    portfolio = portfolio[:1]
    for position in portfolio:
        #print("{} shares of {}".format(position.qty, position.unrealized_plpc))
        #print(dir(position))
        print(vars(position)['_raw'].keys())
