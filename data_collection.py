"""
Data Collection Module
Author: [Brant Anderson]
Description: This module is responsible for collecting historical and real-time stock price data from Yahoo Finance.
Date: [10/21/23]
first edition
"""

import yfinance as yf
import pandas as pd
import time

def download_historical_data(stock_symbol, start_date, end_date):
    """
    Download historical stock price data for a given stock symbol within a specified date range.

    Args:
        stock_symbol (str): The stock symbol of the company (e.g., 'AAPL' for Apple Inc.).
        start_date (str): The start date in the format 'YYYY-MM-DD'.
        end_date (str): The end date in the format 'YYYY-MM-DD'.

    Returns:
        pd.DataFrame: A DataFrame containing historical stock price data, including Date, Open, High, Low, Close, and Volume.
    """
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data

def update_real_time_data(stock_symbol, data, max_length, update_interval=60, max_updates=5):
    """
    Update the existing dataset with real-time stock price data for a given stock symbol.

    Args:
        stock_symbol (str): The stock symbol of the company (e.g., 'AAPL' for Apple Inc.).
        data (pd.DataFrame): The existing DataFrame containing historical data.
        max_length (int): The maximum length of the dataset to manage memory usage.
        update_interval (int): The time interval in seconds for updating real-time data.
        max_updates (int): Maximum number of updates (optional).

    Returns:
        pd.DataFrame: The updated DataFrame with real-time data appended.
    """
    updates = 0

    while True:
        real_time_data = yf.download(stock_symbol, period="1d", interval="1m")
        data = data.append(real_time_data)
        
        # Manage dataset length to avoid excessive memory usage
        if len(data) > max_length:
            data = data.iloc[-max_length:]
        
        updates += 1

        if max_updates is not None and updates >= max_updates:
            break

        time.sleep(update_interval)

    return data

