import logging
import sys

import flask
from flask import Flask, request
from flask_cors import CORS

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('UTF8')

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
app = Flask(__name__)
CORS(app)


@app.route('/')
def heart_beat():
    return flask.jsonify({"status": "ok"})


@app.route('/api/v1/schemas/license_scoring', methods=['POST'])
def predict_and_score():
    input_json = request.get_json()
    app.logger.info("Analyzing the given EPV")

    return flask.jsonify(input_json)


if __name__ == "__main__":
    app.run()
