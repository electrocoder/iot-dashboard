# Import package
import paho.mqtt.client as mqtt

count=0

# Define Variables
# MQTT_HOST = "iot.eclipse.org" 
MQTT_HOST = "localhost" 
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "/45/sahin/"
MQTT_MSG = ""

# Define on connect event function
# We shall subscribe to our Topic in this function
def on_connect(mosq, obj, rc):
 mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_message event function. 
# This function will be invoked every time,
# a new message arrives for the subscribed topic 
def on_message(mosq, obj, msg):
 global count
 print count
 count += 1
 print "Topic: " + str(msg.topic)
 print "QoS: " + str(msg.qos)
 print "Payload: " + str(msg.payload)
 print "------------------"

def on_subscribe(mosq, obj, mid, granted_qos):
 print("Subscribed to Topic: " + 
 MQTT_MSG + " with QoS: " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

# Initiate MQTT Client
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.on_log = on_log
mqttc.username_pw_set(username="mese", password="mese")
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()