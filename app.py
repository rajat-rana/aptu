from flask import Flask
from applications import home
from applications import app2

#app = Flask(__name__)

import os


server = Flask(__name__)
app = home.create_app(server, '/app/')
app_2 = app2.create_app(server, '/app2/')


@server.route('/')
def hello():
    return " Hello World. change routes  to '/app' and 'app2' to go to apps"


# @server.route('/app2')
# def hello_app():
#     return "Hello App"
