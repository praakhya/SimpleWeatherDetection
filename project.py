#! /usr/bin/python3
from datetime import datetime as dt
import serial, Adafruit_DHT
from Adafruit_IO import Client, Data, Feed, RequestError
from sense_hat import SenseHat
import subprocess
import os
import sys

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 21
sense = SenseHat()
ser = serial.Serial('/dev/ttyUSB1')
data = []
for index in range(0, 10):
    datum = ser.read();
    data.append(datum)
pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
temperature = sense.get_temperature()
pressure = sense.get_pressure()
humidity = sense.get_humidity()
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
ss=0.2
sense.show_message("IP %s" % subprocess.check_output(['hostname', '-I']), scroll_speed=ss, text_colour=[100,100,100])
sense.show_message("PM2.5 %.2f" % pmtwofive, scroll_speed=ss, text_colour=[100,100,100])
sense.show_message("PM10  %.2f" % pmten, scroll_speed=ss, text_colour=[255,0,0])
sense.show_message("Pres %.2f" % pressure, scroll_speed=ss, text_colour=[0,255,0])
sense.show_message("Hum %.2f" % humidity, scroll_speed=ss, text_colour=[255,255,0])
sense.show_message("Temp %.2f" % temperature, scroll_speed=ss, text_colour=[0,0,255])
datafile=os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),"data.txt")
f = open(datafile, "a+")
f.write("%s,%.2f,%.2f,%.2f,%.2f,%.2f\n" % (dt.now().strftime("%d/%m/%Y %H:%M:%S"), pmtwofive, pmten, pressure, temperature, humidity))
f.close()
