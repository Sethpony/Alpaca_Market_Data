import alpaca_trade_api as tradeapi
import pandas as pd
import config
import matplotlib.pyplot
import argparse
from util import load_config

# iex as source, what is IEX again?
# used for websocket connection - wss stands for web socket secure

# run the program with parser
# python data_visualize.py --config ./config_files/config_job_run.json

# first create argument parser object, then enact on that object
parser = argparse.ArgumentParser(
    description="retrieves arguments needed for using get_bars call from Alpaca Market Data API")
parser.add_argument('--config', action='store', nargs='+',
                    help='add input parameter for location of config file to run API call job')

args = parser.parse_args()
print(f'this the arguments that have been passed {args}')
print(f'this is the arguments that have been passed: {args.config}')


# print(f'args config 0 {args.config[0]}')
print(f'{load_config(args.config[0])}')

conf = load_config(args.config[0])
print(f'print conf:{conf}')
keys = conf

#todo: update .json file by using the paramters

#### start of API Calls ####
base_url = "wss://stream.data.alpaca.markets/v2/iex"

# set up auth credentials (key and secret key)
APCA_API_KEY_ID = config.APCA_API_KEY_ID
APCA_API_SECRET_KEY = config.APCA_API_SECRET_KEY

# create api object so we can make some calls
api = tradeapi.REST(key_id=APCA_API_KEY_ID, secret_key=APCA_API_SECRET_KEY,
                    base_url=base_url, api_version='v2')


if ('jobs' in keys):
    for job in conf['jobs']:
        print('printing the values tied to the jobs key')
        print(job)
        symbol = job['symbol']
        time_frame = job['time_frame']
        start_date = job['start_date']
        end_date = job['end_date']
        print(symbol)
        spy_bars = api.get_bars(symbol, time_frame, start_date, end_date)
        print(spy_bars)
        # spy_bars = api.get_bars(str(job['symbol']), str(job['time_frame']), str(job['start_date']), str(job['end_date']))
    # print(spy_bars)
    # spy_bars = api.get_bars(symbol, timeframe, start, end)

# symbol = "SPY"
# timeframe = "1Day"
# start = "2021-01-01"
# end = "2021-01-30"
# Retrieve daily bars for SPY in a dataframe and printing the first 5 rows
#spy_bars = api.get_bars(symbol, timeframe, start, end)
#print(spy_bars)
# spy_bars = api.get_trades('AAPL', '2020-01-25', '2020-01-30',5)
# print(spy_bars)


# plot stock data
# spy_bars.to_csv('market_data.csv')
# print("wrote market data")
#
# matplotlib.pyplot.plot(spy_bars['high'])
# matplotlib.pyplot.show()



