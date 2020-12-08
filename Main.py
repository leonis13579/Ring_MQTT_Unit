import paho.mqtt.client as mqtt
import random
import time
import threading


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe("base/relay/dynamic")
    client.subscribe("base/relay/notify")


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg


def thread_method():
    while True:
        client.publish("base/state/ring", True)
        print("Posted Ring")
        time.sleep(2)
        client.publish("base/state/ring", False)
        time.sleep(random.randint(20, 25))


client = mqtt.Client(client_id="mqtt-teeannet13-szom8f", transport="tcp")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("111", "111")
client.connect("dev.rightech.io", 1883)
x = threading.Thread(target=thread_method, args=())
x.start()
client.loop_forever()
