# this is where the PCB project begins!

class state:
    def __init__(self):
        self.launch = 1
        self.accel = 1
        self.motorOut = 1
        self.airBrakes = 1
        self.apogee = 1
        self.main = 1
        self.state = None

    # idea: maybe have a string that is produced from the 1s and 0s?

    # where 1 means that the state hasn't been completed, and 2 means 
    # the state has been completed
    
    # determine margin of error for acceleration and altitude
        
    # need to account for the initial altitude that the rocket
    # is at on the launch stand. This could potentially be 
    # determined when the rocket circuit check is completed!
    # and will need another function
    
    def rocketAccel(self, acceleration, velocity):
        if acceleration > -32.194:
            self.accel = 2
        else:
            self.accel = self.accel
            self.motorOut = 1
            self.airBrakes = 1
            self.apogee = 1
            self.main = 1

    def rocketMotorOut(self, acceleration, velocity):
        if acceleration == -32.194:
            self.accel = 1
            self.motorOut = 2
            self.airBrakes = self.airBrakes
            self.apogee = self.apogee
            self.main = self.main
        else:
            self.motorOut = self.motorOut
        
    def rocketAirBrakes(self, acceleration, velocity, altitude):
        if altitude > 8000:
            if self.accel == 1: # unsure if this should be a condition
                self.airBrakes = 2
            else:
                self.airBrakes = 1
        else:
            self.airBrakes = 1

    def rocketApogee(self, acceleration, velocity, altitude):
        if altitude == 10000:
            if velocity == 0:
                if acceleration == -32.194:
                    self.apogee = 2
                else:
                    self.airBrakes = 1
            else:
                self.airBrakes = 1
        else:
            self.airBrakes = 1

    def rocketMain(self, acceleration, velocity, altitude):
        if acceleration == 32.194:
            if altitude == 1000:
                self.main = 2
            else:
                self.main = 1
