// Common.h
#ifndef COMMON_H
#define COMMON_H

#include <ArduinoWebsockets.h>
//ArduinoWebSockets by Gil Maimon...
#include <WiFi.h>
//should be here already if you'pre using an esp32

const char* ssid = "RocketryMQTTAP"; // Replace with your WiFi SSID
const char* password = "gospartans";  // Replace with your WiFi Password

using namespace websockets;

extern WebsocketsClient client;

void connectToWiFi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
}

void webSocketEvent(WebsocketsEvent event, String data) {
  // Handle WebSocket events
}

void connectToWebSocket(const char* websockets_server) {
  client.onEvent(webSocketEvent);
  client.connect(websockets_server);
}

void sendPing() {
  if (client.ping()) {
    Serial.println("Sent Ping");
  } else {
    Serial.println("Ping Failed");
  }
}


#endif
