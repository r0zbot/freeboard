from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/info/cpu')
def cpuInfo():
    out = {}
    out["temperature"] = int(int(open("/sys/class/thermal/thermal_zone0/temp").read())/1000)
    return json.dumps(out)