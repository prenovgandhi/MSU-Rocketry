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
