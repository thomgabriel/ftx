from api import FtxClient
import datetime as dt
import pandas as pd
import dateparser

ftx = FtxClient()
market_name = 'BTC/USD'
resolution = 900 # TimeFrame in seconds.
limit = 10000
start_time = (dt.datetime.fromisoformat('2020-07-05 00:00:00'))
end_time = (dt.datetime.now().timestamp())

ohlcv = pd.DataFrame(data=ftx.get_historical_data(market_name,resolution,limit,start_time.timestamp(),end_time))
ohlcv.columns = ["Close", "High", "Low", "Open","datetime", 'time', "Volume"]
ohlcv.index = ohlcv.datetime.apply(lambda x: dateparser.parse(x[:18]))

print(ohlcv)



# for x in ftx.list_markets():
#     print(x['name'])
