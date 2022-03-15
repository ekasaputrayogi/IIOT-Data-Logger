# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import machine
import time
import network
import os
import configuration
import wifi_connection
import pinconfig
from umqtt.simple import MQTTClient



led = machine.Pin(2, machine.Pin.OUT)

while True:
    #---Connect to Wifi---#
    config = configuration.open_config()
    station = network.WLAN(network.STA_IF)
    station.active(False)
    station.active(True)
    station.connect(config[0], config[1])

    if station.isconnected() == True:
        print("Connection successful")
        print(station.ifconfig())

        led.on()
        print(config[6])            
        pinconfig()

        #---Connect to MQTT Server---#
        server = config[2]
        user_name = config[3]
        user_password = config[4]
        port = config[5]
        try:
            client = MQTTClient("umqtt_client",server)
            client.connect()
        except Exception as e:
            print("Unable to connect to mqtt server: ", e)
            continue

        #---Processing and sending data to MQTT Server---#
        while True:
            data_pin0 = pinconfig.pin0_read()
            if station.isconnected() == False:
                break
            try:
                client.publish("IOTBOX", str(data_pin0))
            except:
                print("Unable to send data")
                time.sleep(3)
                break
            time.sleep(0.5)
            
    elif station.isconnected() == False:
        led.off()
        config = configuration()
        config = configuration.create_config()

    
