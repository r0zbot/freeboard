import requests
from flask import Flask
from flask import request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/info')
def sysinfo():
    meminfo = {}
    out2 = ""
    for line in open("/proc/meminfo").readlines():
        key,value = line.split(":");
        meminfo[key.strip()] = value.replace("kB","").strip()
    out = {
        "ip": {
            "client": request.remote_addr,
            "server": requests.get('http://wtfismyip.com/text').content.decode("utf-8").strip()
        },
        "temperature": int(int(open("/sys/class/thermal/thermal_zone0/temp").read())/1000),
        "memory": {
            "ram": {
                "free": meminfo["MemAvailable"],
                "total": meminfo["MemTotal"] 
            },
            "swap": {
                "free": meminfo["SwapFree"],
                "total": meminfo["SwapTotal"]
            }
        }
    }
    return json.dumps(out)