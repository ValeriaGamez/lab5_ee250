# from flask import Flask, request, jsonify
import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)

# TODO: create a route for the delay endpoint.
#      The route should accept POST requests and return the same message that was sent to it.

@app.route('/delay', methods=['POST'])
def add_message_route():
    message = flask.request.data
    #res = flask.jsonify(message)
    return message
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
