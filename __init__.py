# -*- coding: utf-8 -*-
from modules import cbpi
from modules.core.hardware import SensorPassive
from modules.core.props import Property
import max31865

@cbpi.sensor
class PT100(SensorPassive):
    # CONFIG PARAMETER	
    csPin  = Property.Select("csPin", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
    misoPin = 9
    mosiPin = 10
    clkPin = 11
    
    def init(self):

        # INIT SENSOR
        self.max = max31865.max31865(int(self.csPin),int(self.misoPin), int(self.mosiPin), int(self.clkPin))

    def read(self):

        # READ SENSOR
        if self.get_config_parameter("unit", "C") == "C":
            self.data_received(round(self.max.readTemp(), 2))
        else:
            self.data_received(round(9.0 / 5.0 * self.max.readTemp() + 32, 2))


