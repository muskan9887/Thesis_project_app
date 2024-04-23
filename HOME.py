import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Real Estate Insights: Forecasting & Recommendations"
)

# Sidebar
st.sidebar.success("Select")

# Title
st.markdown("<h1 style='text-align: center;'>Smart Real Estate Analytics: Integrating Housing Forecasting and "
            "Recommendation System</h1>", unsafe_allow_html=True)

# Image
st.image("datasets/home.jpeg", width=700, caption="Image Caption")
