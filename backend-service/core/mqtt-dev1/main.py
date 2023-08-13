import paho.mqtt.client as mqtt
import time
import random

mqtt_broker = "192.168.1.69"

client = mqtt.Client("P1")
client.connect(mqtt_broker)

def publish_infinitely():
    while True:
        num = random.randint(0, 100)
        msg = f"test{num}"
        print(f"publishing {msg}")
        client.publish("test/espTopic", msg)
        time.sleep(1)

if __name__ == "__main__":
    print("mqtt protocol initialized.")
    publish_infinitely()
    