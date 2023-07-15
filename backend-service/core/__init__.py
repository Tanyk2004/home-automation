from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}}) 
app.config["CORS_HEADERS"] = "Content-Type"

from core import views