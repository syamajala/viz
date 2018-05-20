import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Output, Event
from flask import session

from app import app


layout = html.Div([
    html.Form(children=[
        dcc.Input(id='title',
                  placeholder='Title',
                  type='text',
                  value=''),
        dcc.Input(id='pth',
                  placeholder='Path to data',
                  type='text',
                  value=''),
        html.Button('Submit', id='submit_button')])
])


@app.callback(Output('url', 'pathname'),
              events=[Event('submit_button', 'click')],
              state=[State('title', 'value'),
                     State('pth', 'value')])
def submit(title, pth):
    session['configured'] = True
    session['title'] = title
    session['pth'] = pth
    return '/homepage'
