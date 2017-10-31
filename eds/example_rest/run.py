#!flask/bin/python
from flask import Flask, jsonify
from base64 import b64decode
import requests
from requests.auth import HTTPDigestAuth
import json
app = Flask(__name__)





@app.route('/eds/MemsIPE/MemsData', methods=['GET'])
def get_tasks():
    url = "http://localhost:8000/onem2m/MemsIPE/sensor_data/x/"

    mems_data = requests.get(url)
    print "code:" + str(mems_data.status_code)
    print mems_data.text

    return json.dumps(myResponse.text)
    print myResponse

if __name__ == '__main__':
    app.run(debug=True,port=8080)