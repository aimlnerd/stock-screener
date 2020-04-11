import yfinance as yf


class YahooFinance:
    def __init__(self):
        pass

    def pe(self):
        pass

    def ebit_by_ev(self):
        pass

    def  net_debt(self):
        pass

    def history(self, ticker, period="max"):
        yf_ticker = yf.Ticker(ticker)
        df_history = yf_ticker.history(period=period)
        return df_history

    def historical_closing_price(self, ticker):
        df_history = self.history(ticker=ticker, period="max").reset_index()
        return df_history[['Date', 'Close']]


if __name__ == '__main__':
    yahfin = YahooFinance()
    yahfin.historical_closing_price(ticker='TSLA')
