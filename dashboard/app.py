import pandas as pd
import ast
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from plot.historical_price import Historical

df = pd.DataFrame({'a': [1,3], 'b': [9, 39] })


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])




app = dash.Dash()
app.layout = html.Div([html.H1(children='Stock Screener'),
                       html.Div(children='A tool for stock picking.'),
                       html.Label('Input Ticker'),
                       dcc.Input(id='input_ticker',
                           placeholder='Enter list of Ticker',
                           type='text',
                           value="['TSLA', 'APL']"),
                       dcc.Graph(id='historical_price'),
                       html.Div(children=[
                            html.H4(children='US Agriculture Exports (2011)'),
                            generate_table(df)])
                       ])


@app.callback(
    Output(component_id='historical_price', component_property='figure'),
    [Input(component_id='input_ticker', component_property='value')]
)
def input_to_hist_price(ticker):
    lst_ticker = ast.literal_eval(ticker)
    return Historical(ticker=lst_ticker).plot_closing_price()


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
