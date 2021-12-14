import paho.mqtt.client as mqtt

class MqqtClient:
    def __init__(self) -> None:
        pw = "Faelles123kode098"
        username = "iotgrp10"
        mqqt_uri = "626582a1d37a4c9da269c096cf520060.s1.eu.hivemq.cloud"
        
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
        client.username_pw_set(username, pw)
        client.connect(mqqt_uri, 8883)
        self.client = client
    
    def publish(self, topic, val):
        self.client.publish(topic, val, qos=0)

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected successfully")
        else:
            print("Connect returned result code: " + str(rc))

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))
