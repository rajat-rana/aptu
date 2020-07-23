from flask import Flask
from applications import home
#app = Flask(__name__)

import os


server = Flask(__name__)
app = home.create_app(server)
@server.route('/')
def hello():
    app.run_server(debug=True)
