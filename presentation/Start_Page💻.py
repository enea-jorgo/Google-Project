import pandas as pd
import plotly.graph_objects as go
import streamlit as st


from PIL import Image 


image_path = '/Users/enea/Spiced/Google-Project/streamlit_final/google_alphabet.webp'
image = Image.open(image_path)

st.image(image, caption="Google Alphabet Logo", use_container_width=True)

# Displaying information about Alphabet Inc.
st.markdown(
    """
        <strong>Rebranded:</strong> October 2, 2015<br>
        Alphabet Inc. is the parent company of Google and its subsidiaries, 
        managing a wide range of industries like search, advertising, AI, 
        cloud computing, and more. Alphabet’s innovative approach continues 
        to drive advancements in the tech industry globally.
    </p>
    """,
    unsafe_allow_html=True
)

# Image 1

st.title('YouTube Acquisition by Google')

# Load and display the image
image_path = '/Users/enea/Spiced/Google-Project/youtube.png'
image = Image.open(image_path)

# Display the image in Streamlit
st.image(image, caption="Google's Acquisition of YouTube", use_container_width=True)



# What are stocks?
st.title("Understanding Stocks and Their Impact on Company Revenue")

st.markdown(
    """
    ## What Are Stocks?
    Stocks represent ownership in a company. By purchasing stocks, investors own a share of the company 
    and may benefit from **dividends** or **price appreciation**. Companies issue stocks to raise capital 
    for operations or growth.
    """
)

st.markdown(
    """
    ## Do Stocks Impact Company Revenue?
    Stocks **don’t directly affect revenue**, but they can have **indirect effects**, such as:
    
    1. **Raising Capital**: Funds from stock issuance can support expansion and revenue growth.
    2. **Market Sentiment**: A strong stock performance boosts brand value and investor confidence.
    3. **Employee Incentives**: Stock options can improve employee productivity, indirectly increasing revenue.
    """
)