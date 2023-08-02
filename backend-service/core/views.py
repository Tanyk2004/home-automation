from flask import jsonify, request
from core import app
from core.RelayControl import RelayStateControl
from flask_cors import cross_origin
import os
import wave, pyaudio
import simpleaudio as sa

@app.before_request
def before_request():
  headers = { 'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS', 
              'Access-Control-Allow-Headers': 'Content-Type' }
  
  if request.method == 'OPTIONS' or request.method == 'options':
    return jsonify(headers), 200
    



@app.route("/", methods=["GET"])
@cross_origin()
def index():
    return jsonify({"message": "Home Automation API is Running!"}), 200

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

@app.route("/audio/play", methods = ["POST"])
def playAudio():
    data = request
    audio_file = data.files.get('audio')
    audio_file.save("audio.wav")
    
    play_audio("audio.wav")

    if data is None:
        return jsonify({"message" : "Sound upload failed", "success" : False}), 400
    return jsonify({"message" : "Sound uploaded successfully", "success" : True}), 200

def play_audio(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()


