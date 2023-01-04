from dash import html, dcc
import pandas as pd
import plotly.express as px

from dash_application import app

from dash import dcc, html
from dash.dependencies import Input, Output



# App layout
app.layout = html.Div(children=[
    html.H1(children='CTS PROJECT'),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''')])