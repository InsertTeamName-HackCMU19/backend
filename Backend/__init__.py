from flask import Flask, escape, request
import json
from dij_cmu import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app, send_wildcard=True)


@app.route('/navigation', methods=['post'])
def test():
    data = json.loads(request.data)
    print(data)
    start = data['start']
    end = data['end']
    path = findPath(start, end)
    print(path)
    return json.dumps(path)

app.run(host='0.0.0.0')