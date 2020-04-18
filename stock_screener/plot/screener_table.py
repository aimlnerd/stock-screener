import dash_table

from stock_screener.data.metric import Metric


class Screener:
    def __init__(self, ticker=[], data_api='yahoofinance', metric=['balance_sheet']):
        self.tickers = ticker
        self.data_api = data_api
        self.metric = metric

    def table(self):
        df = Metric(ticker=self.tickers, data_api=self.data_api, metric=self.metric)()
        table = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current=0,
            page_size=10,
            style_cell={'padding': '5px'},
            style_header = {'backgroundColor': 'blue', 'fontWeight': 'bold'}
        )
        return table


if __name__ == '__main__':
    Screener(ticker=['TSLA', 'AAPL'], data_api='yahoofinance', metric=['balance_sheet']).table()