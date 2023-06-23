from flask import Flask
from flask_cors import CORS
from core.RelayControl import RelayStateControl, Relay

app = Flask(__name__)
CORS(app)


from core import views