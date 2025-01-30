import streamlit as st

st.markdown(
    """
    <h1 style='text-align: center; font-size: 36px; color: black;'>
    Fun Facts⬇️
    </h1>
    """,
    unsafe_allow_html=True,
)


image_path = "/Users/enea/Spiced/Google-Project/streamlit_final/fun_facts.jpg"


st.image(image_path, caption="Fun Facts About Google and Apple Investments", use_container_width=True)