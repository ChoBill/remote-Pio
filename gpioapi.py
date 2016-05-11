#!/usr/bin/env python
# -*- coding: utf-8 -*
'''
Provide a web api to access Raspberry Pi GPIO pins.
'''

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Set RPi.GPIO mode: BCM/BOARD
GPIO_Mode="BCM"
# Set GPIO Pin number
GPIO_Pins="22,23,24,25"

def prep_cmd(cmd, pin):
    '''
    Prepare gpio.py command and parameter
    Args:
        cmd : [on|off|read]
        pin : pin numbers seperated by ",". eg: 22,23
    Returns:
        CMD: retrun the command string
    '''
    import os
    dir_name = os.path.dirname(os.path.realpath(__file__))
    Script = dir_name + "/gpio.py"
    SetMode=GPIO_Mode
    CMD = ["sudo", Script, "mode", SetMode, cmd]
    CMD.extend (pin.split(","))
    return CMD

def run_cmd(CMD):
    '''
    Run gpio.py command
    Args:
       CMD: Command string
    Retruns:
        stdout of the command
    '''
    import sys, subprocess
    out = subprocess.check_output(CMD)
    lines = out.decode('utf-8').splitlines()
    return lines

def parse_response(resp):
    '''
    Parse the gpio.py stdout to {pin_number: pin_value}
    Args:
        resp: stdout of the command response
    Retruns:
        pin_status: a dictionary of the {pin_num: pin_value} pair
    '''
    pin_status = {}
    for line in resp:
        w1, pin_num, w3, pin_value = line.split(' ') 
        pin_status.update ({pin_num: pin_value})
    return pin_status

@app.route("/")
def remote_gpo():
    '''
    Render a web UI to control the gpio
    '''
    return render_template('remote_gpo.html')

@app.route("/gpio/<pin>/", methods=['GET', 'POST'])
def gpio(pin):
    '''
    API to access the gpio pins by gpio.py command tool
    GET  /gpio/{pin} - Retrun data {pin_num: pin_value}
    POST /gpio/{pin} - Post {cmd: [on|off]}
    '''
    if request.method == 'GET':
        cmd = "read"
    elif request.method == 'POST':
        cmd = request.form['cmd']
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

@app.route("/gpio/", methods=['GET'])
def gpio_read():
    '''
    API to read the gpio pins
    GET /gpio/ - Retrun data {pin_num: pin_value}
    '''
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
