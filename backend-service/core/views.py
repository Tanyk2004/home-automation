from core import app
import json

@app.route('/')
def index():
    return json.loads('{"message": "Hello World!"}')