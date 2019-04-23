#!/usr/bin/env python

import time
import numpy as np
import RPi.GPIO as GPIO
import time
import sys
import subprocess


GPIO.setmode(GPIO.BCM) 
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP) # set pin 17, input mode:pull_up


def GPIO22_callback(channel):
    subprocess.call("/home/pi/project/control.py", shell=True)

GPIO.add_event_detect(22,GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)

while True:
    time.sleep(10)
