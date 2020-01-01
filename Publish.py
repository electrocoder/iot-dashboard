#!/usr/bin/python
# -*- coding: utf-8 -*-

# MQTT Python Publish Örneği
# Mese Bilisim

import paho.mqtt.client as mqtt
import time


MQTT_HOST = "iothook.com" 
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "test"
MQTT_MSG = ""


def on_connect(client, userdata, flags, rc):
	print(client, userdata, flags, rc)


def on_publish(client, userdata, mid):
	print(client, userdata, mid)


def on_log(mqttc, obj, level, string):
    print(mqttc, obj, level, string)


mqttc = mqtt.Client()

mqttc.on_log = on_log
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish


# mqttc.username_pw_set(username="username", password="password")
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

for i in range(0, 5000000):
	MQTT_MSG = "data/%s" % i
	mqttc.publish(MQTT_TOPIC, MQTT_MSG)
	time.sleep(1)

mqttc.disconnect()

