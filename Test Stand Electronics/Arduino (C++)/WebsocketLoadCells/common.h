// Common.h
#ifndef COMMON_H
#define COMMON_H

#include <ArduinoWebsockets.h>
#include <WiFi.h>

const char* ssid = "yourSSID"; // Replace with your WiFi SSID
const char* password = "yourPASSWORD";  // Replace with your WiFi Password

using namespace websockets;

extern WebsocketsClient client;

void connectToWiFi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
}

void connectToWebSocket(const char* websockets_server) {
  client.onEvent(webSocketEvent);
  client.connect(websockets_server);
}

void webSocketEvent(WebsocketsEvent event, String data) {
  // Handle WebSocket events
}

#endif
