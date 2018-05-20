#!/usr/bin/env python
import os
import shutil
import argparse
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import session
from flask_session import Session

from app import app
from pages import homepage, user_config

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return user_config.layout
    if pathname == '/homepage':
        return homepage.layout


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Analysis Tool')
    parser.add_argument('-d', '--debug', dest='debug', action='store_true', default=False)
    parser.add_argument('-p', '--port', dest='port', type=int, default=8050)

    args = parser.parse_args()

    if os.path.exists('flask_session'):
        shutil.rmtree('flask_session')

    sess = Session()
    sess.init_app(app.server)
    app.run_server(debug=args.debug, port=args.port)
