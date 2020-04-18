import ast
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from plot.historical_price import Historical
from plot.screener_table import Screener


app = dash.Dash()
app.layout = html.Div([html.H1(children='Stock Screener'),
                       html.Div(children='A tool for stock picking.'),
                       html.Label('Input Ticker '),
                       dcc.Input(id='input_ticker',
                                 placeholder='Enter list of Ticker',
                                 type='text',
                                 value="['TSLA', 'APL']"),
                       dcc.Graph(id='historical_price'),
                       html.Div(children=[html.H4(children='Top value stocks'),
                       Screener(ticker=['TSLA', 'AAPL'], data_api='yahoofinance', metric=['balance_sheet']).table()
                       ])
                       ])


@app.callback(
    Output(component_id='historical_price', component_property='figure'),
    [Input(component_id='input_ticker', component_property='value')]
)
def input_to_hist_price(ticker):
    lst_ticker = ast.literal_eval(ticker)
    return Historical(ticker=lst_ticker, data_api='yahoofinance').plot_closing_price()


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
