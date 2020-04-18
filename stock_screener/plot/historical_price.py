import pandas as pd
import plotly.express as px

from stock_screener.data.metric import Metric


class Historical:
    def __init__(self, ticker, data_api='yahoofinance'):
        self.ticker = ticker
        self.metric = Metric(ticker=ticker, data_api='yahoofinance')

    def plot_closing_price(self):
        df = self.metric.closing_price()

        fig = px.line(df, x='Date', y='Close', color = "Ticker", hover_name = "Ticker", labels = {'y': 'Closing Price'},
                      title=f"Historical stock price of {str(self.ticker)}")

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(count=3, label="3y", step="year", stepmode="backward"),
                    dict(count=5, label="5y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        return fig


if __name__ == '__main__':
    hist = Historical(ticker=['TSLA', '^GSPC'])
    hist.plot_closing_price()
