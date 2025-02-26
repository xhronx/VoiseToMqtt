from paho.mqtt import client as mqtt_client
#from paho.mqtt.client import client as mqtt_client
#import paho.mqtt.client as mqtt
#import json

mqtt = mqtt_client.Client("test")
#mqtt.username_pw_set("test","test")
#mqtt.connect("192.168.0.11", 1883)
#mqtt.subscribe("tele/tasmota_4AC310/SENSOR")
#mqtt.on_message = on_message
#mqtt.loop_forever()