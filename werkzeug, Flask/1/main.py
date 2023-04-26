from flask import Flask, request
from werkzeug.exceptions import NotFound

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        return 'Hello World'
    return f'Hello {request.method} request!'   

@app.route('/404/')
def not_found():
    raise NotFound


app.run('localhost', 8080, debug=True)