
import yfinance as yf
import streamlit as st
import pandas as pd

# Title of the app
st.write("""
         # Simple Stock Price App
         Shown as stock closing price
         """)

# Input for company name for Google search
company_name = st.text_input("Enter Company Name to Find its Ticker Symbol on Google", "")

# Google search link appears after company name is entered
if company_name:
    query = f"{company_name} stock ticker symbol"
    google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    st.markdown(f"Search for the ticker symbol on [Google]({google_search_url})", unsafe_allow_html=True)

# Instruction for user
st.write("After finding the ticker symbol, enter it below:")

# Input for ticker symbol
ticker_symbol = st.text_input("Enter Ticker Symbol", "")

if ticker_symbol:
    # Fetching the stock data
    tickerData = yf.Ticker(ticker_symbol)
    tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    
    # Displaying charts
    st.line_chart(tickerDF.Close)
    st.line_chart(tickerDF.Volume)



