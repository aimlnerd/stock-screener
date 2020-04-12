import dash_table
import pandas as pd
import plotly.express as px



class Screener:
    def __init__(self, tickers=[]):
        self.tickers = tickers

    def table(self):
        df = pd.DataFrame({'a': [1, 3], 'b': [9, 39]})
        table = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'))
        return table
