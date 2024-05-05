# this is where the PCB project begins!

class state:
    def __init__(self):
        self.launch = 0
        self.accel = 0
        self.motorOut = 0
        self.airBrakes = 0
        self.apogee = 0
        self.main = 0

    # where 0 means that the state hasn't been completed, and 1 means 
    # the state has been completed
    
    def rocketAccel(self, acceleration):
        if acceleration > 32.194:
            self.accel = 1
        else:
            self.accel = self.accel

    def rocketMotorOut(self, acceleration):
        if acceleration == 32.194:
            self.motorOut = 1
        else:
            self.motorOut = self.motorOut
        
    def rocketAirBrakes(self, acceleration, altitude):
        if altitude > 8000:
            if acceleration == 32.194:
                self.airBrakes = 1
            
