#!/bin/bash
export FLASK_APP=api.py
export FLASK_DEBUG=1
# tirar isso quando for rodar for real
python3 -m flask run --host=0.0.0.0