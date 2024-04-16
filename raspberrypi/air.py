from sensor import Sensor
from state import State

# Bit latches: this serves as a signal that we are entering a particular stage. 
# setting one of these to true means that we are currently entering the relevant stage.
arm                 = False
liftoff             = False
apogee              = False
main_deploy         = False
recovery            = False

# Current state latches: when true, it means that the current stage has been reached.
_armed              = False  # Rocket is armed.
_liftoff_detected   = False  # Rocket is accelerating
_apogee_detected    = False  # Algorithm detects that apogee is reached
_main_deployed      = False  # Main parachute is deployed

#######################################################################
# Initialization
#######################################################################

# initialize our sensors so we can read from them, and start collecting data
sensors = Sensor()
sensors.start_sensors()

# initialize state object so we can determine/change state
state = State()

# Main loop
while True:

    #######################################################################
    # Interpret state information from ground station
    #######################################################################

    # TODO: figure out what this variable needs to be, maybe xbee stuff
    new_state = ""

    if new_state != "":

        new_state = ord(new_state)  # convert from char to int

        # Get bit flags from new state
        arm         = state.get_bit(state.ARM_BIT, byte=new_state)
        liftoff     = state.get_bit(state.LIFTOFF_BIT, byte=new_state)
        apogee      = state.get_bit(state.APOGEE_BIT, byte=new_state)
        main_deploy = state.get_bit(state.MAIN_DEPLOY_BIT, byte=new_state)
        recovery    = state.get_bit(state.RECOVERY_BIT, byte=new_state)

        ### Arm rocket ###
        if arm:
            if not _armed:
                _armed = True
                #TODO: should we send a message here through MQTT (like how message is printed below)?
                print("Armed")
        else:
            # if we're armed, we are now in liftoff stage so other stages are set to False
            if _armed:
                _armed = False
                _apogee_detected = False
                _main_deployed = False
                freefall_counter = 0
                apogee_counter = 0

        ### Liftoff detected ###
        if liftoff:
            if not _liftoff_detected:
                _liftoff_detected = True
        else:
            # no longer in powered flight
            if _liftoff_detected:

               # TODO: probably detect apogee here?

        ### apogee detected ###
        if apogee:
            if not _apogee_detected:
                _apogee_detected = True
        else:
            if _apogee_detected:
               # _apogee_detected = False
               pass
            
