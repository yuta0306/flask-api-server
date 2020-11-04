from flask import Flask
from flask import jsonify, render_template

import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    obj = {
        'text': 'Hello, {}'.format(name),
    }
    output = json.dumps(obj)

    return jsonify(output)


if __name__ == "__main__":
    app = app.run(debug=True)