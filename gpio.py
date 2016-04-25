#!/usr/bin/env python

# Usage:
# sudo python gpio.py mode [BOARD|BCM] [on|off|read] [PIN_NUMBERs]
# Example:
# sudo python gpio.py mode BCM on   22 23 24 25 
# sudo python gpio.py mode BCM off  22 23 24 25 
# sudo python gpio.py read BCM 22 23 24 25

import RPi.GPIO as GPIO

# Initial GPIO settings
def initial_GPIO_mode(mode):
    GPIO.setmode (mode)
    GPIO.setwarnings(False)

# Set GPIO_PINs to output pins
def setup_GPIO_as_output_pin(GPIO_PINs):
    for pin in GPIO_PINs:
        GPIO.setup (int(pin), GPIO.OUT)

# Set value to GPIO_PINs 
def set_pins(GPIO_PINs, value):
    for pin in GPIO_PINs:
        GPIO.output (int(pin), value) 

# Read value from GPIO_PINs and print 
def read_pins(GPIO_PINs):
    for pin in GPIO_PINs:
        value = GPIO.input (int(pin)) 
        print ("Pin %s is %d" % (pin, value))

# If the input parameter not correct. Print the usage and exit
def usage():
    print "Usage:"
    print "> sudo python gpio.py mode [BOARD|BCM] [on|off|read] [PIN_NUMBERs]"
    print "Example:"
    print "> sudo python gpio.py mode BCM on 22 23 24 25"
    exit()

if __name__ == "__main__":
    import sys

    # Parsing the command input parameter
    if len (sys.argv) > 4:
        if ( sys.argv[1] != "mode"):
            usage()
        # Get the second argument as mode
        mode = sys.argv[2]
        # Initial GPIO
        if (mode == "BOARD"):
            initial_GPIO_mode(GPIO.BOARD)
        elif (mode == "BCM"):
            initial_GPIO_mode(GPIO.BCM)
        else:
            usage()

        # Get the third argument as cmd
        cmd = sys.argv[3]

        # Get the following arguments
        pin_list = []
        for arg_index in range (4, len (sys.argv)):
            pin_list.append( sys.argv[arg_index] )

        # setup GPIO pins
        setup_GPIO_as_output_pin (pin_list)

        # parsing cmd arguments
        if (cmd == 'on'):
            set_pins (pin_list, GPIO.HIGH)
        elif (cmd == 'off'):
            set_pins (pin_list, GPIO.LOW)
        elif (cmd == 'read'):
            read_pins (pin_list)
        else:
            usage()
    else:
        usage()

