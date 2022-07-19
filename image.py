from flask import Flask, send_file, request, send_from_directory

app = Flask(__name__)


@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
        filename = 'images/car0.jpg'
    else:
        filename = 'images/car0.jpg'
    return send_file(filename, mimetype='images/car0.jpg')


@app.route('/images/<path>')
def send_report(path):
    return send_from_directory('images', {path})



if __name__ == "__main__":
    app.run()