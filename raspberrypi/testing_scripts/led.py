import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker 
    # Print result of connection attempt
    print("Connected with result code {0}".format(str(rc)))
    # Subscribe to topic "deploy/parachute"
    client.subscribe("deploy/parachute")

def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server. 
    print("Message received-> " + str(msg.payload))  # Print a received msg
    if "1" in str(msg.payload):	
        GPIO.output(25, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(25, GPIO.LOW)

client_name = "SpartanFlight"
server_address = "raspberrypi"
mqtt_client = mqtt.Client(client_name)

mqtt_client.connect(server_address, 1883, 60)

mqtt_client.on_connect = on_connect  # Define callback function for successful connection
mqtt_client.on_message = on_message  # Define callback function for receipt of a message

mqtt_client.loop_forever()
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(25,GPIO.OUT)
#GPIO.output(25,GPIO.HIGH)
#time.sleep(1)
#GPIO.output(25,GPIO.LOW)

