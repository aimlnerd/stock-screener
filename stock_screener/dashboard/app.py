import ast
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from stock_screener.plot.historical_price import Historical
from stock_screener.plot.screener_table import Screener

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = False
app.title = "Stock Screener"

app.layout = html.Div([html.H1(children='Stock Screener'),
                       html.H3(children='A tool for stock picking'),
                       html.Label('Input Ticker '),
                       dcc.Input(id='input-ticker',
                                 placeholder='Enter list of Ticker',
                                 type='text',
                                 value="['TSLA','SABR']"),
                       html.H2(children='Historical Price'),
                       dcc.Graph(id='historical-price'),
                       html.H2(children='Top value stocks'),
                       html.Div(children=Screener(ticker=['AAPL'], data_api='yahoofinance',
                                                  metric=['balance_sheet']).table(),
                                id='screener-table-container')

                       ])

######### Callbacks ##################

#Update 'historical-price' graph
@app.callback(
    Output(component_id='historical-price', component_property='figure'),
    [Input(component_id='input-ticker', component_property='value')]
)
def input_to_hist_price(ticker):
    lst_ticker = ast.literal_eval(ticker)
    return Historical(ticker=lst_ticker, data_api='yahoofinance').plot_closing_price()

#Update screener-table
@app.callback(
    Output(component_id='screener-table-container', component_property='children'),
    [Input(component_id='input-ticker', component_property='value')]
)
def input_to_screener_table(ticker):
    lst_ticker = ast.literal_eval(ticker)
    return Screener(ticker=lst_ticker, data_api='yahoofinance', metric=['balance_sheet', 'info']).table()


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
