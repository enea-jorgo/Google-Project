import pandas as pd
import plotly.graph_objects as go
import streamlit as st


from PIL import Image 

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

image_path = '/Users/enea/Spiced/Google-Project/streamlit_final/ Major_Events.jpg'
image = Image.open(image_path)

st.image(image, caption="Major Events that Affected Stock Market 2004-2020", use_container_width=True)


# Difference in Close Price: Day of Event vs Day After Event

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


google_stock = pd.DataFrame({
    'Date': ['2004-11-04', '2008-09-16', '2008-11-05', '2009-02-18', 
             '2010-05-07', '2012-11-07', '2015-07-07', '2016-11-10',
             '2018-03-23', '2020-03-10'],
    'Close': [92.442444, 221.686691, 171.291290, 176.731735, 
              246.816818, 333.893890, 550.030029, 780.289978, 
              1026.550049, 1275.170044]
})

google_stock['Date'] = pd.to_datetime(google_stock['Date'])

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

# Create DataFrame for event analysis
merged_data = pd.DataFrame({
    'Events': list(index_to_event.values()),
    'Date': ['2004-11-03', '2008-09-15', '2008-11-04', '2009-02-17', 
             '2010-05-06', '2012-11-06', '2015-07-06', '2016-11-09',
             '2018-03-22', '2020-03-09'],
    'Close': [92.0, 220.6, 170.2, 175.8, 
              245.8, 332.8, 548.2, 779.1, 
              1025.1, 1274.2]
})
merged_data['Date'] = pd.to_datetime(merged_data['Date'])

final_filtered_google_stock = google_stock.copy()
final_filtered_google_stock['Event'] = final_filtered_google_stock.index.map(index_to_event)
final_filtered_google_stock = final_filtered_google_stock.rename(columns={'Date': 'Day_After_Date', 'Close': 'Next_Close'})


combined_data = pd.merge(
    merged_data, 
    final_filtered_google_stock, 
    left_on="Events", 
    right_on="Event", 
    how="inner"
)
combined_data["Close_Diff"] = combined_data["Next_Close"] - combined_data["Close"]

st.title("Google Stock Close Price Analysis for Significant Events")
st.markdown(
    """
    This application provides a detailed visualization of the change in Google stock's **Close** price between the 
    day of significant events and the day after.
    """
)

st.subheader("Price Difference Visualization")
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(
    data=combined_data,
    x="Close_Diff", 
    y="Events", 
    palette="coolwarm", 
    ax=ax
)

ax.set_title("Close Price Difference: Event Day vs. Day After", fontsize=16, weight="bold")
ax.set_xlabel("Difference in Close Price (USD)", fontsize=12)
ax.set_ylabel("Significant Events", fontsize=12)
ax.axvline(0, color="black", linewidth=1, linestyle="--")

for i in range(len(combined_data)):
    ax.text(
        combined_data["Close_Diff"].iloc[i], 
        i, 
        f"{combined_data['Close_Diff'].iloc[i]:.2f} USD", 
        color="black", 
        va="center", 
        fontsize=10
    )

st.pyplot(fig)

st.subheader("Event Data Summary")
st.dataframe(combined_data[['Events', 'Date', 'Close', 'Day_After_Date', 'Next_Close', 'Close_Diff']])



# Google Stock Close Price Differences: Day Before vs Day of Event
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Event data
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


events_df = pd.DataFrame(events_data).sort_values(by='Date', ascending=True)

events_df['Close Diff'] = events_df['Close'] - events_df['Day Before Close']


st.subheader("Difference in Close Price: Day Before and Day of Event")


fig, ax = plt.subplots(figsize=(14, 9))


bars = ax.barh(
    events_df["Events"], 
    events_df["Close Diff"], 
    color=["#4caf50" if x >= 0 else "#f44336" for x in events_df["Close Diff"]],
    edgecolor='black'
)


for bar in bars:
    width = bar.get_width()
    label_x = width + (1.5 if width > 0 else -1.5)  
    color = 'white' if abs(width) > 10 else 'black'
    ax.text(
        label_x, 
        bar.get_y() + bar.get_height() / 2, 
        f"{width:.2f}", 
        va='center', 
        ha='center' if abs(width) < 2 else ('left' if width > 0 else 'right'),
        fontsize=10,
        color=color
    )

ax.set_title("Impact of Significant Events on Google Stock Close Prices", fontsize=16, weight='bold')
ax.set_xlabel("Difference in Close Price ($)", fontsize=13)
ax.set_ylabel("Significant Events", fontsize=13)
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', which='major', labelsize=10)

st.pyplot(fig)