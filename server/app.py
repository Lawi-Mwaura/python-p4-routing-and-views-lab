#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_route():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count_route(parameter):
    return str (parameter)

@app.route('/count/<int:parameter>')
def count_range_10(parameter):
    count = '\n'.join(str(i) for i in range(parameter))
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
