# Import package
import paho.mqtt.client as mqtt
import time

# Define Variables
# MQTT_HOST = "iot.eclipse.org" 
MQTT_HOST = "localhost" 
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "/45/sahin/"
MQTT_MSG = "/gonder/kalorifer/33/"

def on_connect(client, userdata, flags, rc):
	print("Connected flags ",str(flags),"result code ",str(rc))
	print(userdata)
	print("Baglanti saglandi...")

# Define on_publish event function
def on_publish(client, userdata, mid):
	print(userdata)
	print "Mesaj gonderildi..."

def on_log(mqttc, obj, level, string):
    print(string)

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish

# Connect with MQTT Broker
mqttc.on_log = on_log
mqttc.username_pw_set(username="mese", password="mese")
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

while True:
	# Publish message to MQTT Broker 
	mqttc.publish(MQTT_TOPIC, MQTT_MSG)
	# mqttc.publish(MQTT_TOPIC,MQTT_MSG, qos=2) # mesaj alma protokolu
	time.sleep(3)

# Disconnect from MQTT_Broker
mqttc.disconnect()