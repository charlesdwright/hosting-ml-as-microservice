from part3 import get_sentiment
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_whale():
    return 'Whale, Hello there!'

@app.route('/blah')
def blah_yadda():
    return 'Blah blah yadda yadda'

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        input = request.args.get('input')
    else:
        input = request.get_json(force=True)['input']
    if not input:
        return 'No input value found'
    return get_sentiment(input)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='0.0.0.0')
