import numpy as np

"""
timeframe in minutes
start in unix timestamp
end in unix timestamp
data in json from poloniex
"""
def moving_average(timeframe, start, end, data):
    # find start/ end indexes
    timestamp_dif = start - data[0]['date']
    if timestamp_dif < 0:
        print('Historical data not available.\n')
        return
    start_index = int(timestamp_dif / 300)
    end_index = start_index + int((end - start) / 300)
    total_samples = end_index - start_index + 1

    # determine number of samples in a timeframe
    data_sample_rate = 5
    number_of_samples = int(timeframe / data_sample_rate)

    # create data numpy array
    data_array = np.zeros(total_samples)
    for i in range(total_samples):
        data_array[i] = data[start_index + i]['weightedAverage']
    cum_sum = np.cumsum(data_array)
    avg_array = np.zeros(total_samples)
    for i in range(total_samples - number_of_samples):
        avg_array[number_of_samples + i] = cum_sum[number_of_samples + i] - cum_sum[i]
    avg_array /= number_of_samples
    return data_array, avg_array
