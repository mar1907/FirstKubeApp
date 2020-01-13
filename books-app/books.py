import requests
import pprint

from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = "AIzaSyAFGTZA7vCirJuaekd-9uh4Rm1Ne9wKR1o"
APPLICATION_NAME = "sm-sd2/1.0"

URL = "https://www.googleapis.com/books/v1/volumes"

@app.route('/books/<string:title>', methods=['GET'])
def get_books(title):
    PARAMS = {'key': API_KEY, 'q': 'intitle:'+title, 'maxResults': '20'}
    r = requests.get(url = URL, params = PARAMS)

    data = r.json()

    volumeInfo = []
    for d in data['items']:
        volumeInfo.append(d['volumeInfo'])
    keys = ['authors', 'title']

    for i in range(len(volumeInfo)):
        volumeInfo[i] = { k: (volumeInfo[i][k] if k in volumeInfo[i] else "") for k in keys }

    return jsonify(volumeInfo)

if __name__ == '__main__':
    app.run(debug=True, port=5035, host="0.0.0.0")
