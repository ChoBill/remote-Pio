# Remote-Pio
Remote-Pio Provide a web API and a web frontend to access the Raspberry Pis' GPO pins.

# Quick Start
> Requirements:
> * Flask

Run the test server:
```
python gpioapi.py
```

Browse the website(Default port of the test server is 5000):
```
(http://raspberrypi:5000/)
```

Use the web API:
```
(http://raspberrypi:5000/gpio/read/)
(http://raspberrypi:5000/gpio/on/22/)
(http://raspberrypi:5000/gpio/off/23/)
```

# Change GPIO Settings:
In gpioapi.py:
```
# Set RPi.GPIO mode: BCM/BOARD
GPIO_Mode="BCM"
# Set GPIO Pin number
GPIO_Pins="22,23,24,25"
```

# License
Remote-Pio is releaseed under the [BSD 2-Clause License] (https://opensource.org/licenses/bsd-license). 
