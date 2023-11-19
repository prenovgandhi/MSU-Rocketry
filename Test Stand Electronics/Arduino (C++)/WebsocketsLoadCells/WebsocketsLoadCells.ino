#include <ArduinoWebsockets.h>

 #include <WiFi.h> // For ESP32

const char* ssid = "RocketryMQTTAP"; // Replace with your WiFi SSID
const char* password = "gospartans"; // Replace with your WiFi password

const char* websockets_server_host = "192.168.0.100"; // Replace with your WebSocket server URL
//const char* websockets_server_host = "ws://192.168.0.100:1880/ws/stand/thrustloadcell/forceavg"; // Replace with your WebSocket server URL
const uint16_t websockets_server_port = 1880; // Replace with your WebSocket server port, typically 80 for WS or 443 for WSS

using namespace websockets;

WebsocketsClient client;

void setup() {
  Serial.begin(115200);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");

  // Connect to WebSocket server

  client.onEvent(onWebsocketEvent);
  Serial.println("\n line 30");
  client.connect(websockets_server_host, websockets_server_port, "/ws/stand/thrustloadcell/forceavg"); // The path is typically "/" but might be different on your server
  Serial.println("\n line 32");
}

void loop() {
  client.poll();

  // Here you can send messages periodically or based on some conditions
  // For example, to send a message every 10 seconds:
  static unsigned long lastTime = 0;
  if (millis() - lastTime > 1000) {
    lastTime = millis();
    client.send("Hello from Arduino"); // Replace with your message
  }
}

void onWebsocketEvent(WebsocketsClient& client, WebsocketsEvent event, String data) {
  if(event == WebsocketsEvent::ConnectionOpened) {
    Serial.println("Connnection Opened");
  } 
  else if(event == WebsocketsEvent::ConnectionClosed) {
    Serial.println("Connnection Closed");
  } 
  else if(event == WebsocketsEvent::GotPing) {
    Serial.println("Got a Ping!");
  } 
  else if(event == WebsocketsEvent::GotPong) {
    Serial.println("Got a Pong!");
  } 
  // else if(event == WebsocketsEvent::GotText) {
  //   Serial.println("Got Text: " + data);
  // }
}
