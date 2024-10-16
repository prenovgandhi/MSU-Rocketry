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
#######################################################################

# initialize our sensors so we can read from them, and start collecting data
sensors = Sensor()

# initialize state object so we can determine/change state
state = State()

#TODO: xbee stuff, see MSU-Rocketry/FrontierOS/mosquittopub.py on the github

# initially, we will be in the idle state
current_state = "idle"

# Main loop
while True:

    #######################################################################
    # Interpret state information
    #######################################################################

    # if y-acceleration equals ~9.8, we are entering the armed state
    #TODO: make this a range instead of exactly 9.8
    # if sensors.mpu.acceleration[1] == 9.8:
    sensors.start_sensors()
