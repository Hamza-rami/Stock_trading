import yfinance as yf
import pandas as pd
import datetime as dt
import os

# Get absolute path of the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

stocknames = ['AAPL', 'MSFT', 'TSLA', 'GC=F', 'SPY']
startdate = '2025-01-01'
enddate = dt.datetime.now().date()

def run_update():
    # Fetch and save individual stocks
    for stock in stocknames:
        df = yf.download(stock, start=startdate, end=enddate, interval='1d', auto_adjust=False, actions=False)
        df.to_csv(os.path.join(script_dir, f'{stock}.csv'))
    
    # Create combined portfolio
    combined_df = pd.DataFrame()
    for stock in stocknames:
        df = pd.read_csv(os.path.join(script_dir, f'{stock}.csv'), index_col='Date', parse_dates=True)
        if 'Adj Close' in df.columns:
            temp = df[['Adj Close']].rename(columns={'Adj Close': stock})
            combined_df = temp if combined_df.empty else combined_df.join(temp)
    
    combined_df.dropna().to_csv(os.path.join(script_dir, 'combined_portfolio.csv'))

if __name__ == "__main__":
    run_update()