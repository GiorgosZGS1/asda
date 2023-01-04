from flask import render_template, request 

from dash_application.dashboard import app

@app.server.route('/dash')
def dashboard():
    return app.index()

@app.server.route('/hello')
def hello():
    return render_template('index.html')
