import folium
import pandas as pd
from folium.plugins import HeatMap

m = folium.Map(location=[-33.918500, 151.229900], zoom_start=18)

# open csv file
df = pd.read_csv('merged_released.csv')

# get rows with not null values in network delay, ssid = uniwide and frequency = 5GHz
df_5ghz = df[(df['frequency'] == '5GHz') & (df['ssid'] == 'uniwide') & (df['network delay (ms)'].notna())]

# group by gps latitude and gps longitude and get the mean of rssi
data_5ghz = df_5ghz.groupby(['gps latitude', 'gps longitude'])['rssi'].mean().reset_index()

# create HeatMap and save it to html file
HeatMap(data_5ghz).add_to(m)
m.save("5ghz_heat.html")