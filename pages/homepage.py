import dash_html_components as html

from app import app


def build_layout(session):
    print session
    return html.Div([html.H3('TODO')])
