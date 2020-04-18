from datetime import datetime as dt
from datetime import timedelta
import dash
import dash_html_components as html
import dash_core_components as dcc
import re

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.DatePickerRange(
        start_date_placeholder_text="Start Date",
        end_date_placeholder_text="End Date",
        id='my-date-picker-range',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2017, 9, 19),
        initial_visible_month=dt.now().date(),
        display_format='D MMMM YYYY',
        start_date=dt.now().date() - timedelta(weeks=4),
        end_date=dt.now().date()
    ),
    html.Div(id='output-container-date-picker-range')
])