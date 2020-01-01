#!/usr/bin/python
# -*- coding: utf-8 -*-

# MQTT Python Subscribe Örneği
# Mese Bilisim

import paho.mqtt.client as mqtt


def on_message(mosq, obj, msg):
    print("MESSAGE: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.connect("iothook.com", 1883, 60)
mqttc.subscribe("#", 0)

mqttc.loop_forever()
