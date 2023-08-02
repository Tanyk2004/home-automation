import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("received:" , str(message.payload.decode('utf-8')))

mqtt_broker = "192.168.1.69"

client = mqtt.Client("P2")
client.connect(mqtt_broker)

client.loop_start()

client.subscribe("outTopic")
client.on_message=on_message
time.sleep(60)
client.loop_stop()

def publish_infinitely():
    while True:
        client.publish("test", "test")
        time.sleep(1)

if __name__ == "__main__":
    print("mqtt protocol initialized.")
   