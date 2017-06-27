# -*- coding: utf-8 -*-
import os
from subprocess import Popen, PIPE, call

from modules import cbpi, app
from modules.core.hardware import SensorPassive
import json
import os, re, threading, time
from flask import Blueprint, render_template, request
from modules.core.props import Property

import max31865
csPin = 8
misoPin = 9
mosiPin = 10
clkPin = 11
max = max31865.max31865(csPin,misoPin,mosiPin,clkPin)

blueprint = Blueprint('PT100', __name__)

temp = 22

class myThread (threading.Thread):

    value = 0


    def __init__(self, sensor_name):
        threading.Thread.__init__(self)
        self.value = 0
        self.sensor_name = sensor_name
        self.runnig = True

    def shutdown(self):
        pass

    def stop(self):
        self.runnig = False

    def run(self):

        while self.runnig:
            try:
                app.logger.info("READ TEMP")
                ##### read temp from max
                self.value = max.readTemp()
            except:
                pass

            time.sleep(4)



@cbpi.sensor
class PT100(SensorPassive):

    sensor_name = Property.Text("SensorPT100")

    def init(self):

        self.t = myThread(self.sensor_name)

        def shudown():
            shudown.cb.shutdown()
        shudown.cb = self.t

        self.t.start()

    def stop(self):
        try:
            self.t.stop()
        except:
            pass

    def read(self):
        if self.get_config_parameter("unit", "C") == "C":
            self.data_received(round(self.t.value, 2))
        else:
            self.data_received(round(9.0 / 5.0 * self.t.value + 32, 2))

    @classmethod
    def init_global(cls):
        '''
        Called one at the startup for all sensors
        :return: 
        '''


@blueprint.route('/<int:t>', methods=['GET'])
def set_temp(t):
    global temp
    temp = t
    return ('', 204)


@cbpi.initalizer()
def init(cbpi):
    cbpi.app.logger.info("INITIALIZE PT100 MODULE")
    cbpi.app.register_blueprint(blueprint, url_prefix='/api/pt100')
