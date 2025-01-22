import pandas as pd
import plotly.graph_objects as go
import streamlit as st


from PIL import Image 


image_path = '/Users/enea/Spiced/Google-Project/streamlit_final/google_alphabet.webp'
image = Image.open(image_path)

st.image(image, caption="Google Alphabet Logo", use_container_width=True)

# Image 1

st.title('YouTube Acquisition by Google')

# Load and display the image
image_path = '/Users/enea/Spiced/Google-Project/youtube.png'
image = Image.open(image_path)

# Display the image in Streamlit
st.image(image, caption="Google's Acquisition of YouTube", use_container_width=True)


# 1st PLOT

st.title('Google Stock Analysis: Highest and Lowest Prices')

st.header('Showing stock prices from 2004 to 2020')
st.write("Let's show the highest and lowest stock prices of Google over the years.")


google_stock = pd.read_csv('/Users/enea/Spiced/Google-Project/GOOGL.csv')

google_stock['Date'] = pd.to_datetime(google_stock['Date'])

google_stock['Year'] = google_stock['Date'].dt.year

google_stock_filtered = google_stock[(google_stock['Year'] >= 2004) & (google_stock['Year'] <= 2020)]

lowest_prices = google_stock_filtered.groupby('Year')['Low'].min()
highest_prices = google_stock_filtered.groupby('Year')['High'].max()

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=lowest_prices.index, 
        y=lowest_prices.values, 
        mode='lines+markers', 
        name='Lowest Price', 
        line=dict(color='red'), 
        marker=dict(color='red', size=8)
    )
)

fig.add_trace(
    go.Scatter(
        x=highest_prices.index, 
        y=highest_prices.values, 
        mode='lines+markers', 
        name='Highest Price', 
        line=dict(color='green'), 
        marker=dict(color='green', size=8)
    )
)

fig.update_layout(
    title='Google Stock: Highest and Lowest Prices (2004-2020)', 
    xaxis_title='Year', 
    yaxis_title='Stock Price ($)', 
    legend_title='Price Type'
)

st.plotly_chart(fig)

# Image 2
image_path = '/Users/enea/Spiced/Google-Project/streamlit_final/google_acquisitionfx.webp'
image = Image.open(image_path)

st.image(image, caption="Google Acquisitions Visualized 2004-2020", use_container_width=True)


# Google Stock Close Prices on Acquisition Events
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.title("Google Stock Close Prices on Acquisition Events")

acquisitions_merged = pd.DataFrame({
    "Acquisition Events": [
        "Keyhole Acquisition", "YouTube Acquisition", "Android Acquisition",
        "GrandCentral Acquisition", "Motorola Mobility Acquisition", "Waze Acquisition",
        "Nest Labs Acquisition"
    ],
    "Date": pd.to_datetime([
        "2004-10-04", "2006-11-13", "2005-08-17", "2007-07-13", "2012-08-15",
        "2013-06-11", "2014-01-13"
    ]),
    "Close": [
        67.597595, 240.755753, 142.692688, 276.356354, 334.104095,
        440.345337, 562.052063
    ]
})


acquisitions_merged = acquisitions_merged.sort_values(by='Date', ascending=True)


fig = go.Figure()


fig.add_trace(go.Scatter(
    x=acquisitions_merged['Date'], 
    y=acquisitions_merged['Close'], 
    mode='lines+markers', 
    name='Stock Close Price', 
    line=dict(color='blue'),
    marker=dict(color='blue', size=8)
))


for i, txt in enumerate(acquisitions_merged['Acquisition Events']):
    fig.add_annotation(
        x=acquisitions_merged['Date'].iloc[i],
        y=acquisitions_merged['Close'].iloc[i],
        text=txt,
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        font=dict(size=9),
        arrowcolor='blue'
    )


fig.update_layout(
    title='Google Stock Close Prices on Acquisition Events',
    xaxis_title='Acquisition Events Date',
    yaxis_title='Stock Price ($)',
    showlegend=True,
    xaxis_tickformat='%Y-%m-%d',
    xaxis_tickangle=45
)

st.plotly_chart(fig, use_container_width=True)



# Image 3

image_path = '/Users/enea/Spiced/Google-Project/streamlit_final/Major_Events.jpg'
image = Image.open(image_path)

st.image(image, caption="Major Events that Affected Stock Market 2004-2020", use_container_width=True)


# Difference in Close Price: Day of Event vs Day After Event
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


google_stock = pd.DataFrame({
    'Date': ['2004-11-04', '2008-09-16', '2008-11-05', '2009-02-18', 
             '2010-05-07', '2012-11-07', '2015-07-07', '2016-11-10',
             '2018-03-23', '2020-03-10'],
    'Close': [92.442444, 221.686691, 171.291290, 176.731735, 
              246.816818, 333.893890, 550.030029, 780.289978, 
              1026.550049, 1275.170044]
})

google_stock['Date'] = pd.to_datetime(google_stock['Date'])

dates_to_check = [
    '2004-11-04', '2008-09-16', '2008-11-05', '2009-02-18', 
    '2010-05-07', '2012-11-07', '2015-07-07', '2016-11-10',
    '2018-03-23', '2020-03-10'
]
dates_to_check = pd.to_datetime(dates_to_check)

filtered_google_stock = google_stock[google_stock['Date'].isin(dates_to_check)].copy()

