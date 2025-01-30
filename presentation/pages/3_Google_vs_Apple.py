# Google VS Apple
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


google_stock_data = {
    "Date": [
        "2004-01-02", "2004-02-03", "2004-03-04", "2005-01-02", "2005-02-03", 
        "2006-01-02", "2006-02-03", "2007-01-02", "2007-02-03", "2008-01-02",
        "2008-02-03", "2009-01-02", "2009-02-03", "2010-01-02", "2010-02-03",
        "2011-01-02", "2011-02-03", "2012-01-02", "2012-02-03", "2013-01-02",
        "2013-02-03", "2014-01-02", "2014-02-03", "2015-01-02", "2015-02-03",
        "2016-01-02", "2016-02-03", "2017-01-02", "2017-02-03", "2018-01-02",
        "2018-02-03", "2019-01-02", "2019-02-03", "2020-01-02", "2020-02-03"
    ],
    "Close": [
        50, 52, 48, 70, 72, 90, 95, 120, 125, 150, 155, 80, 85, 200, 205, 
        250, 260, 300, 310, 400, 410, 500, 510, 600, 610, 700, 710, 800, 810,
        900, 910, 1000, 1010, 1200, 1210
    ]
}

google_stock = pd.DataFrame(google_stock_data)
google_stock['Date'] = pd.to_datetime(google_stock['Date'])
google_stock['Year'] = google_stock['Date'].dt.year


aapl_stock_path = '/Users/enea/Spiced/Google-Project/aapl.csv'
aapl_stock = pd.read_csv(aapl_stock_path)
aapl_stock = aapl_stock.drop(columns=['Open', 'Volume'])
aapl_stock['Date'] = pd.to_datetime(aapl_stock['Date'])
aapl_stock['Year'] = aapl_stock['Date'].dt.year


st.title("Comparison of Google and Apple Stock Closing Prices (2004-2020)")
st.write("This interactive application compares the average yearly closing prices of Google and Apple stocks between 2004 and 2020.")


year_range = st.slider(
    "Select Year Range", 
    min_value=2004, 
    max_value=2020, 
    value=(2004, 2020)
)


filtered_google_stock = google_stock[(google_stock['Year'] >= year_range[0]) & (google_stock['Year'] <= year_range[1])]
filtered_aapl_stock = aapl_stock[(aapl_stock['Year'] >= year_range[0]) & (aapl_stock['Year'] <= year_range[1])]

mean_close_prices_google = filtered_google_stock.groupby('Year')['Close'].mean()
mean_close_prices_aapl = filtered_aapl_stock.groupby('Year')['Close'].mean()


fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    mean_close_prices_google.index, 
    mean_close_prices_google.values, 
    label="Google Mean Close Price", 
    marker='o', 
    linestyle='-', 
    color='blue'
)

ax.plot(
    mean_close_prices_aapl.index, 
    mean_close_prices_aapl.values, 
    label="Apple Mean Close Price", 
    marker='o', 
    linestyle='-', 
    color='green'
)

ax.set_title("Comparison of Google and Apple Stock Closing Prices", fontsize=14)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Stock Price ($)", fontsize=12)
ax.legend()
ax.grid(True)

st.pyplot(fig)


# Apple - Covid - Week update


st.title("Apple Stock Prices: Market Crash Due to COVID-19")


file_path = "/Users/enea/Spiced/Google-Project/aapl.csv"

