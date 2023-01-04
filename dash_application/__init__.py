import logging
from flask import Flask
from dash import Dash

format = "%(asctime)s: %(message)s"
date_format = "%d-%b-%y %H:%M:%S"
logging.basicConfig(format=format, level=logging.INFO, datefmt=date_format, 
                    handlers=[logging.FileHandler(filename="logs/info.txt", encoding='utf-8', mode='a+')])

server = Flask(__name__,)

server.config['DEBUG'] = True

app = Dash(__name__, server=server, url_base_pathname='/dash/')
app.config['suppress_callback_exceptions'] = True

from dash_application import views

