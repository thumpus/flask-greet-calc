# Put your app in here.
from flask import Flask
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_nums():
    """add a and b"""
    a = int(request.args.get["a"])
    b = int(request.args.get["b"])
    result = add(a, b)
    return str(result)

@app.route('/sub')
def subtract_nums():
    """subtract b from a"""
    a = int(request.args.get["a"])
    b = int(request.args.get["b"])
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def multiply_nums():
    """multiple a and b"""
    a = int(request.args.get["a"])
    b = int(request.args.get["b"])
    result = mult(a, b)
    return str(result)

@app.route('/div')
def divide_nums():
    """divide a into b"""
    a = int(request.args.get["a"])
    b = int(request.args.get["b"])
    result = div(a, b)
    return str(result)

