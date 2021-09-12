from flask import Flask, jsonify, request
from onyx_taxi_db import Driver, Client, Order
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, world</p>"


@app.route("/drivers", methods=["POST"])
def post_driver():
    content = request.get_json()
    return jsonify(content)


if __name__ == "__main__":
    app.run()
