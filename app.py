from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

number = 0
@app.route('/')
def index():
    return 'hello world'

@app.route('/ping')
def ping():
    return 'hello world'

@app.route('/apl')
def apl():
    return jsonify({"hello": "Emerald"})

@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

if (os.getenv('LIVE', 'false') == 'true'):
    if __name__ == '__main__':
        app.run(debug=False, host='0.0.0.0')
else:
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
