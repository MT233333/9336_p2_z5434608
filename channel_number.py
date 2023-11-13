import pandas as pd


# open csv file
df = pd.read_csv('merged_released.csv')

# get the 2.4GHz uniwide data
df_2p4ghz = df[(df['frequency'] == '2.4GHz') & (df['ssid'] == 'uniwide')]

# get other 2.4GHz data
df_other = df[(df['frequency'] == '2.4GHz') & (df['ssid'] != 'uniwide')]

# get the unique data
data_2p4ghz = df_2p4ghz[['bssid', 'channel']].drop_duplicates()
data_other = df_other[['bssid', 'channel']].drop_duplicates()


# get the number of occurrences of each unique channel
num_channels_data2 = data_2p4ghz['channel'].value_counts()
num_channels_data3 = data_other['channel'].value_counts()

# print the result
print(f"Number of occurrences of each unique channel in data2:\n{num_channels_data2}")
print(f"Number of occurrences of each unique channel in data3:\n{num_channels_data3}")

