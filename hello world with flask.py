from flask import Flask, request
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)


@app.route('/name')
def hello():
    return f'Hello, World'


@app.route('/aa')
def hello():
    return {
        'Name': "geek",
        "Age": "22",
        "Date": 'aaaaa',
        "programming": "python"
    }


# getting response
@app.route('/bb', methods=["POST"])
def hi():
    todo_data = request.data
    print(todo_data)
    return todo_data


# passing name
@app.route('/<name>')
def hello(name):
    return f'Hello, World {name}'


if __name__ == "__main__":
    app.run(debug=True)
