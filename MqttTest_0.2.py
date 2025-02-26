import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    #print(f"Connected with result code {reason_code}")
    mqttc.publish("test/test1", "111")
    mqttc.disconnect()
    #mqttc.loop_stop()
    mqttc.publish("test/test2", "222")
#    # Subscribing in on_connect() means that if we lose the connection and
#    # reconnect then subscriptions will be renewed.
#    client.subscribe("$SYS/#")local

# The callback for when a PUBLISH message is received from the server.
#def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
#mqttc = mqtt.CONNECT("dfsfdhsgfksdghfkj")
mqttc.username_pw_set("test","test")
mqttc.connect("127.0.0.1", 1883)

mqttc.on_connect = on_connect
#mqttc.on_message = on_message

#mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()