index_to_event = {
    0: "George W. Bush Victory Announcement",
    1: "Lehman Brothers Bankruptcy",
    2: "Obama's Victory Announcement",
    3: "American Recovery and Reinvestment Act Signed",
    4: "Flash Crash",
    5: "Obama's Victory Announcement (Re-elected)",
    6: "Start of China’s Stock Market Turmoil",
    7: "U.S. Presidential Election of Donald Trump",
    8: "Trade War and Tariffs",
    9: "Market Crash Due to COVID-19"
}

filtered_google_stock['Event'] = filtered_google_stock.index.map(index_to_event)
filtered_google_stock = filtered_google_stock.rename(columns={'Date': 'Day after the event'})

final_filtered_google_stock = filtered_google_stock[['Event', 'Day after the event', 'Close']]

merged_data = pd.DataFrame({
    'Events': [
        "George W. Bush Victory Announcement", "Lehman Brothers Bankruptcy", 
        "Obama's Victory Announcement", "American Recovery and Reinvestment Act Signed", 
        "Flash Crash", "Obama's Victory Announcement (Re-elected)", 
        "Start of China’s Stock Market Turmoil", "U.S. Presidential Election of Donald Trump", 
        "Trade War and Tariffs", "Market Crash Due to COVID-19"
    ],
    'Date': ['2004-11-03', '2008-09-15', '2008-11-04', '2009-02-17', 
             '2010-05-06', '2012-11-06', '2015-07-06', '2016-11-09',
             '2018-03-22', '2020-03-09'],
    'Close': [92.0, 220.6, 170.2, 175.8, 
              245.8, 332.8, 548.2, 779.1, 
              1025.1, 1274.2]
})

merged_data['Date'] = pd.to_datetime(merged_data['Date'])

final_filtered_google_stock.rename(
    columns={"Event": "Events", "Day after the event": "Day_After_Date", "Close": "Next_Close"}, inplace=True
)

combined_data = pd.merge(
    merged_data, 
    final_filtered_google_stock, 
    on="Events", 
    how="inner"
)

combined_data["Close_Diff"] = combined_data["Next_Close"] - combined_data["Close"]


st.title("Close Price Analysis for Significant Events")
st.write(
    "This application displays the differences in **Close** stock values between the day of the event and the day after the event."
)

st.subheader("Difference in Close Price: Day of Event vs Day After Event")

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(combined_data["Events"], combined_data["Close_Diff"], color="skyblue")
ax.set_xlabel("Difference in Close Price")
ax.set_ylabel("Events")
ax.set_title("Difference in Close Price: Day of Event vs Day After Event")


for i, v in enumerate(combined_data["Close_Diff"]):
    ax.text(v, i, f"{v:.2f}", va="center", fontsize=10)

st.pyplot(fig)



# Google Stock Close Price Differences: Day Before vs Day of Event
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


events_data = {
    "Events": [
        "George W. Bush Victory Announcement", "Lehman Brothers Bankruptcy", "Obama's Victory Announcement",
        "American Recovery and Reinvestment Act Signed", "Flash Crash", "U.S. Credit Rating Downgrade by S&P",
        "Obama's Victory Announcement (Re-elected)", "Start of China’s Stock Market Turmoil", "U.S. Presidential Election of Donald Trump",
        "Trade War and Tariffs", "Market Crash Due to COVID-19"
    ],
    "Date": pd.to_datetime([
        "2004-11-03", "2008-09-15", "2008-11-04", "2009-02-17", "2010-05-06", "2011-08-05", "2012-11-06",
        "2015-07-06", "2016-11-09", "2018-03-22", "2020-03-09"
    ]),
    "Close": [
        95.930931, 217.147141, 183.653656, 171.501495, 249.584579, 289.809814, 341.201202, 
        545.619995, 805.590027, 1053.150024, 1215.790039
    ],
    "Day Before Close": [
        92.442444, 221.686691, 171.291290, 176.731735, 246.816818, 292.558563, 333.893890,
        550.030029, 780.289978, 1026.550049, 1275.170044
    ]
}


events_df = pd.DataFrame(events_data)
events_df = events_df.sort_values(by='Date', ascending=True)


events_df['Close Diff'] = events_df['Close'] - events_df['Day Before Close']


st.subheader("Difference in Close Price:Day Before and Day of Event")

fig, ax = plt.subplots(figsize=(12, 8))


bars = ax.barh(
    events_df["Events"], 
    events_df["Close Diff"], 
    color=["#4caf50" if x >= 0 else "#f44336" for x in events_df["Close Diff"]],
    edgecolor='black'
)


for bar in bars:
    width = bar.get_width()
    color = 'white' if abs(width) > 5 else 'black'
    ax.text(
        width + (1.5 if width > 0 else -1.5),  
        bar.get_y() + bar.get_height() / 2,  
        f"{width:.2f}",
        va='center',
        ha='center' if abs(width) < 2 else ('left' if width > 0 else 'right'),
        fontsize=10,
        color=color
    )


ax.set_xlabel("Difference in Close Price ($)", fontsize=12)
ax.set_ylabel("Events", fontsize=12)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.6)
ax.tick_params(axis='both', which='major', labelsize=10)


st.pyplot(fig)


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

    
    st.sidebar.header("Event Configuration")
    event_date = st.sidebar.date_input("Select Event Date", pd.to_datetime("2020-03-09"))
    event_date = pd.to_datetime(event_date)

  
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


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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

    
    st.subheader("Visualization: Apple Stock Prices")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-', color='blue', label='Closing Price')
    ax.axvline(event_date, color='red', linestyle='--', label=f'Event Date ({event_date.date()})')
    ax.set_title("Apple Stock Prices a Week Before and After Obama's Re-election Announcement", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Closing Price (USD)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

  
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




