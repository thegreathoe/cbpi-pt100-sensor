# cbpi-pt100-sensor
This is a simple sensor for craftbeerpi which uses a max31865 chip to run pt100 probes.

The code for the request to the max chip is from https://github.com/steve71/MAX31865 so all credit really goes there... i slightly modified the code to work with the new plug-in system on craftbeerpi v3.

I have not yet added the ability to change the pins from the craftbeerpi interface, so it is using:
csPin = 8
misoPin = 9
mosiPin = 10
clkPin = 11

the code has also been altered to use a 430 ohm resistor as the reference... as that it what came on my board for calibration.
