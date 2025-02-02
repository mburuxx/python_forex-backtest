import requests
import pandas as pd
import defs

# Create a session for making HTTP requests
session = requests.Session()

# Define trading instrument, data count, and granularity
instrument = "EUR_USD"
count = 10
granularity = "H1"

# Construct API URL for fetching historical data and print url
url = f"{defs.OANDA_URL}/instruments/{instrument}/candles"
print(url) 

# Define request parameters
params = dict(
    count=count,
    granularity=granularity,
    price="MBA"  # Mid, Bid, and Ask prices
)

# Make GET request with parameters and authentication headers
response = session.get(url, params=params, headers=defs.SECURE_HEADER)
print(response.status_code) 

# Ensure the response is valid before processing data
if response.status_code != 200:
    print("Error fetching data:", response.text)
    exit()

# Convert response to JSON
data = response.json()
print(data.keys()) 

# Define price types and OHLC (Open, High, Low, Close) components
prices = ['mid', 'bid', 'ask']
ohlc = ['o', 'h', 'l', 'c']

# Print formatted column
for price in prices:
    for oh in ohlc:
        print(f"{price}_{oh}")

# Initialize list for storing structured historical data
historical_data = []
for candle in data.get('candles', []): 
    if not candle.get('complete', False):
        continue 

    # Create a dictionary for storing candle data
    new_dict = {
        'time': candle['time'], 
        'volume': candle['volume']
    }

    # Extract price data for each price type and OHLC component
    for price in prices:
        for oh in ohlc:
            new_dict[f"{price}_{oh}"] = candle[price][oh]

    historical_data.append(new_dict) 

# Convert list of dictionaries to a Pandas DataFrame
candles_df = pd.DataFrame.from_dict(historical_data)

# Save DataFrame as a pickle file for later use
candles_df.to_pickle("EUR_USD_H1.pkl")

# Load the saved pickle file to verify data persistence
test_data = pd.read_pickle("EUR_USD_H1.pkl")
print(test_data)
