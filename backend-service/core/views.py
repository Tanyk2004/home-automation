from flask import jsonify, request
from core import app
from core.RelayControl import RelayStateControl, Relay
from core.db.model import dbManager
from flask_cors import cross_origin

from flask import Response

@app.before_request
def before_request():
  headers = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type' }
  if request.method == 'OPTIONS' or request.method == 'options':
    return jsonify(headers), 200
    
def __init__(self):
    print("relay state control created")
    db = dbManager()
    if ( not db.checkIfRelayExists(4)):
        db.addRelay(4, False)


@app.route("/", methods=["GET"])
@cross_origin()
def index():
    return jsonify({"message": "Home Automation API is Running!"}), 200


# TODO - if you want to embed a video stream on to the page as well try this https://chat.openai.com/share/e2f71f0e-06d5-45ca-8aa1-6070cd6fbe8f
# TODO - add schema validation for requests

# This function modifies the relay state

@app.route("/relay/update", methods=["PUT"])
@cross_origin()
def relay():
    data = request.get_json()
    rsc = RelayStateControl()
    if rsc.updateRelay(data["relayNumber"], data["relayState"]):
        return jsonify({"updatedRelayState": (data["relayState"]), "success" : True}), 200
    else:
        return jsonify({"updatedRelayState": (data["relayState"]), "success" : False}), 201


# @app.route("/relay/all", methods=["OPTIONS"])
# def getRelayPreFlight():
#     print("running options")
#     if request.method == "OPTIONS":
#         # Set the necessary headers for the preflight response
#         response_headers = {
#             "Access-Control-Allow-Origin": "*",  # or set your specific allowed origins
#             "Access-Control-Allow-Methods": "GET, PUT, OPTIONS",
#             "Access-Control-Allow-Headers": "Content-Type",
#             "Acess-Control-Allow-Credentials":"true"
#         }
#         return "", 200, response_headers

# This function returns the relay state
@app.route("/relay/all", methods=["GET"])
@cross_origin()
def getRelay():
    # return jsonify({"relayState": [], "success" : True}), 200
    rsc = RelayStateControl()
    relayList : list = rsc.getAllRelays()
    return jsonify({"relayState": relayList, "success" : True}), 200

# This function creates a new relay and adds it to the database
@app.route("/relay/create", methods=["POST"])
def addRelay():
    data = request.get_json()
    rsc = RelayStateControl()
    success = rsc.addRelay(data["relayNumber"], data["relayState"])
    if success:
        return jsonify({"message" : "Relay successfully created" , "success" : True}), 201
    else:
        return jsonify({"message" : "Relay already exists" , "success" : False}), 200

@app.route("/relay/delete", methods=["PUT"])
def deleteRelay():
    data = request.get_json()
    rsc = RelayStateControl()
    removedRelay = rsc.removeRelay(data["relayNumber"])
    
    if removedRelay == None:
        return jsonify({"message" : "Relay doesn't exist" , "success" : False}), 200
    return jsonify({"message" : "Relay Deleted successfully" , "success" : True}), 200




