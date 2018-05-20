import dash

app = dash.Dash()

server = app.server
server.config['SESSION_TYPE'] = 'filesystem'
server.config['SECRET_KEY'] = 'mysecretkey'
app.config.suppress_callback_exceptions = True
