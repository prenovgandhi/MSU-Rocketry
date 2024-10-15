



  GNU nano 7.2                                                                                           sensor.py                                                                                                    
import time
import board
import serial
import csv
import threading

import os
import ssl
import socketpool
import paho.mqtt.client as mqtt

from mpl3115a2 import adafruit_mpl3115a2
from mpu6050 import adafruit_mpu6050
import adafruit_gps


class Sensor:
    """
        Interface with Adafruit MPU6050, MPL3115A2, and GPS Breakout using their respective libraries.
    """

    def __init__(self):

        self.filename = "data.csv"
        fields = ["X Acc.", "Y Acc.", "Temperature", "Altitude"] #added altitude 4/3

        # open file for writing
        fp = open(self.filename, "w")
        csvwriter = csv.writer(fp, delimiter=',')
        csvwriter.writerow(fields)
        fp.close()
        # initialize mqtt connection
        client_name = "SpartanFlight"
        server_address = "raspberrypi"
        self.mqtt_client = mqtt.Client(client_name)

        self.mqtt_client.connect(server_address, 1883, 60)

        i2c = board.I2C()  # uses board.SCL and board.SDA

        # Initialize the MPL3115A2.
        self.mpl = adafruit_mpl3115a2.MPL3115A2(i2c)
        self.mpl.sealevel_pressure = 1022.5  # Look up the pressure at sealevel at the specific time/location in hectopascals

        # Initialize the MPU6050
        self.mpu = adafruit_mpu6050.MPU6050(i2c)

        # Initialize the gps
        uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
        self.gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")         
        self.gps.send_command(b"PMTK220,1000")


    def start_sensors(self):
        """
        Start collecting sensor data.
        """
        # Main loop runs forever printing the location, etc. every second.
        last_print = time.monotonic()
        # while True:
        try:
            # publish altimeter data

