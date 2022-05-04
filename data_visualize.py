import alpaca_trade_api as tradeapi
import pandas as pd
import config
import matplotlib.pyplot
import argparse
import json

# iex as source, what is IEX again?
# used for websocket connection - wss stands for web socket secure

# run the program with parser
# python data_visualize.py --config ./config_files/config_job_run.json

parser = argparse.ArgumentParser(description='run get_bars for a symbol, timeframe, start, and end time')
parser.add_argument('--config', action='store', nargs='+' , default=None,
                    help='config file that lists all arguments we need for a run')
args = parser.parse_args()
print(args)
print(args.config[0])

config_filename = args.config


# create load_conf method that creates a json object from the config.json file
# def load_conf(config_filename):
#     if ('.json' in config_filename):
#         json_file = json.load(open(config_filename))
#         return json_file
#     else:
#         print("not a valid json file")
#
#
# if args.config is not None:

    # conf = load_conf(args.config)
    # keys = conf.keys
    #
    # if('jobs' in keys):
    #     for job in conf['jobs']:
    #         print('run')
    #         print(job)


base_url = "wss://stream.data.alpaca.markets/v2/iex"

# set up auth credentials (key and secret key)
APCA_API_KEY_ID = config.APCA_API_KEY_ID
APCA_API_SECRET_KEY = config.APCA_API_SECRET_KEY

# create api object so we can make some calls
api = tradeapi.REST(key_id=APCA_API_KEY_ID, secret_key=APCA_API_SECRET_KEY,
                    base_url=base_url, api_version='v2')

symbol = "SPY"
timeframe = "1Day"
start = "2021-01-01"
end = "2021-01-30"
# Retrieve daily bars for SPY in a dataframe and printing the first 5 rows
spy_bars = api.get_bars(symbol, timeframe, start, end)
# print(spy_bars)
# spy_bars = api.get_trades('AAPL', '2020-01-25', '2020-01-30',5)
# print(spy_bars)


# plot stock data
# spy_bars.to_csv('market_data.csv')
# print("wrote market data")
#
# matplotlib.pyplot.plot(spy_bars['high'])
# matplotlib.pyplot.show()


# run the program with parser
# python data_visualize.py --config ./config_files/config_job_run.json
