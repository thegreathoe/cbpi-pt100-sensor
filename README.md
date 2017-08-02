# cbpi-pt100-sensor
PT100 probes using a max31865 chip.  for wiring go to https://github.com/thegreathoe/cbpi-pt100-sensor/ updated 8/2/17

You may need to clear your browser cache if updating from a previous version!!!!!

You can now select the conversion mode and number of wires on your probe in software.  You will need to select a setting to get the probe working after an update.

If you are updating from a previous version, you will need to set the reference resistors on the craftbeerpi hardware page!  My chip uses a 430 ohm resistor 

Using a max31865 board like: https://learn.adafruit.com/adafruit-max31865-rtd-pt100-amplifier/

**
on your pi use the following GPIO pins.
csPin = 8  *this one can be any GPIO you want, if using multiple probes you change this on each one, but keep the other 3 pins the same*
misoPin = 9
mosiPin = 10
clkPin = 11
**

The code for the request to the max chip is from https://github.com/steve71/MAX31865 so all credit really goes there... i slightly modified the code to work with the new plug-in system on craftbeerpi v3.  you can now change the ref resistor from teh hardware page of the craftbeerpi

Manuel neatened up my origional code and added the ability to select the cs pin.... so the rest of the credit goes there... I just kind of peieced it all together.

8/2/17:: Pascal has been working on a pretty nice update which allows you to select the number of wires used on your probe in software... you still need to sever traces or solder jumpers on the board!  He has also been added as a contributer

7/2/17:: Verified with Pascal Fouchy that it is working on multiple sensors at once, and i have added the ability to change the reference resistor value from the craftbeerpi hardware page
