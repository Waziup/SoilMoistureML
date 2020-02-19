import pandas as pd
import matplotlib.pyplot as plt
import pylab


data = pd.read_csv('data with irrigation.csv', index_col=0, parse_dates=True);
#data.index = pd.to_datetime(data.timestamp, format='%Y-%m-%dT %H:%M:%S', errors='coerce')
plt.rcParams['figure.figsize'] = (18, 5)
plt.plot(data.index, data[['Plot 2 humidity','Plot 2 irrigation']])
plt.show()
