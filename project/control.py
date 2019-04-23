#!/usr/bin/env python

import BlynkLib
import time
import numpy as np
import RPi.GPIO as GPIO
import time
import sys

# setup the callback routine, the system will run the callback function
# if it detects a falling edge in one of these GPIOs
GPIO.setmode(GPIO.BCM) 
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP) # set pin 17, input mode:pull_up

s1 = GPIO.PWM(19, 46.5)
s2 = GPIO.PWM(13, 46.5)
p = GPIO.PWM(5,50)
s1.start(0)
s2.start(0)
p.start(0)

# NUM: 0 LEFT SERVO
#      1 RIGHT SERVO

def set_wheel(num, value):
    if num == 0:
        dc = (7.8-6.0)/255*value+6.0
        if value == 128:
            dc = 0
        s1.ChangeDutyCycle(dc)
    elif num == 1:
        dc = (7.8-6.0)/255*value+6.0
        if value == 128:
            dc = 0
        s2.ChangeDutyCycle(dc)
    elif num == 2:
        if value == 1:
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
            p.ChangeDutyCycle(0)
            time.sleep(0)
        elif value == 0:
            p.ChangeDutyCycle(12.5)
            time.sleep(1)            
            p.ChangeDutyCycle(0)
            time.sleep(0)

def GPIO17_callback(channel):
    s1.stop()
    s2.stop()
    p.stop()
    GPIO.cleanup()
    sys.exit()

GPIO.add_event_detect(17,GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)

###########
## BLYNK ##
###########

BLYNK_AUTH = 'a3405a6221a7467eb097be95034e2c54'

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.ON("V*")
# update the value of virtual pins in this function
def blynk_handle_vpins(pin, value):
    global pin_value
    pin_value[int(pin)] = int(value[0])
    if int(pin) <= 2:
##        print('sent')
        set_wheel(int(pin),int(value[0]))

@blynk.ON("connected")
def blynk_connected():
    # You can also use blynk.sync_virtual(pin)
    # to sync a specific virtual pin
    print("Updating V0 values from the server...")
    blynk.sync_virtual(0,1,2)

pin_value = np.array([0,0,0])

while True:
    blynk.run()

    print(pin_value)
    time.sleep(0.5)
