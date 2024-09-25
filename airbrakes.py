# attempt at getting airbrakes to work
# deploy airbrakes after 8,000 ft has been reached

# def calculate(acceleration, velocity, altitude, cRocket, time1, time2, apogee = 10000):
#     # get values from gps and accelerometer
#     if altitude >= 8000 and acceleration != 0:
#         apo_time = -velocity/acceleration
#         predicted_apo = 0.5*acceleration*(apo_time**2) + velocity*apo_time + altitude
#         if predicted_apo > 10000:
#             print("DEPLOY!!!")
#             return predicted_apo
#         else:
#             pass
    
#     elif altitude < 8000:
#         pass
    
#     elif acceleration == 0:
#         pass
    
# print(calculate(-3, 130, 8500, 1, 1.1))

def ydc(t0, t1, y0, y1, ydd):
    # yd = -0.5*ydd - y0/t0
    return (-0.5*ydd*(t1 - t0) - (y1 - y0)/(t1 -t0))

def yddc(t0, t1, y0, y1, yd):
    # ydd = -2*(yd/t0) - 2*(y0/(t0^2))
    return (-2*(yd/(t1 - t0)) - 2*((y1-y0)/((t1 -t0)**2)))

# def calculate(t1, t2, y1, y2, ydd1, ydd2):
#     t = t2 - t1
#     y = y2 - y1
#     ydd = ydd2 - ydd1

#     yd = -0.5*ydd*t - y/t

#     apo_step = 0.5*-32.174*(t**2) + yd*t

#     apo = apo_step + 0.5*-32.174

# print(calculate(20, 21, 7000, 7500, 30, 31))

def rungeKutta(y0, y1, t0, t1, xdd, ydd, zdd):
    yd = ydc(t0, t1, y0, y1, ydd)
    print(yd)

    ydd = yddc(t0, t1, y0, y1, yd)

    h = t1 - t0
    
    m1 = h*yd
    k1 = h*ydd
    # update equation with only three inputs
    m2 = h*(yd + 0.5*k1)
    k2 = h*yddc(t0 + 0.5*h, y0 + 0.5*m1, yd + 0.5*k1)

    m3 = h*(yd +0.5*k2)
    k3 = h*yddc(t0 + 0.5*h, y0 + 0.5*m2, yd + 0.5*k2)

    m4 = h*(yd + k3)
    k4 = h*yddc(t0 + h, y0 + m3, yd + k3)

    ynp1 = y0 + (1/6)*(m1 + 2*m2 + 2*m3 + m4)
    ydnp1 = yd + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

    return ynp1

print(rungeKutta(8500, 8600, 24, 24.5, 0, -5, 0))