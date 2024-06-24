import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page Title and Description
st.set_page_config(page_title='Stock Price App', layout='wide', initial_sidebar_state='expanded')
st.title("Enhanced Stock Price App")
st.write("""
Welcome to the Enhanced Stock Price App! 
This app fetches and displays historical stock closing price and volume.
""")

# Sidebar - Input Ticker Symbol and Date Range
st.sidebar.header('Input Parameters')
tickerSymbol = st.sidebar.text_input("Enter Ticker Symbol (e.g., AAPL)", 'GOOGL')
start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2010-01-01'))
end_date = st.sidebar.date_input("End Date", pd.to_datetime('2020-12-31'))

# Function to Fetch and Clean Data with caching using st.cache_data
@st.cache_data  # Cache data to speed up app
def load_data(symbol, start, end):
    tickerData = yf.Ticker(symbol)
    df = tickerData.history(period='1d', start=start, end=end)
    
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    # Ensure index is datetime and timezone-aware (assuming UTC)
    df.index = pd.to_datetime(df.index)  # Convert index to datetime if not already
    if not df.index.tzinfo:  # Check if index is timezone-aware
        df.index = df.index.tz_localize('UTC')  # Localize to UTC if not already
    
    return df

# Load Data
df = load_data(tickerSymbol, start_date, end_date)

# Display Cleaned Historical Data
st.subheader('Cleaned Historical Data')
st.write(df)

# Plot Closing Price and Volume using Plotly for interactive visualization
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Closing Price'))
fig.update_layout(title='Stock Closing Price', xaxis_title='Date', yaxis_title='Price ($)')
st.plotly_chart(fig)

# Sidebar - Interactive Date Range Selection
st.sidebar.markdown('## Interactive Date Range Selection')
start_date_selection = st.sidebar.date_input("Start Date", min_value=df.index.min().to_pydatetime(), max_value=df.index.max().to_pydatetime())
end_date_selection = st.sidebar.date_input("End Date", min_value=df.index.min().to_pydatetime(), max_value=df.index.max().to_pydatetime())

# Convert date inputs to datetime.datetime objects and localize to UTC timezone
if start_date_selection and end_date_selection:
    start_date_selection = pd.Timestamp(start_date_selection).tz_localize('UTC')
    end_date_selection = pd.Timestamp(end_date_selection).tz_localize('UTC')

    # Update data based on selected date range (convert to timezone-aware UTC)
    filtered_data = df.loc[start_date_selection:end_date_selection]

    # Additional Stock Metrics - Calculate and display 50-day moving average
    st.sidebar.markdown('## Additional Stock Metrics')
    df['50_MA'] = df['Close'].rolling(window=50).mean()
    st.line_chart(df[['Close', '50_MA']])

    # Comparative Analysis - Enable users to compare the performance of multiple stocks or indices
    st.sidebar.markdown('## Comparative Analysis')
    tickerSymbols_comparison = st.sidebar.text_input("Enter Ticker Symbols for Comparison (comma-separated)", 'AAPL, MSFT')
    symbols_list = [symbol.strip() for symbol in tickerSymbols_comparison.split(',')]

    if symbols_list:
        for symbol in symbols_list:
            try:
                tickerData_comp = yf.Ticker(symbol)
                df_comp = tickerData_comp.history(period='1d', start=start_date, end=end_date)
                fig.add_trace(go.Scatter(x=df_comp.index, y=df_comp['Close'], mode='lines', name=f'{symbol} Closing Price'))
            except ValueError:
                st.warning(f"Invalid ticker symbol: {symbol}")

        fig.update_layout(title='Stock Closing Price Comparison', xaxis_title='Date', yaxis_title='Price ($)')
        st.plotly_chart(fig)

    # Error Handling and Notifications
    st.sidebar.markdown('## Error Handling and Notifications')
    try:
        tickerData_error = yf.Ticker(tickerSymbol)
        df_error = tickerData_error.history(period='1d', start=start_date, end=end_date)
    except ValueError as e:
        st.error(f"Error fetching data: {str(e)}")

    # Help Section
    st.sidebar.markdown('## Help Section')
    st.sidebar.markdown('This app fetches and displays historical stock data using Yahoo Finance.')
    st.sidebar.markdown('[GitHub Repository](https://github.com/Sarayu30/stockanalysis_webapp)')

    # Footer
    st.sidebar.markdown('---')
    st.sidebar.markdown('Created with ❤️ by Sarayu Krishna')

    # Display the app
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable deprecated warning
    st.pyplot()  # Display all Matplotlib charts at once