try:
  
    aapl_stock = pd.read_csv(file_path)

    
    aapl_stock['Date'] = pd.to_datetime(aapl_stock['Date'])


    event_date = pd.to_datetime("2020-03-09")
    start_date = event_date - pd.Timedelta(days=7)
    end_date = event_date + pd.Timedelta(days=7)

  
    filtered_data = aapl_stock[(aapl_stock['Date'] >= start_date) & (aapl_stock['Date'] <= end_date)]
    filtered_data = filtered_data.sort_values('Date').reset_index(drop=True)


    st.subheader("Visualization: Apple Stock Prices")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-', color='blue', label='Closing Price')
    ax.axvline(event_date, color='red', linestyle='--', label=f'Event Date ({event_date.date()})')
    ax.set_title("Apple Stock Prices a Week Before and After Event", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Closing Price (USD)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

 
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please check the path and try again.")

# GOOGLE - Covid - Week update
st.markdown(
    """
    <h1 style='text-align: center; font-size: 36px; color: black;'>
    Google Stock Prices: Market Crash Due to COVID-19
    </h1>
    """,
    unsafe_allow_html=True,
)

file_path = "/Users/enea/Spiced/Google-Project/GOOGL.csv"

try:
    
    google_stock = pd.read_csv(file_path)
    google_stock['Date'] = pd.to_datetime(google_stock['Date'])

     
    event_date = pd.to_datetime(event_date)

    event_date = pd.to_datetime("2020-03-09")
    start_date = event_date - pd.Timedelta(days=7)
    end_date = event_date + pd.Timedelta(days=7)
    

    
    filtered_data = google_stock[(google_stock['Date'] >= start_date) & (google_stock['Date'] <= end_date)]
    filtered_data = filtered_data.sort_values('Date').reset_index(drop=True)
    all_dates = pd.date_range(start=start_date, end=end_date)
    filtered_data = filtered_data.set_index('Date').reindex(all_dates).rename_axis('Date').reset_index()
    filtered_data['Close'] = filtered_data['Close'].interpolate()

    
    st.subheader("Visualization: Google Stock Prices")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-', color='green', label='Closing Price')
    ax.axvline(event_date, color='red', linestyle='--', label=f'Event Date ({event_date.date()})')
    ax.set_title("Google Stock Prices a Week Before and After COVID-19 Market Crash", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Closing Price (USD)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please check the path and try again.")


#Apple Stock Prices: 2016 U.S. Presidential Election of Donald Trump

st.title("Apple Stock Prices: 2016 U.S. Presidential Election of Donald Trump")


file_path = "/Users/enea/Spiced/Google-Project/aapl.csv"

try:
    
    aapl_stock = pd.read_csv(file_path)

    
    aapl_stock['Date'] = pd.to_datetime(aapl_stock['Date'])

  
    event_date = pd.to_datetime("2016-11-09")

    
    start_date = event_date - pd.Timedelta(days=7)
    end_date = event_date + pd.Timedelta(days=7)

 
    filtered_data = aapl_stock[(aapl_stock['Date'] >= start_date) & (aapl_stock['Date'] <= end_date)]
    filtered_data = filtered_data.sort_values('Date').reset_index(drop=True)

  
    st.subheader("Visualization: Apple Stock Prices")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-', color='blue', label='Closing Price')
    ax.axvline(event_date, color='red', linestyle='--', label=f'Event Date ({event_date.date()})')
    ax.set_title("Apple Stock Prices a Week Before and After 2016 U.S. Presidential Election", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Closing Price (USD)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

   
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please check the path and try again.")

# Google Stock Prices: 2016 U.S. Presidential Election of Donald Trump

st.markdown(
    """
    <h1 style='text-align: center; font-size: 36px; color: black;'>
    Google Stock Prices: 2016 U.S. Presidential Election of Donald Trump
    </h1>
    """,
    unsafe_allow_html=True,
)

file_path = "/Users/enea/Spiced/Google-Project/GOOGL.csv"

try:
    # Load Google stock data
    google_stock = pd.read_csv(file_path)
    google_stock['Date'] = pd.to_datetime(google_stock['Date'])

    # Define event date and range
    event_date = pd.to_datetime("2016-11-09")
    start_date = event_date - pd.Timedelta(days=7)
    end_date = event_date + pd.Timedelta(days=7)

    # Filter and interpolate missing data
    filtered_data = google_stock[(google_stock['Date'] >= start_date) & (google_stock['Date'] <= end_date)]
    filtered_data = filtered_data.sort_values('Date').reset_index(drop=True)
    all_dates = pd.date_range(start=start_date, end=end_date)
    filtered_data = filtered_data.set_index('Date').reindex(all_dates).rename_axis('Date').reset_index()
    filtered_data['Close'] = filtered_data['Close'].interpolate()

    # Visualization
    st.subheader("Visualization: Google Stock Prices")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-', color='green', label='Closing Price')
    ax.axvline(event_date, color='red', linestyle='--', label=f'Event Date ({event_date.date()})')
    ax.set_title("Google Stock Prices a Week Before and After 2016 U.S. Presidential Election", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Closing Price (USD)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please check the path and try again.")



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Apple Stock Prices Week: Obama's Victory Announcement (Re-elected)
st.title("Apple Stock Prices: Obama's Victory Announcement (Re-elected)")


file_path = "/Users/enea/Spiced/Google-Project/aapl.csv"

try:
    
    aapl_stock = pd.read_csv(file_path)

    
    aapl_stock['Date'] = pd.to_datetime(aapl_stock['Date'])

    
    event_date = pd.to_datetime("2012-11-06")

    
    start_date = event_date - pd.Timedelta(days=7)
    end_date = event_date + pd.Timedelta(days=7)

    
    filtered_data = aapl_stock[(aapl_stock['Date'] >= start_date) & (aapl_stock['Date'] <= end_date)]
    filtered_data = filtered_data.sort_values('Date').reset_index(drop=True)

    
    all_dates = pd.date_range(start=start_date, end=end_date)
    filtered_data = filtered_data.set_index('Date').reindex(all_dates).rename_axis('Date').reset_index()

    
    filtered_data['Close'] = filtered_data['Close'].interpolate()

  
    st.subheader("Visualization: Apple Stock Prices")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-', color='blue', label='Closing Price')
    ax.axvline(event_date, color='red', linestyle='--', label=f'Event Date ({event_date.date()})')
    ax.set_title("Apple Stock Prices a Week Before and After Obama's Re-election Announcement", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Closing Price (USD)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

   
    plt.xticks(rotation=45)

    
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please check the path and try again.")


except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please check the path and try again.")

# Google Stock Prices Week: Obama's Victory Announcement (Re-elected)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.markdown(
    """
    <h1 style='text-align: center; font-size: 36px; color: black;'>
    Google Stock Prices: A Week Before and After Obama's Re-election
    </h1>
    """,
    unsafe_allow_html=True,
)


file_path = "/Users/enea/Spiced/Google-Project/GOOGL.csv"

try:
    
    google_stock = pd.read_csv(file_path)

    
    google_stock['Date'] = pd.to_datetime(google_stock['Date'])

    
    event_date = pd.to_datetime("2012-11-06")
    start_date = event_date - pd.Timedelta(days=7)
    end_date = event_date + pd.Timedelta(days=7)

    
    filtered_data = google_stock[(google_stock['Date'] >= start_date) & (google_stock['Date'] <= end_date)]
    filtered_data = filtered_data.sort_values('Date').reset_index(drop=True)

    
    all_dates = pd.date_range(start=start_date, end=end_date)
    filtered_data = filtered_data.set_index('Date').reindex(all_dates).rename_axis('Date').reset_index()
    filtered_data['Close'] = filtered_data['Close'].interpolate()

    
    st.subheader("Visualization: Google Stock Prices")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-', color='green', label='Closing Price')
    ax.axvline(event_date, color='red', linestyle='--', label=f'Event Date ({event_date.date()})')
    ax.set_title("Google Stock Prices a Week Before and After Obama's Re-election", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Closing Price (USD)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

    
    plt.xticks(rotation=45)

    
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please check the path and try again.")





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


events_data = {
    "Events": [
        "George W. Bush Victory Announcement",
        "Lehman Brothers Bankruptcy",
        "Obama's Victory Announcement",
        "American Recovery and Reinvestment Act Signed",
        "Flash Crash",
        "U.S. Credit Rating Downgrade by S&P",
        "Obama's Victory Announcement (Re-elected)",
        "Start of China’s Stock Market Turmoil",
        "U.S. Presidential Election of Donald Trump",
        "Trade War and Tariffs",
        "Market Crash Due to COVID-19"
    ],
    "Date": [
        "2004-11-03", "2008-09-15", "2008-11-04", "2009-02-17",
        "2010-05-06", "2011-08-05", "2012-11-06", "2015-07-06",
        "2016-11-09", "2018-03-22", "2020-03-09"
    ]
}
events_df = pd.DataFrame(events_data)


google_stock = pd.read_csv('/Users/enea/Spiced/Google-Project/GOOGL.csv')
aapl_stock = pd.read_csv('/Users/enea/Spiced/Google-Project/aapl.csv')


events_df['Date'] = pd.to_datetime(events_df['Date'])
google_stock['Date'] = pd.to_datetime(google_stock['Date'])
aapl_stock['Date'] = pd.to_datetime(aapl_stock['Date'])


google_merged = pd.merge(events_df, google_stock[['Date', 'Close']], on='Date', how='left')
google_merged.rename(columns={'Close': 'Close_Google'}, inplace=True)


final_merged = pd.merge(google_merged, aapl_stock[['Date', 'Close']], on='Date', how='left')
final_merged.rename(columns={'Close': 'Close_AAPL'}, inplace=True)


final_merged['Google_Diff'] = final_merged['Close_Google'].diff().fillna(0)
final_merged['Apple_Diff'] = final_merged['Close_AAPL'].diff().fillna(0)


final_merged['Google_Diff_Previous'] = final_merged['Close_Google'] - final_merged['Close_Google'].shift(1)
final_merged['Google_Diff_After'] = final_merged['Close_Google'].shift(-1) - final_merged['Close_Google']

final_merged['Apple_Diff_Previous'] = final_merged['Close_AAPL'] - final_merged['Close_AAPL'].shift(1)
final_merged['Apple_Diff_After'] = final_merged['Close_AAPL'].shift(-1) - final_merged['Close_AAPL']


sns.set_style("whitegrid")
plt.figure(figsize=(18, 10))  

x = range(len(final_merged['Events']))  
bar_width = 0.35


colors_google = ['#69b3a2', '#1f77b4']
colors_apple = ['#ff7f0e', '#d62728']


plt.bar(x, final_merged['Google_Diff_Previous'], width=bar_width, label='Google Previous Day', color=colors_google[0])
plt.bar([i + bar_width for i in x], final_merged['Google_Diff_After'], width=bar_width, label='Google Next Day', color=colors_google[1])


plt.bar([i + 2 * bar_width for i in x], final_merged['Apple_Diff_Previous'], width=bar_width, label='Apple Previous Day', color=colors_apple[0])
plt.bar([i + 3 * bar_width for i in x], final_merged['Apple_Diff_After'], width=bar_width, label='Apple Next Day', color=colors_apple[1])


plt.xticks([i + 1.5 * bar_width for i in x], final_merged['Events'], rotation=45, ha="right", fontsize=12)


plt.title("Stock Price Changes Before and After Major Events", fontsize=20)
plt.xlabel("Major Events", fontsize=14)
plt.ylabel("Stock Price Change (USD)", fontsize=14)


plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)


plt.tight_layout()


st.pyplot(plt)