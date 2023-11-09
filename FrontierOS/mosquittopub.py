import subprocess
import serial

# Configure the serial port
serial_port = serial.Serial('COM7', 9600)  # Replace with the actual COM port and baud rate

# MQTT broker configuration
mqtt_broker = "localhost"  # Use "localhost" if your MQTT broker is running locally
mqtt_port = 1883  # Replace with the MQTT broker port

# Function to publish a message to MQTT
def publish_to_mqtt(topic, message):
    command = [
        "mosquitto_pub",
        "-h", mqtt_broker,
        "-p", str(mqtt_port),
        "-t", topic,
        "-m", message,
    ]
    subprocess.run(command)

# Main loop to read from serial and publish to MQTT
try:
    while True:
        line = serial_port.readline().decode().strip()
        if line:
            parts = line.split(" ")
            topic, message = parts[0], parts[1]
            publish_to_mqtt(topic, message)
except KeyboardInterrupt:
    serial_port.close()
