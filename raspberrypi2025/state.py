class State:

    def __init__(self):
        '''
        Define different states of the rocket.

        Each state has an assigned bit corresponding to a bit in the binary integer "0000 0000".
        When sending a command to change the state, we can send a single byte: each of the 8 bits
        signifies which state is currently active (i.e. sending "7"  would mean "0000 0111" in binary,
        so the first 3 states (from right to left) are active)
        '''

        # idle, default state
        self.IDLE = 0

        # rocket has been armed
        self.ARMED = 1 # sending this number means we are entering this state
        self.ARMED_BIT = 0 # this state's place in the 8-bit binary integer

        # rocket is accelerating (powered flight)
        self.LIFTOFF = 2
        self.LIFTOFF_BIT = 1

        # we have reached apogee, deploy drogue parachute
        self.APOGEE = 4
        self.APOGEE_BIT = 2

        # we are at an altitude of 1000 feet, deploy main parachute
        self.MAIN_DEPLOY = 8
        self.MAIN_DEPLOY_BIT = 3

        # recovery mode
        self.RECOVERY = 16
        self.RECOVERY_BIT  = 4

    # Set state
    def set(self, new_state):
        self.state = new_state

    # Add state (input each state as separate parameter)
    def add(self, *new_states):
        for new_state in new_states:
            self.state += new_state

    # Remove state
    def remove(self, *new_states):
        for new_state in new_states:
            self.state -= new_state


    def lift_off(self):
        while self.mpu.acceleration[1] > 0:

    def burnout(self):
        while True:
            val = []
            for n in range(5):
                n = self.mpu.acceleration[1]
                val.append(n)
            for i in values:
                total += i
                total = total / 5
                
    
                
            
            
