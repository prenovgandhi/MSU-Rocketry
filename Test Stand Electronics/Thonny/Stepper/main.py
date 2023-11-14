from umqtt.simple import MQTTClient
from stepper import Stepper
from machine import Pin
from time import sleep

# mqtt client setup
CLIENT_NAME = 'StepperESP'
BROKER_ADDR = '192.168.0.100'
keepalive_topic = CLIENT_NAME.encode() + b'/keepalive/1' #topic is "StepperESP/keepalive/1"
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=600)
mqttc.connect()

# Stepper setup
s1 = Stepper(26,27,steps_per_rev=200,speed_sps=1600)
rest = Pin(25, Pin.OUT)
steptopic = b'/stepper/1'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    

def take_step(topic, msg):
    if is_number(msg.decode()):
        s1.target_deg(float(msg.decode()))
        print(float(msg.decode()))
    if msg.decode() == 'stoprest':
        rest.value(1)
    if msg.decode() == 'startrest':
        rest.value(0)
    if msg.decode() == 'forwards':
        s1.free_run(1)
    if msg.decode() == 'backwards':
        s1.free_run(-1)
    if msg.decode() == 'stop':
        s1.free_run(0)

        
# mqtt subscription
mqttc.set_callback(take_step)
mqttc.subscribe(steptopic)


while True:
    mqttc.check_msg()
    mqttc.publish(keepalive_topic, str("yeehaw!").encode())
    
    
    sleep(0.25)

