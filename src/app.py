import flask
import logging
import logging.handlers
from json import loads
from dicttoxml import dicttoxml
from flask import request, jsonify, send_from_directory

from estimator import estimator

app = flask.Flask(__name__)

# logging.basicConfig(filename="access.log", level=logging.)
handler = logging.handlers.RotatingFileHandler(
    "access.log", maxBytes=1024*1024)
logging.getLogger("werkzeug").setLevel(logging.DEBUG)
logging.getLogger("werkzeug").addHandler(handler)
app.logger.setLevel(logging.WARNING)
app.logger.addHandler(handler)


@app.route("/", methods=["GET"])
def index():
    return "<h2>Covid 19 Estimator</h2>"


@app.route("/api/v1/on-covid-19", methods=["POST"])
@app.route("/api/v1/on-covid-19/json", methods=["POST"])
def make_estimate():
    input_data = request.json
    return jsonify(estimator(input_data))


@app.route("/api/v1/on-covid-19/xml", methods=["POST"])
def make_estimate_json():
    input_data = request.json
    return dicttoxml(estimator(input_data))


@app.route("/api/v1/on-covid-19/logs", methods=["GET"])
def get_logs():
    return send_from_directory("./", "access.log")


app.run()
