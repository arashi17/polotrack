from moving_average import moving_average
import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

with open('../data/hist_usdt_btc.json', 'r') as f:
    hist = json.load(f)

start_time = int(datetime(2018,1,1).timestamp())
end_time = int(datetime(2019,1,24).timestamp())
timeframe_hours = 6
timeframe_minutes = timeframe_hours * 60

dt, mov_avg = moving_average(timeframe_minutes, start_time, end_time, hist)

plt.plot(dt)
plt.plot(mov_avg)
plt.show()
