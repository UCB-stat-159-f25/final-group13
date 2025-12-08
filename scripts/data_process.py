import numpy as np
import pandas as pd
import yfinance as yf

def download_sp500(start_date: str = "1990-01-01", end_date: str = None, ticker: str = "^GSPC"):
    df = yf.download(ticker, start=start_date, end=end_date)
    df = df.reset_index().set_index("Date").sort_index()
    return df


def add_technical_indicators(df: pd.DataFrame):
    
    df = df.copy()

    # Simple moving averages
    df["MA10"] = df["Close"].rolling(window=10).mean()
    df["MA50"] = df["Close"].rolling(window=50).mean()

    # Exponential moving averages
    df["EMA10"] = df["Close"].ewm(span=10, adjust=False).mean()
    df["EMA50"] = df["Close"].ewm(span=50, adjust=False).mean()

    # Daily returns & log returns
    df["Return"] = df["Close"].pct_change()
    df["LogReturn"] = np.log1p(df["Return"])

    # Rolling volatility (e.g., 20-day std of returns)
    df["Volatility20"] = df["Return"].rolling(window=20).std()

    # Momentum: price difference vs 10 days ago
    df["Momentum10"] = df["Close"] - df["Close"].shift(10)

    # MACD (12-26 EMA) and signal line (9-period EMA of MACD)
    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = ema12 - ema26
    df["MACD_signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

    return df


def time_series_split(df: pd.DataFrame, train_frac: float = 0.6, val_frac: float = 0.2):
   
    n = len(df)
    train_end = int(n * train_frac)
    val_end = int(n * (train_frac + val_frac))

    df_train = df.iloc[:train_end].copy()
    df_val = df.iloc[train_end:val_end].copy()
    df_test = df.iloc[val_end:].copy()

    return df_train, df_val, df_test