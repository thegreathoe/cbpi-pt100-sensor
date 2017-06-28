# cbpi-pt100-sensor
PT100 probes using a max31865 chip.  for wiring go to https://github.com/thegreathoe/cbpi-pt100-sensor/

Using a max31865 board like: https://learn.adafruit.com/adafruit-max31865-rtd-pt100-amplifier/

**
on your pi use the following GPIO pins.
csPin = 8  *this one can be any GPIO you want, if using multiple probes you change this on each one, but keep the other 3 pins the same*
misoPin = 9
mosiPin = 10
clkPin = 11
**

The code for the request to the max chip is from https://github.com/steve71/MAX31865 so all credit really goes there... i slightly modified the code to work with the new plug-in system on craftbeerpi v3.  the code has also been altered to use a 430 ohm resistor as the reference... as that it what came on my board for calibration.

Manuel neatened up my origional code and added the ability to select the cs pin.... so the rest of the credit goes there... I'm just kind of peieced it all together.

