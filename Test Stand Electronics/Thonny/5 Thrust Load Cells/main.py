from machine import Pin
from hx711 import HX711
from umqtt.simple import MQTTClient
import time  # Don't forget to import the time module
import utime

CLIENT_NAME = 'loadcellesp_02'
BROKER_ADDR = '192.168.0.100'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
print('about to connect to wifi')
mqttc.connect()
print('connected')

pin_OUT1 = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)
pin_OUT2 = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
pin_OUT3 = Pin(21, Pin.IN, pull=Pin.PULL_DOWN) # I2C
pin_OUT4 = Pin(26, Pin.IN, pull=Pin.PULL_DOWN) # A2C
pin_OUT5 = Pin(27, Pin.IN, pull=Pin.PULL_DOWN) # A2C - Soder...

pin_SCK1 = Pin(4, Pin.OUT)
pin_SCK2 = Pin(22, Pin.OUT)
pin_SCK3 = Pin(23, Pin.OUT) 
pin_SCK4 = Pin(32, Pin.OUT)
pin_SCK5 = Pin(33, Pin.OUT)

# Use the GPIO constructor
hx1 = HX711(pin_SCK1, pin_OUT1, gain = 64)
hx2 = HX711(pin_SCK2, pin_OUT2, gain = 64)
hx3 = HX711(pin_SCK3, pin_OUT3, gain = 64)
hx4 = HX711(pin_SCK4, pin_OUT4, gain = 64)
hx5 = HX711(pin_SCK5, pin_OUT5, gain = 64)

while True:
    value1 = hx1.get_value()
    value2 = hx2.get_value()
    value3 = hx3.get_value()
    value4 = hx4.get_value()
    value5 = hx5.get_value()
    valueavg = (value1+value2+value3+value4+value5)/5
    #mqttc.publish( b'/loadcell2/force1/', str(value1).encode() )
    #mqttc.publish( b'/loadcell2/force2/', str(value2).encode() )
    #mqttc.publish( b'/loadcell2/force3/', str(value3).encode() )
    #mqttc.publish( b'/loadcell2/force4/', str(value4).encode() )
    #mqttc.publish( b'/loadcell2/force5/', str(value5).encode() )
    mqttc.publish( b'/loadcell2/forceavg/', str(valueavg).encode() )
    #print("HX Get Value1:", value1)
    #print("HX Get Value2:", value2)
    #print("HX Get Value3:", value3)
    #print("HX Get Value4:", value4)
    #print("HX Get Value5:", value5)
    print("HX Get Valueavg:", valueavg)
    time.sleep(0.05)