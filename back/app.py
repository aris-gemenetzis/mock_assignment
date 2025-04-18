from flask import Flask
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"
