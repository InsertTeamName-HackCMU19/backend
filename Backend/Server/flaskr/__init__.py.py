from flask import Flask, escape, request
import json
from dij_cmu import *

app = Flask(__name__)

@app.route('/test', methods=['post'])
def test():
    data = json.load(request.data)
    start = data['start']
    end = data['end']



    return json.dumps(json.loads(data))

app.run(host='0.0.0.0')