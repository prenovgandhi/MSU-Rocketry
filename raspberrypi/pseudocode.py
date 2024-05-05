# Initialize variables
max_altitude = 0
current_altitude = 0
previous_altitude = 0
max_altitude_tolerance = 10  # Tolerance for detecting peak altitude
is_ascent = True
is_deployed_main = False
is_deployed_drogue = False

# Main loop
while True:
    # Read altitude from altimeter
    current_altitude = read_altitude()

    # Read altitude from GPS
    gps_altitude = read_gps_altitude()

    # Read pressure from barometer
    pressure = read_pressure()

    # Detect ascent
    if current_altitude > previous_altitude:
        is_ascent = True
    else:
        is_ascent = False

    # Detect apogee
    if not is_ascent and abs(current_altitude - max_altitude) <= max_altitude_tolerance:
        # Apogee detected
        deploy_drogue()
        is_deployed_drogue = True

    # Update maximum altitude
    max_altitude = max(max_altitude, current_altitude)

    # Check for main parachute deployment
    if current_altitude <= target_main_parachute_altitude and not is_deployed_main:
        deploy_main()
        is_deployed_main = True

    # Check for landing
    if current_altitude <= 0:
        break

    # Update previous altitude
    previous_altitude = current_altitude

    # Sleep for some time before next iteration
    sleep(interval)
