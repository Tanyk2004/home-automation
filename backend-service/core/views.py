from flask import jsonify, request
from core import app
import json

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Home Automation API is Running!"}), 200


# TODO - create a get based api endpoint for getting the relay state

# we want to use this to update the relay state
# TODO - Now connect this to the GPIO code in a different class based on relay ID's
@app.route('/relay', methods=['PUT'])
def relay():
    data = request.get_json()
    headers= request.headers
    print(data)
    print(headers)
    return jsonify({"updatedRelayState" : (data["relayState"] + 1)}), 200