import logging
import sys

import flask
from flask import Flask, request
from flask_cors import CORS
from src.github_license_graph import GithubLicenseGraph

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('UTF8')

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
app = Flask(__name__)
CORS(app)

global github_license_graph


@app.before_first_request
def load_model():
    app.github_license_graph = GithubLicenseGraph.load("data/github_license_graph.pkl")
    app.logger.info("Git License Graph got loaded successfully!")


@app.route('/')
def heart_beat():
    return flask.jsonify({"status": "ok"})


@app.route('/api/v1/schemas/license_scoring', methods=['POST'])
def predict_and_score():
    input_json = request.get_json()
    app.logger.info("Analyzing the given EPV")
    m = app.github_license_graph.get_license_recommendation_for_license_list(input_json.get("license_list"))
    response = {"stack_level_license": m}
    return flask.jsonify(response)


if __name__ == "__main__":
    app.run()
