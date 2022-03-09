#!/usr/bin/python

from tokenize import String
from numpy import character
import RPi.GPIO as GPIO
import xbox_read
import time

#pwm.setPWMFreq(60)

GPIO.setmode(GPIO.BCM)
class Motor:
    def __init__(self,p1,p2,enable):
        self.pin1=p1
        self.pin2=p2
        GPIO.setup(self.pin1,GPIO.OUT)
        GPIO.setup(self.pin2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        self.pwm=GPIO.PWM(enable,1000)


    def setDir(self, forward):  #1=true=forward, 0=false=backwards
        if(forward):
            GPIO.output(self.pin1,1)
            GPIO.output(self.pin2,0)
        else:
            GPIO.output(self.pin1,0)
            GPIO.output(self.pin2,1)


    def stop(self):
        GPIO.output(self.pin1, 0)
        GPIO.output(self.pin2, 0)


    def setDuty(self, level: character):  #l=low=75%, m=medium=50%, h=high=40%
        if level=='l':
            self.pwm.ChangeDutyCycle(75)
        if level=='m':
            self.pwm.ChangeDutyCycle(50)
        if level=='h':
            self.pwm.ChangeDutyCycle(40)

 
def analogsticks(motor: Motor, value : int):
    motor.setDir(value>0)
    temp = abs(value)
    if temp > 32000:
        motor.setDuty('h')
    elif temp > 16000:
        motor.setDuty('m')
    elif temp > 0:
        motor.setDuty('l')
    else:
        motor.stop()

#Right trigger is upwards, left trigger is downwards
def triggers(motor: Motor):
    motor.setDir(rt_intensity>=lt_intensity)
    temp = max(rt_intensity,lt_intensity)
    if temp > 250:
        motor.setDuty('h')
    elif temp > 0:
        motor.setDuty('l')
    else:
        motor.stop

#We need to assign these pins
vertmotor = Motor(1,2,3)
leftmotor = Motor(1,2,3)
rightmotor = Motor(1,2,3)
lt_intensity = 0
rt_intensity = 0
for event in xbox_read.event_stream(deadzone=12000):
    if event.key=='RT' or event.key=='LT':
        if event.key=='RT':
            rt_intensity = event.value
        else:
            lt_intensity = event.value
        triggers(vertmotor) 
    if event.key=='Y1':
        analogsticks(leftmotor, event.value)
    if event.key=='Y2':
        analogsticks(rightmotor, event.value)


