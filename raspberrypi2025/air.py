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

  GNU nano 7.2                         air.py                                   
from sensor import Sensor
from state import State

# Bit latches: this serves as a signal that we are entering a particular stage.
# Setting one of these to true means that we are currently entering the relevan>
arm                 = False
liftoff             = False
apogee              = False
main_deploy         = False
recovery            = False

# Current state latches: when true, it means that the current stage has been re>
_armed              = False  # Rocket is armed.
_liftoff_detected   = False  # Rocket is accelerating
_apogee_detected    = False  # Algorithm detects that apogee is reached
_main_deployed      = False  # Main parachute is deployed


#######################################################################
# Initialization
