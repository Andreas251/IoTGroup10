import paho.mqtt.client as mqtt

pw = "Faelles123kode098"
username = "iotgrp10"
mqqt_uri = "626582a1d37a4c9da269c096cf520060.s1.eu.hivemq.cloud"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set(username, pw)

# connect to HiveMQ Cloud on port 8883
client.connect(mqqt_uri, 8883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic")

# publish "Hello" to the topic "my/test/topic"
client.publish("my/test/topic", "Hello")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()










