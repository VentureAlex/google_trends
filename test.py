import pandas as pd
from pytrends.request import TrendReq

# Set up a pytrends request
pytrends = TrendReq()

# Define the search parameters
kw_list = ["AAPL"]  # List of search terms
timeframe = 'today 5-y'  # Last 5 years

# Request the interest over time
pytrends.build_payload(kw_list, timeframe=timeframe)
interest_over_time_df = pytrends.interest_over_time()

# Instead of printing, save the DataFrame to a CSV file
interest_over_time_df.to_csv('interest_over_time.csv', index=True)

#
# Step 1: Load the data
df = pd.read_csv('interest_over_time.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# Step 2: Calculate percentage change
df['percent_change'] = df['AAPL'].pct_change() * 100  # Assuming 'NVDA' is the column of interest

# Step 3: Identify significant increases
# Defining a "significant" increase as more than 100% increase from the previous period
significant_increases = df[df['percent_change'] > 100]

print(significant_increases)