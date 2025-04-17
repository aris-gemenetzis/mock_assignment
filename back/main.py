# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import uvicorn
import json

"""
from flask import Flask
from flask_cors import CORS, cross_origin
from fastapi import FastAPI


import requests
from bs4 import BeautifulSoup
"""

"""
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('greeting.html', say=request.form['say'], to=request.form['to'])


if __name__ == "__main__":
    app.run()
"""

"""
base_url = 'http://localhost:3000'

# payload = {'company': company, 'revenue': revenue, 'costs': costs}


def get_tax_info():
    # url = f"{base_url}/test/{name}"
    url = f"{base_url}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # tax_data = response.json()
        # print(tax_data)
        # tax_data = response.json()
        print(type(soup))
        print("data retrieved")
        print(response.content)
    else:
        print(f"failed to retrieve data {response.status_code}")


name = 'deloitte'
# get_tax_info(name)
get_tax_info()
"""

"""
app = FastAPI()

# base_url = 'http://localhost:3000/handler'
base_url = 'http://localhost:3000/'


@app.get("/")
async def root():
    return {"message": "Hello World"}
"""
"""
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
"""

# working fastapi
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)  # 8000


"""
app = Flask(__name__)
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/form/<company>')
def get_info(company):
    print(company)
    return f"<h1>{company}</h1>"
"""

"""
x = requests.get('http://localhost:3000/', params = {"company": "deloitte"})
print(x.status_code)

url = 'http://localhost:3000/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print(type(soup))
    print(soup.findAll)
"""
"""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


with app.test_request_context('/', method='POST'):
    assert request.method == 'POST'
"""
"""
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.post('/createpost')
def create_post():
    return {'message': 'post'}
"""
