from flask import Flask
from flask_executor import Executor

app = Flask(__name__)
executor = Executor(app)
app.config['EXECUTOR_TYPE'] = 'thread'

from app import lights, routes, errors
