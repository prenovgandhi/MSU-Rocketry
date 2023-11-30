import time
import board
import serial
import csv

import os
import ssl
import socketpool
import paho.mqtt.client as mqtt

from mpl3115a2 import adafruit_mpl3115a2
from mpu6050 import adafruit_mpu6050
import adafruit_gps

client_name = "SpartanFlight"
server_address = "raspberrypi"
mqtt_client = mqtt.Client(client_name)

mqtt_client.connect(server_address, 1883, 60)

############################################

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the MPL3115A2.
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
sensor.sealevel_pressure = 1022.5  # Look up the pressure at sealevel at the specific time/location in hectopascals

# Initialize the MPU6050
mpu = adafruit_mpu6050.MPU6050(i2c)

# Initialize the gps
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
# Main loop runs forever printing the location, etc. every second.
last_print = time.monotonic()

filename = "acceleration.csv"
fields = ["X", "Y"]

fp = open(filename, "w")

csvwriter = csv.writer(fp)

csvwriter.writerow(fields)

fp.close()

while True:
    try:
        fp = open(filename, "a")

        csvwriter = csv.writer(fp)
        
        mqtt_client.publish("mpl3115a2/altitude", str( sensor.altitude ))
        mqtt_client.publish("mpl3115a2/temperature", str( sensor.temperature ))
    
        mqtt_client.publish("mpu6050/AcX", str( mpu.acceleration[0] ))
        mqtt_client.publish("mpu6050/AcY", str( mpu.acceleration[1] ))

        print(mpu.acceleration)

        acc = (round(mpu.acceleration[0], 6), round(mpu.acceleration[1], 6))

        #csvwriter.writerow(mpu.acceleration)
        csvwriter.writerow(acc)

        # Make sure to call gps.update() every loop iteration and at least twice
        # as fast as data comes from the GPS unit (usually every second).
        # This returns a bool that's true if it parsed new data (you can ignore it
        # though if you don't care and instead look at the has_fix property).
        gps.update()
        mqtt_client.publish("gps/updating", "Updating...")
        # Every second print out current location details if there's a fix.
        current = time.monotonic()
        if current - last_print >= 0.1:
            last_print = current
            if not gps.has_fix:
                # Try again if we don't have a fix yet.
                mqtt_client.publish("gps/status", "Waiting for fix...")
                mqtt_client.publish("gps/inuse", str( gps.satellites ))
                continue
        
            # We have a fix! (gps.has_fix is true)
            mqtt_client.publish("gps/status", str(gps.has_fix))
            mqtt_client.publish("gps/inuse", str( gps.satellites ))
            mqtt_client.publish("gps/latitude", str( gps.latitude ))
            mqtt_client.publish("gps/longitude", str( gps.longitude ))
            mqtt_client.publish("gps/altitude", str( gps.altitude_m ))

        time.sleep(0.001)

        fp.close()

    except:
        continue

