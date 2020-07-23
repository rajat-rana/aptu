from flask import Flask
from applications import home
#app = Flask(__name__)

import os


# server = Flask(__name__)
app = home.create_app(Flask(__name__))
server = app.server
# @server.route('/')
if __name__ == '__main__':
    app.run_server(debug=True)
