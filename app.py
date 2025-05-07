import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("vehicles_us.csv")
st.title("Vehicle Listings Explorer")
st.header("Explore Vehicle Price and Mileage Data")

# Show a checkbox to toggle raw data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df.head())

# Histogram of Prices
fig_price = px.histogram(df, x='price', nbins=50, title='Distribution of Vehicle Prices')
st.plotly_chart(fig_price)

# Scatter Plot of Price vs Odometer
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_scatter)