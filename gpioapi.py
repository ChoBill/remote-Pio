#!/usr/bin/env python

from flask import Flask
from flask import jsonify

app = Flask(__name__)

# Set RPi.GPIO mode: BCM/BOARD
GPIO_Mode="BCM"
# Set GPIO Pin number
GPIO_Pins="22,23,24,25"

def prep_cmd(cmd, pin):
    # Set command parameters
    import os
    dir_name = os.path.dirname(os.path.realpath(__file__))
    Script = dir_name + "/gpio.py"
    SetMode=GPIO_Mode
    # Prepare gpio.py command & parameters
    CMD = ["sudo", Script, "mode", SetMode, cmd]
    CMD.extend (pin.split(","))
    return CMD

def run_cmd(CMD):
    import sys, subprocess
    out = subprocess.check_output(CMD)
    lines = out.decode(sys.stdout.encoding).splitlines()
    return lines

def parse_response(resp):
    pin_status = {}
    for line in resp:
        w1, pin_num, w3, pin_value = line.split(' ') 
        pin_status.update ({pin_num: pin_value})
    return pin_status

# Provide webapi to access the gpio pins
# Example:
#   http://127.0.0.1/gpio/on/22,23/
@app.route("/gpio/<cmd>/<pin>/")
def gpio(cmd, pin):
    # Prepare the command & arguments
    CMD = prep_cmd(cmd, pin)
    # Run the gpio.py command
    resp_lines = run_cmd (CMD)
    # Prepare response for json response
    response = {}
    # No news is good news
    if ( len(resp_lines) == 0 ):
        response.update ({"status": "OK"})
    # If response the "Usage", then the CMD is not correct
    elif ( resp_lines[0].find("Usage") == 0 ):
        response.update ({"status": "Error"})
    # Read result of the pin(s)
    else:
        response.update ({"status": "OK"})
        response.update ({"data": parse_response(resp_lines) })
    return jsonify(**response)

@app.route("/gpio/read/")
def gpio_read():
    # Prepare the command & arguments
    CMD = prep_cmd("read", GPIO_Pins)
    # Run the gpio.py command
    resp_lines = run_cmd (CMD)
    # Prepare response for json response
    response = {}
    response.update ({"status": "OK"})
    response.update ({"data": parse_response(resp_lines) })
    return jsonify(**response)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
