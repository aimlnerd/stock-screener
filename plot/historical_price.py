import pandas as pd
import plotly.express as px

from data.yahoofinance import YahooFinance

yahfin = YahooFinance()
df = yahfin.historical_closing_price(ticker='TSLA')


class Historical:
    def __init__(self, tickers):
        self.tickers = tickers
        self.yahfin = YahooFinance()

    def closing_price(self):
        df = pd.DataFrame()
        for ticker in self.tickers:
            df_ticker = yahfin.historical_closing_price(ticker=ticker)
            df_ticker['Ticker'] = ticker
            df = pd.concat([df, df_ticker], axis=0)

        fig = px.line(df, x='Date', y='Close', color = "Ticker", hover_name = "Ticker",
                      title=f"Historical stock price of {str(self.tickers)}")

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
    hist = Historical(tickers=['TSLA', '^GSPC'])
    hist.closing_price()
