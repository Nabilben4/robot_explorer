import streamlit as st

import paho.mqtt.client as mqtt
import time

#-------configuration du broker------------
mqtt_broker = "test.mosquitto.org"
mqtt_port = 1883


#-------config client-----
mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)

 #------fonction envoi de message-----------------   
def send_message(n,mqtt_topic):
    message = str(n)
    mqtt_client.publish(mqtt_topic, message)

#---------------------------------------------------

st.subheader("Commande du servomoteur ")
tilt = st.slider("tilt",min_value=1,max_value=100,value=50,step=1)
send_message(tilt,"robot/servo1")
pan = st.slider("pan",min_value=1,max_value=100,value=50,step=1)
send_message(pan,"robot/servo2")

init = st.button("init")

mav = st.button("avant",on_click=True)

mar = st.button("arriere")

dte = st.button("droite")

gau = st.button("gauche")

stop = st.button("stop")

if init:
    send_message(50,"robot/servo1")
    send_message(50,"robot/servo2")
    
if mav:
    send_message(1023,"robot/mav")
if mar:
    send_message(1023,"robot/mar")
if dte:
    send_message(128,"robot/dte")
if gau:
    send_message(128,"robot/gau")
if stop:
    send_message(0,"robot/stop")
st.write(mav)
mqtt_client.loop()
#-----------------------------------------------
