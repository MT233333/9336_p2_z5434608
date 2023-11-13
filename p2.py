import folium
import pandas as pd
from folium.plugins import HeatMap

m = folium.Map(location=[-33.918500, 151.229900], zoom_start=18)

# open csv file
df = pd.read_csv('merged_released.csv')
# get rows with not null values in network delay column and with ssid = uniwide
df1 = df[(df['ssid'] == "uniwide")  & (df['network delay (ms)'].notna())]
# group by gps latitude and gps longitude and get the mean of rssi
data = df1.groupby(['gps latitude', 'gps longitude'])['rssi'].mean().reset_index()
print(data)

# create HeatMap and save it to html file
HeatMap(data).add_to(m)
m.save("rssi_heat.html")
