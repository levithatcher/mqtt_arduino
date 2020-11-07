import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect("localhost", 1883)
client.loop_start()

client.publish("house/bulbs", "ON")