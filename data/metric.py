import pandas as pd
from data_api.yahoofinance import YahooFinance


class Metric:
    def __init__(self, ticker, data_api='yahoofinance'):
        self.ticker = ticker
        if data_api=='yahoofinance':
            self.data_api = YahooFinance

    def price_to_earning(self, ticker):
        pass

    def ebit_by_ev(self):
        pass

    def  net_debt(self):
        pass

    def closing_price(self):
        """

        :param ticker: list of ticker
        :return: dataframe with closing price
        """
        if isinstance(self.ticker, (list)):
            df = pd.DataFrame()
            for ticker in self.ticker:
                df_ticker = self.data_api(ticker=ticker).price(period="max")
                df_ticker = df_ticker[['Date', 'Close']]
                df_ticker['Ticker'] = ticker
                df = pd.concat([df, df_ticker], axis=0)

        return df


if __name__ == '__main__':
    metric = Metric(ticker=['TSLA', '^GSPC'], data_api='yahoofinance')
    #metric.price_to_earning()
    metric.closing_price()
