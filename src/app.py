import flask
import logging
import logging.handlers
from json import loads
from dicttoxml import dicttoxml
from flask import request, jsonify, send_from_directory, make_response, render_template, url_for
from gevent.pywsgi import WSGIServer

from estimator import estimator

app = flask.Flask(__name__)

# create a file to store weblogs
# log = open("access.log", 'w')
# log.seek(0)
# log.truncate()
# log.write("Web Application Log\n")
# log.close()

# log_handler = logging.handlers.RotatingFileHandler(
#     "access.log", maxBytes=1000000, backupCount=1)

# formatter = logging.Formatter(
#     "%(levelname)s - %(message)s"
# )
# log_handler.setFormatter(formatter)
# app.logger.setLevel(logging.DEBUG)  
# app.logger.addHandler(log_handler)

logging.basicConfig(filename="access.log", level=logging.DEBUG, format="%(message)s")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/v1/on-covid-19/", methods=["POST"])
@app.route("/api/v1/on-covid-19/json/", methods=["POST"])
def make_estimate():
    input_data = request.json
    logging.debug("App running on PORT: 5000")
    return jsonify(estimator(input_data))


@app.route("/api/v1/on-covid-19/xml/", methods=["POST"])
def make_estimate_json():
    input_data = request.json
    response = make_response(
        dicttoxml(estimator(input_data), custom_root="response", attr_type=False))
    response.mimetype = "application/xml"
    logging.debug("App running on PORT: 5000")
    return response


@app.route("/api/v1/on-covid-19/logs/", methods=["GET"])
def get_logs():
    logs = open("access.log", "r")
    response = make_response(logs.read())
    response.mimetype = "text/plain"
    logging.debug("App running on PORT: 5000")
    return response


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    logging.debug("App running on PORT: 5000")
    http_server.serve_forever()
