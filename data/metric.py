import logging
import pandas as pd
from data_api.yahoofinance import YahooFinance

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


class Metric:
    def __init__(self, ticker, data_api='yahoofinance'):
        self.ticker = ticker
        if data_api=='yahoofinance':
            self.data_api = YahooFinance

    def latest_qtr_balance_sheet(self, ticker):
        df = self.data_api(ticker=ticker).quarterly_balance_sheet()
        latest_qtr = max(df.columns)
        return df[latest_qtr]

    def bs_ratios(self):
        if isinstance(self.ticker, (list)):
            df_master = pd.DataFrame()
            for ticker in self.ticker:
                df = pd.DataFrame(data={'ticker': ticker})
                df_bs = self.latest_qtr_balance_sheet(ticker)

                latest_qtr_total_assets = self._get_metric(df=df_bs, metric='Total Assets')
                latest_qtr_total_liabilities = self._get_metric(df=df_bs, metric='Total Liab')
                df['latest_qtr_total_solvency_ratio'] = self._solvency_ratio(assets=latest_qtr_total_assets, liabilities=latest_qtr_total_liabilities)

                latest_qtr_total_cash = self._get_metric(df=df_bs, metric='Cash')
                latest_qtr_total_short_long_term_debt = self._get_metric(df=df_bs, metric='Short Long Term Debt')
                df['latest_qtr_net_debt'] = self._net_debt(debt=latest_qtr_total_short_long_term_debt, cash=latest_qtr_total_cash)
                df_master = pd.concat([df_master, df], axis=0)
        return df_master

    def _get_metric(self, df, metric):
        return float(df.loc[metric])

    def _net_debt(self, debt, cash):
        return debt-cash


    def _solvency_ratio(self, assets, liabilities):
        return assets/liabilities

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
    metric = Metric(ticker=['TSLA', 'SABR'], data_api='yahoofinance')
    metric.bs_ratios()
    metric.closing_price()
