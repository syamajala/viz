import dash
from flask import Flask

server = Flask(__name__, template_folder='pages')
app = dash.Dash(__name__, server=server)

server.config['SESSION_TYPE'] = 'filesystem'
server.config['SECRET_KEY'] = 'mysecretkey'
app.config.suppress_callback_exceptions = True
