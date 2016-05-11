#!/usr/bin/env python

'''
A command line tool to access the Raspberry Pi GPIO pins.
Usage:
> sudo python gpio.py mode [BOARD|BCM] [on|off|read] [PIN_NUMBERs]
Example:
$ sudo python gpio.py mode BCM on   22 23 24 25 
$ sudo python gpio.py mode BCM off  22 23 24 25 
$ sudo python gpio.py read BCM 22 23 24 25
'''

import RPi.GPIO as GPIO

def initial_GPIO_mode(mode):
    '''
    Initial GPIO settings
    Args:
        mode: [BOARD|BCM] GPIO mode of Raspberry Pi
    '''
    GPIO.setmode (mode)
    GPIO.setwarnings(False)

def setup_GPIO_as_output_pin(GPIO_PINs):
    '''
    Set GPIO_PINs as output pins
    Args:
        GPIO_Pins: List of the GPIO pins
    '''
    for pin in GPIO_PINs:
        GPIO.setup (int(pin), GPIO.OUT)

def set_pins(GPIO_PINs, value):
    '''
    Set value to GPIO_PINs 
    Args:
        GPIO_Pins: List of the GPIO pins
        value: [GPIO.HIGH|GPIO.LOW]
    '''
    for pin in GPIO_PINs:
        GPIO.output (int(pin), value) 

def read_pins(GPIO_PINs):
    '''
    Read value from GPIO_PINs and print 
    Args:
        GPIO_Pins: List of the GPIO pins
    '''
    for pin in GPIO_PINs:
        value = GPIO.input (int(pin)) 
        print ("Pin %s is %d" % (pin, value))

# If the input parameter not correct. Print the usage and exit
def usage():
    '''
    If the input parameter not correct. Print the usage and exit.
    '''
    print (__doc__)
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

