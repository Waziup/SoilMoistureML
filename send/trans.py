import pandas as pd
import matplotlib.pyplot as plt
import pylab

def getObs(myfile, name):
   obs = pd.read_csv(myfile,
                     sep=',',
                     parse_dates=[0]).drop('date_received',1);
   
   obs['value'] = obs['value'].apply(pd.to_numeric, errors='coerce')
   obs2 = obs.drop_duplicates('timestamp', keep='last').set_index('timestamp')
   obs2.index = pd.to_datetime(obs2.index, format='%Y-%m-%dT%H:%M:%S.%fZ')
   obs3 = obs2.resample('5min').mean()
   obs3['value'].interpolate('time', inplace=True, limit_direction='both')
   obs4 = obs3.round({'value': 2})
   obs4.rename(columns={'value': name}, inplace=True)
   return(obs4);

def getWeather(myfile, name):
   obs = pd.read_csv(myfile,
                     sep=',',
                     parse_dates=[4]).drop(['device_id', 'sensor_id', 'date_received'], axis=1);
   
   obs['value'] = obs['value'].apply(pd.to_numeric, errors='coerce')
   obs2 = obs.drop_duplicates('timestamp', keep='last').set_index('timestamp')
   obs2.index = pd.to_datetime(obs2.index, format='%Y-%m-%dT%H:%M:%SZ', errors='coerce')
   obs3 = obs2.resample('5min').mean()
   obs3['value'].interpolate('time', inplace=True, limit_direction='both')
   obs4 = obs3.round({'value': 2})
   obs4.rename(columns={'value': name}, inplace=True)
   return(obs4);

obs1 = getObs('UGB-PILOTS_Sensor80-SH.csv', 'soil');
obs1['obs1 min'] = (obs1.soil.shift(1) > obs1.soil) & (obs1.soil.shift(-1) > obs1.soil);

obs = [obs1, getObs('UGB-PILOTS_Sensor80-SH.csv', 'Soil humidity 1'),
       getObs('UGB-PILOTS_Sensor81-SH.csv', 'Soil humidity 2'),
       getObs('UGB-PILOTS_Sensor82-SH.csv', 'Soil humidity 3'),
       getObs('UGB-PILOTS_Sensor84-SH.csv', 'Soil humidity 4'),
       getWeather('TP.csv', 'Air temperature (C)'),
       getWeather('HD.csv', 'Air humidity (%)'),
       getWeather('PA.csv', 'Pressure (KPa)'),
       getWeather('WS.csv', 'Wind speed (Km/h)'),
       getWeather('WG.csv', 'Wind gust (Km/h)'),
       getWeather('WD.csv', 'Wind direction (Deg)'),
       ]

merged = reduce(lambda x, y: pd.merge(x, y, on = 'timestamp', how='outer'), obs)

#merged = merged.drop(pd.date_range('2018-01-01', '2019-03-12'), errors='ignore')
#merged = merged[~merged['timestamp'].isin(pd.date_range(start='20150210', end='20190312'))]

merged = merged.loc['2019-02-23':'2019-06-20']
#merged = merged.loc['2019-01-01':'2019-06-20']

# Print the first 5 entries
print(merged.head(10));
print(obs1)
#merged.to_csv('test.csv');
# Make the graphs a bit prettier
#pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (28, 5)

# Plot the first 500 entries with selected columns
#merged[['Soil humidity 1', 'Soil humidity 2', 'Soil humidity 3', 'Soil humidity 4']].plot();
merged[['Soil humidity 2', 'obs1 min']].plot();
pylab.show()
