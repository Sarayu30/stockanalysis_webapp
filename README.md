 

# Stock Price App using Streamlit

This Streamlit web application fetches and displays historical stock closing prices and allows for interactive analysis of stock data. Users can specify a ticker symbol, select a date range, compare multiple stocks, and visualize stock performance using interactive charts.

## Features

- **Input Parameters:**
  - Users can enter a ticker symbol (e.g., AAPL) to fetch historical data from Yahoo Finance.
  - They can select a start and end date to define the range of data to be displayed.

- **Interactive Date Range Selection:**
  - Sidebar allows users to dynamically adjust the date range to visualize specific periods of interest.

- **Additional Stock Metrics:**
  - Calculates and displays the 50-day moving average (50 MA) alongside the closing price for the selected stock.

- **Comparative Analysis:**
  - Users can compare the closing prices of multiple stocks or indices by entering ticker symbols separated by commas.

- **Error Handling and Notifications:**
  - Provides error messages if an invalid ticker symbol is entered or if there are issues fetching data from Yahoo Finance.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sarayu30/stockanalysis_webapp
   cd stockanalysis_webapp
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

4. **Access the app:**
   Open your web browser and go to `http://localhost:8501`.

## Dependencies

- yfinance
- streamlit
- pandas
- plotly

## Usage

- Enter a ticker symbol and select a date range in the sidebar.
- View historical closing prices and volume for the selected stock.
- Interact with the plotly chart to zoom in or hover over data points for more details.
- Adjust date ranges dynamically using the sidebar inputs.
- Compare stock prices by entering multiple ticker symbols in the Comparative Analysis section.

## Support

For any issues or questions, please [open an issue](https://github.com/Sarayu30/stockanalysis_webapp/issues) on GitHub.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 
