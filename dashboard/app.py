import dash
import dash_core_components as dcc
import dash_html_components as html

from plot.historical_price import Historical

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=Historical(tickers=['TSLA', '^GSPC']).closing_price())
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter