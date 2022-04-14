import alpaca_trade_api as tradeapi
import pandas as pd

import config
import matplotlib.pyplot
import seaborn as sns

#iex as source, what is IEX again?
#used for websocket connection - wss stands for web socket secure


base_url = "wss://stream.data.alpaca.markets/v2/iex"

#set up auth credentials (key and secret key)
APCA_API_KEY_ID = config.APCA_API_KEY_ID
APCA_API_SECRET_KEY = config.APCA_API_SECRET_KEY

#create api object so we can make some calls
api = tradeapi.REST(key_id=APCA_API_KEY_ID, secret_key=APCA_API_SECRET_KEY,
                    base_url=base_url, api_version='v2')

symbol = "SPY"
timeframe = "1Day"
start = "2021-01-01"
end = "2021-01-30"
# Retrieve daily bars for SPY in a dataframe and printing the first 5 rows
spy_bars = api.get_bars(symbol, timeframe, start, end).df
spy_bars.to_csv('market_data.csv')
print("wrote market data")

matplotlib.pyplot.plot(spy_bars['high'])
matplotlib.pyplot.show()



