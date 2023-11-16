#include "Common.h"

const char* websockets_server = "ws://example.com:port"; // Specific WebSocket server URL for this sensor

WebsocketsClient client;

void setup() {
  Serial.begin(115200);
  connectToWiFi();
  connectToWebSocket(websockets_server);
}

void loop() {
  if (client.available()) {
    client.poll();
  }
  sendData();
}

void sendData() {
  // Your specific sensor data code
  String data = "Sensor Data";
  if (client.available()) {
    client.send(data);
  }
  delay(50); // Adjust as needed
}
