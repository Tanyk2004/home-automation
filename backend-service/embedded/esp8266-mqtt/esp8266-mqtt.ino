#include<ESP8266WiFi.h>
#include<PubSubClient.h>

const char *ssid = "tanyk2004";
const char *password = "Muffin@123";

const char *mqtt_broker = "192.168.1.69";
const char *topic = "test/topic";
const int mqtt_port = 1883;

WiFiClient espclient;
PubSubClient client(espclient);
unsigned long lastMsg = 0;
// defines a macro which perfoms text substitution before the code is run
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

void callBack( char *topic, byte *payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Message: ");
  for ( int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  Serial.println("-----------------------");
}

void connectToMqtt() {
  Serial.println("Connecting to MQTT");
  while (!client.connected()) {
    Serial.println("Attempting connection...");

    String clientId = "ESP8266-";
    clientId += String(random(0xffff), HEX);

    if (client.connect(clientId.c_str())) {
      Serial.println("Connected to the broker.");
      client.publish("test/espTopic", "hollaaaaaaa konnichiwaaaaaaa");
      client.subscribe("test/espTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void connectToWifi() {
  Serial.println();
  Serial.println();
  Serial.println("Connecting to WiFi");
  Serial.println();
  WiFi.begin(ssid, password);
  int retries = 0;
  while ( (WiFi.status() != WL_CONNECTED) && ( retries < 15) ) {
    retries++;
    delay(500);
    Serial.print(".");
  }
  if ( retries > 14 ) {
    Serial.println("WiFi connection Failed");
  }
  if ( WiFi.status() == WL_CONNECTED) {
    Serial.println("WiFi Connected");
    Serial.println("IP Address: ");
    Serial.println(WiFi.localIP());
  }
}


void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  Serial.begin(115200);
  connectToWifi();
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callBack);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (!client.connected()) {
    connectToMqtt();
  }
  client.loop();
  unsigned long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
    snprintf (msg, MSG_BUFFER_SIZE, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("outTopic", msg);
  }
}
