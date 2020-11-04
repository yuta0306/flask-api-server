from flask import Flask
from flask import jsonify, render_template

import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    obj = {
        'text': 'Hello, {}'.format(name),
    }
    output = json.dumps(obj)

    return jsonify(output)


if __name__ == "__main__":
    app = app.run(debug=True)