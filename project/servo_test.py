#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# setup the callback routine, the system will run the callback function
# if it detects a falling edge in one of these GPIOs
GPIO.setmode(GPIO.BCM) 
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

s1 = GPIO.PWM(19, 46.5)
s2 = GPIO.PWM(13, 46.5)
p = GPIO.PWM(5,50)
p.start(7.5)
s1.start(0)
s2.start(0)

# num:1 left servo
#     2 right servo

# dir:1 clockwise
#     -1 counterclockwise
#     0 stop
def set_direction(num,dir):
    if num==1:
        if dir==1:
            dc=7.8
        elif dir==0:
            dc=6.9
        elif dir==-1:
            dc=6.0
        s1.ChangeDutyCycle(dc)
    elif num==2:
        if dir==1:
            dc=7.8
        elif dir==0:
            dc=6.9
        elif dir==-1:
            dc=6.0
        s2.ChangeDutyCycle(dc)

if __name__ == '__main__':
    set_direction(2, 0)
    set_direction(1, 0)
##   while True:
##        p.ChangeDutyCycle(7.5)
##        time.sleep(1)
##        p.ChangeDutyCycle(12.5)
##        time.sleep(1)
    i = raw_input()
        

s1.stop()
s2.stop()
GPIO.cleanup()



