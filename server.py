# coding: utf-8
from flask import Flask
from flask import jsonify
from flask import request
import requests
from flask_cors import CORS
import os


app = Flask(__name__)

# add cors
CORS(app)  



@app.route('/')
def index():
    api_url = os.environ.get('ARIA2_RPC_URL')
    if api_url:
        return jsonify(ok=True)
    else:
        return jsonify(ok=False)


@app.route('/jsonrpc', methods=['post', 'put', 'delete'])
def jsonrpc():
    data = request.get_json()
    r = requests.post('http://10.10.10.10:6801/jsonrpc', json=data)
    response = jsonify(**r.json())
    return response, r.status_code


if __name__ == '__main__':
    app.run(port=6800, debug=True)
