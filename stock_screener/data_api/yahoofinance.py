import yfinance as yf
import pandas as pd


class YahooFinance:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

    def _history(self, period="max"):
        df_history = self.ticker.history(period=period)
        return df_history

    def price(self, period="max"):
        df_history = self._history(period=period).reset_index()
        return df_history[['Date', 'Open', 'High', 'Low', 'Close']]

    def quarterly_balance_sheet(self):
        df = self.ticker.quarterly_balance_sheet
        return df

    def quarterly_financials(self):
        df = self.ticker.quarterly_financials
        return df

    def info(self, metric=None):
        df = pd.DataFrame.from_dict(self.ticker.info, orient='index').T
        df = df.rename(columns={'symbol': 'ticker'})
        return df


if __name__ == '__main__':
    yahfin_ticker = YahooFinance(ticker='TSLA')
    yahfin_ticker.info()
    ev = yahfin_ticker.info["enterpriseValue"]
    ebit = yahfin_ticker.financials.iloc[7, 0]

    df_price = yahfin_ticker.price()
    df_bs_ratios = yahfin_ticker.quarterly_balance_sheet()
    df_quarterly_financials= yahfin_ticker.quarterly_financials()