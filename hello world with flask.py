from flask import Flask
import threading, webbrowser

app = Flask(__name__)


@app.route('/name')
def hello():
    return f'Hello, World'


# passing name
@app.route('/<name>')
def hello(name):
    return f'Hello, World {name}'


port = 5000
url = "http://127.0.0.1:{0}".format(port)

threading.Timer(1.25, lambda: webbrowser.open(url)).start()

app.run(port=port, debug=False)
