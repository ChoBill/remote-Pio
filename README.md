# Remote-Pio
Remote-Pio Provide a web API and a web frontend to access the Raspberry Pis' GPO pins.

![remote-Pio demo](https://cloud.githubusercontent.com/assets/18475968/17454271/f173c7aa-5bc1-11e6-874a-c4f5e629dfc6.png)

# Quick Start
> Requirements:
> * Flask

Run the test server:
```
python gpioapi.py
```

Browse the web UI(Default port of the test server is 5000):
```
(http://raspberrypi:5000/)
```

Access the web API:
```
GET  /gpio/      - Return data {pin nums: pin value}
GET  /gpio/{pin} - Return data {pin num: pin value}
POST /gpio/{pin} - Post data {cmd: on|off}
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
