from flask import jsonify, request
from core import app
from core.RelayControl import RelayStateControl, Relay

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Home Automation API is Running!"}), 200

# TODO - if you want to embed a video stream on to the page as well try this https://chat.openai.com/share/e2f71f0e-06d5-45ca-8aa1-6070cd6fbe8f
# TODO - create a get based api endpoint for getting the relay state
# we want to use this to update the relay state
# TODO - Now connect this to the GPIO code in a different class based on relay ID's
# This function modifies the relay state
# TODO  - make an endpoint that returns all the relay ids that are stored in the relay state control array


@app.route('/relay', methods=['PUT'])
def relay():
    data = request.get_json()
    headers= request.headers
    print(data['relayNumber'])
    rsc = RelayStateControl()
    rsc.addRelay(4, False)
    r = rsc.getRelay(data['relayNumber'])
    print(data['relayState'])
    r.setRelayState(data['relayState'])
    return jsonify({"updatedRelayState" : (data["relayState"])}), 200

# This function returns the relay state
@app.route('/relay', methods=['GET'])
def getRelay():
    rsc = RelayStateControl()
    rsc.addRelay(4, False)
    r = rsc.getRelayIndex(0)
    return jsonify({"relayState" : r.getRelayState()}), 200