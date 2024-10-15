Last login: Tue Oct 15 19:34:34 on ttys000
chancesmith@Chances-MacBook-Pro ~ % ssh MSURocketry@raspberrypi.local
MSURocketry@raspberrypi.local's password: 
Linux raspberrypi 6.1.0-rpi4-rpi-v8 #1 SMP PREEMPT Debian 1:6.1.54-1+rpt2 (2023-10-05) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Oct  9 01:25:28 2024 from fe80::428:e568:c46f:3e%wlan0
MSURocketry@raspberrypi:~ $ ls
adafruit_bus_device  env                       sensor.py
adafruit_gps.py      mpl3115a2                 sensor.py.save
adafruit_register    mpl_mpu_gps_code.py       sensor_test.py
air.py               mpl_mpu_gps_code.py.save  state.py
COM6                 mpu6050                   testing_scripts
data.csv             __pycache__
Desktop              sensor_data
MSURocketry@raspberrypi:~ $ sudo nano air.pu
MSURocketry@raspberrypi:~ $ sudo nano air.py
MSURocketry@raspberrypi:~ $ sudo nano sensor.py
MSURocketry@raspberrypi:~ $ sudo nano sensor.py











































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

^G Help          ^O Write Out     ^W Where Is      ^K Cut           ^T Execute       ^C Location      M-U Undo         M-A Set Mark     M-] To Bracket   M-Q Previous     ^B Back          ^◂ Prev Word
^X Exit          ^R Read File     ^\ Replace       ^U Paste         ^J Justify       ^/ Go To Line    M-E Redo         M-6 Copy         ^Q Where Was     M-W Next         ^F Forward       ^▸ Next Word
