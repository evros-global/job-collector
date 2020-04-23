from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
indeed url: <input></input> <br>
number of pages url: <input></input> <br>
<input type=submit></input>
"""
