# -*- coding: utf-8 -*-
from modules import cbpi
from modules.core.hardware import SensorPassive
from modules.core.props import Property
import max31865

@cbpi.sensor
class PT100(SensorPassive):
    # CONFIG PARAMETER & PROPERTIES
    csPin  = Property.Select("csPin", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], description="GPIO Pin connected to the CS Pin of the MAX31865 - For MISO, MOSI, CLK no choice by default it's PIN 9, 10, 11")
    RefRest = Property.Number("Reference Resistor", configurable=True, description="Reference Resistor of the MAX31865 board (it's written on the resistor: 400 or 430,....)")
    misoPin = 9
    mosiPin = 10
    clkPin = 11
    ConfigText = Property.Select("Conversion Mode & Wires", options=["[0xB2] - 3 Wires Manual","[0xD2] - 3 Wires Auto","[0xA2] - 2 or 4 Wires Manual","[0xC2] - 2 or 4 Wires Auto"], description="Choose beetween 2, 3 or 4 wire PT100 & the Conversion mode at 60 Hz beetween Manual or Continuous Auto")

		#
		# Config Register
		# ---------------
		# bit 7: Vbias -> 1 (ON), 0 (OFF)
		# bit 6: Conversion Mode -> 0 (MANUAL), 1 (AUTO) !!don't change the noch fequency 60Hz when auto
		# bit5: 1-shot ->1 (ON)
		# bit4: 3-wire select -> 1 (3 wires config), 0 (2 or 4 wires)
		# bits 3-2: fault detection cycle -> 0 (none)
		# bit 1: fault status clear -> 1 (clear any fault)
		# bit 0: 50/60 Hz filter select -> 0 (60Hz - Faster converson), 1 (50Hz)
		#
		# 0b10110010 = 0xB2     (Manual conversion, 3 wires at 60Hz)
		# 0b10100010 = 0xA2     (Manual conversion, 2 or 4 wires at 60Hz)
		# 0b11010010 = 0xD2     (Continuous auto conversion, 3 wires at 60 Hz) 
		# 0b11000010 = 0xC2     (Continuous auto conversion, 2 or 4 wires at 60 Hz) 
		#

      

    def init(self):

        # INIT SENSOR
        self.ConfigReg = self.ConfigText[1:5]
        self.max = max31865.max31865(int(self.csPin),int(self.misoPin), int(self.mosiPin), int(self.clkPin), int(self.RefRest), int(self.ConfigReg,16))

    def read(self):

        # READ SENSOR
        if self.get_config_parameter("unit", "C") == "C":
            self.data_received(round(self.max.readTemp(), 2))
        else:
            self.data_received(round(9.0 / 5.0 * self.max.readTemp() + 32, 2))


