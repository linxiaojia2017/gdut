#!/usr/bin/python
import os
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)

GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

GPIO.output(5,GPIO.HIGH)
GPIO.output(6,GPIO.HIGH)

tire_left_f = GPIO.PWM(17,50)
tire_left_b = GPIO.PWM(27,50)
tire_right_f = GPIO.PWM(23,50)
tire_right_b = GPIO.PWM(24,50)

turn_control = GPIO.PWM(25,50)
take_control_l = GPIO.PWM(18,50)
take_control_r = GPIO.PWM(21,50)


red_l = GPIO.PWM(13,50)
green_l = GPIO.PWM(19,50)
blue_l = GPIO.PWM(26,50)

red_r = GPIO.PWM(12,50)
green_r = GPIO.PWM(16,50)
blue_r =GPIO.PWM(20,50)

tire_left_f.start(0)
tire_right_f.start(0)
tire_left_b.start(0)
tire_right_b.start(0)

turn_control.start(0)

take_control_l.start(0)
take_control_r.start(0)

red_l.start(0)
green_l.start(0)
blue_l.start(0)
red_r.start(0)
green_r.start(0)
blue_r.start(0)


def take(argument1):
    if argument1=='grasp':
        take_control_l.ChangeDutyCycle(7.5)
        take_control_r.ChangeDutyCycle(7.5)
        time.sleep(1)
        take_control_l.ChangeDutyCycle(0)
        take_control_r.ChangeDutyCycle(0)
    else:
        take_control_l.ChangeDutyCycle(12.5)
        take_control_r.ChangeDutyCycle(2.5)
        time.sleep(1)
        take_control_l.ChangeDutyCycle(0)
        take_control_r.ChangeDutyCycle(0)

def turn(argument1):
    if argument1=='right':
        turn_control.ChangeDutyCycle(20)
        time.sleep(2)
        turn_control.ChangeDutyCycle(0)
    elif argument1=='left':
        turn_control.ChangeDutyCycle(1)
        time.sleep(2)
        turn_control.ChangeDutyCycle(0)
    else:
        turn_control.ChangeDutyCycle(5.5)
        time.sleep(2)
        turn_control.ChangeDutyCycle(0)

def stop():
    tire_left_f.ChangeDutyCycle(0)
    tire_right_f.ChangeDutyCycle(0)
    tire_left_b.ChangeDutyCycle(0)
    tire_right_b.ChangeDutyCycle(0)

def control_tire(sl,sr,speedl,speedr,t):
    if sl == 'f':
        tire_left_f.ChangeDutyCycle(float(speedl))
        tire_left_b.ChangeDutyCycle(0)
    else:
        tire_left_f.ChangeDutyCycle(0)
        tire_left_b.ChangeDutyCycle(float(speedl))
    if sr == 'f':
        tire_right_f.ChangeDutyCycle(float(speedr))
        tire_right_b.ChangeDutyCycle(0)
    else:
        tire_right_f.ChangeDutyCycle(0)
        tire_right_b.ChangeDutyCycle(float(speedr))
    time.sleep(float(t))
    stop()

def go_straight(speed,t):
    control_tire('f','f',speed,speed,t)

def backward(speed,t):
    control_tire('b','b',speed,speed,t)

def turn_left(speed,t): 
    control_tire('b','f',speed,speed,t)

def turn_right(speed,t): 
    control_tire('f','b',speed,speed,t)

def mycycle(speedl,speedr,t):
    control_tire('f','f',speedl,speedr,t)

def led(argument1,argument2,argument3):
    if argument1=='s':
        red_l.ChangeFrequency(5)
        green_l.ChangeFrequency(5)
        blue_l.ChangeFrequency(5)
        red_r.ChangeFrequency(5)
        green_r.ChangeFrequency(5)
        blue_r.ChangeFrequency(5)
    else:
        red_l.ChangeFrequency(50)
        green_l.ChangeFrequency(50)
        blue_l.ChangeFrequency(50)
        red_r.ChangeFrequency(50)
        green_r.ChangeFrequency(50)
        blue_r.ChangeFrequency(50)
    if argument2=='r': 
        red_l.ChangeDutyCycle(50)
        green_l.ChangeDutyCycle(100)
        blue_l.ChangeDutyCycle(100)
    elif argument2=='g':
        red_l.ChangeDutyCycle(100)
        green_l.ChangeDutyCycle(50)
        blue_l.ChangeDutyCycle(100)
    elif argument2=='b':
        red_l.ChangeDutyCycle(100)
        green_l.ChangeDutyCycle(100)
        blue_l.ChangeDutyCycle(50)
    elif argument3=='f':
        red_l.ChangeDutyCycle(100)
        green_l.ChangeDutyCycle(100)
        blue_l.ChangeDutyCycle(100)
    else:
        pass
    if argument3=='r': 
        red_r.ChangeDutyCycle(50)
        green_r.ChangeDutyCycle(100)
        blue_r.ChangeDutyCycle(100)
    elif argument3=='g':
        red_r.ChangeDutyCycle(100)
        green_r.ChangeDutyCycle(50)
        blue_r.ChangeDutyCycle(100)
    elif argument3=='b':
        red_r.ChangeDutyCycle(100)
        green_r.ChangeDutyCycle(100)
        blue_r.ChangeDutyCycle(50)
    elif argument3=='f':
        red_r.ChangeDutyCycle(100)
        green_r.ChangeDutyCycle(100)
        blue_r.ChangeDutyCycle(100)
    else:
        pass

def fan(argument1):
    if argument1=='on':
        take('grasp')
        GPIO.output(1,GPIO.HIGH)
    else:
        GPIO.output(1,GPIO.LOW)
        time.sleep(0.1)
        take('release')

def gods_init():
    stop()
    take('release')
    fan('off')
    led('s','r','b')

gods_init()
cnumber=0
while 1:
    f=open('/root/command/zeus')
    command=f.readline().split()
    f.close()
    if command==['cmd:done','argument1:0','argument2:0','argument3:0']:
        time.sleep(0.1)
    else:
        cnumber=cnumber+1
        print cnumber,

        cmd=command[0][4:]
        argument1=command[1][10:]
        argument2=command[2][10:]
        argument3=command[3][10:]

        if cmd=='walk':
            if argument1=='w':
                print 'walk w'
                go_straight(argument2,argument3)
            elif argument1=='d':
                print 'walk d'
                turn_right(argument2,argument3)
            elif argument1=='a':
                print 'walk a'
                turn_left(argument2,argument3)
            elif argument1=='s':
                print 'walk s'
                backward(argument2,argument3)
            else:
                print 'walk stop'
                stop()
        elif cmd=='take':
            print 'take',argument1
            take(argument1)
        elif cmd=='turn':
            print 'turn',argument1
            turn(argument1)        
        elif cmd=='led':
            print 'led',argument1,argument2,argument3
            led(argument1,argument2,argument3)
        elif cmd=='fan':
            print 'fan',argument1
            fan(argument1)
        elif cmd=='cycle':
            print 'cycle',argument1,argument2,argument3
            mycycle(argument1,argument2,argument3)
        elif cmd=='shutdown'
            print 'zeus shotdown'
            f=open('/root/command/zeus',"w")
            f.write("cmd:done argument1:0 argument2:0 argument3:0")
            f.close()
            break
        else:
            print 'Unknow command'
            break
        f=open('/root/command/zeus',"w")
        f.write("cmd:done argument1:0 argument2:0 argument3:0")
        f.close()
GPIO.cleanup()
