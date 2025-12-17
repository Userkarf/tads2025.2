import pandas as pd
import yfinance as yf

def download_data(
    ticker: str = 'SNFF11.SA'
) -> pd.DataFrame:
    
    """
    Download historical market data for a given ticker using yfinance.

    Parameters
    ----------
    ticker : str, optional
        The ticker symbol to download data for (default is 'SNFF11.SA').

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the historical price data with the date as index.
    """
    
    result = yf.download(
        ticker,
        period='max'
    ).reset_index()

    return result