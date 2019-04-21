#!/usr/bin/python

import os
import time
import math
from PIL import Image

def control_turn(arg1,arg2,arg3):
    while arg1 != 'null':
        fzeus = open('/home/pi/zeus/zeus')
        cmd = fzeus.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fzeus.close()
            fzeus=open('/home/pi/zeus/zeus',"w")
            fzeus.write("cmd:turn argument1:"+arg1+" argument2:0 argument3:0\x0a")
            fzeus.close()
            break
        else:
            time.sleep(0.1)
            fzeus.close()
    while arg2 != 'null':
        fhades = open('/home/pi/hades/hades')
        cmd = fhades.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fhades.close()
            fhades=open('/home/pi/hades/hades',"w")
            fhades.write("cmd:turn argument1:"+arg2+" argument2:0 argument3:0\x0a")
            fhades.close()
            break
        else:
            time.sleep(0.1)
            fhades.close()
    while arg3 != 'null':
        fposeidon = open('/home/pi/poseidon/poseidon')
        cmd = fposeidon.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fposeidon.close()
            fposeidon=open('/home/pi/poseidon/poseidon',"w")
            fposeidon.write("cmd:turn argument1:"+arg3+" argument2:0 argument3:0\x0a")
            fposeidon.close()
            break
        else:
            time.sleep(0.1)
            fposeidon.close()

def control_fan(arg1,arg2,arg3):
    while arg1 != 'null':
        fzeus = open('/home/pi/zeus/zeus')
        cmd = fzeus.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fzeus.close()
            fzeus=open('/home/pi/zeus/zeus',"w")
            fzeus.write("cmd:fan argument1:"+arg1+" argument2:0 argument3:0\x0a")
            fzeus.close()
            break
        else:
            time.sleep(0.1)
            fzeus.close()
    while arg2 != 'null':
        fhades = open('/home/pi/hades/hades')
        cmd = fhades.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fhades.close()
            fhades=open('/home/pi/hades/hades',"w")
            fhades.write("cmd:fan argument1:"+arg2+" argument2:0 argument3:0\x0a")
            fhades.close()
            break
        else:
            time.sleep(0.1)
            fhades.close()
    while arg3 != 'null':
        fposeidon = open('/home/pi/poseidon/poseidon')
        cmd = fposeidon.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fposeidon.close()
            fposeidon=open('/home/pi/poseidon/poseidon',"w")
            fposeidon.write("cmd:fan argument1:"+arg3+" argument2:0 argument3:0\x0a")
            fposeidon.close()
            break
        else:
            time.sleep(0.1)
            fposeidon.close()

def control_take(arg1,arg2,arg3):
    while arg1 != 'null':
        fzeus = open('/home/pi/zeus/zeus')
        cmd = fzeus.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fzeus.close()
            fzeus=open('/home/pi/zeus/zeus',"w")
            fzeus.write("cmd:take argument1:"+arg1+" argument2:0 argument3:0\x0a")
            fzeus.close()
            break
        else:
            time.sleep(0.1)
            fzeus.close()
    while arg2 != 'null':
        fhades = open('/home/pi/hades/hades')
        cmd = fhades.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fhades.close()
            fhades=open('/home/pi/hades/hades',"w")
            fhades.write("cmd:take argument1:"+arg2+" argument2:0 argument3:0\x0a")
            fhades.close()
            break
        else:
            time.sleep(0.1)
            fhades.close()
    while arg3 != 'null':
        fposeidon = open('/home/pi/poseidon/poseidon')
        cmd = fposeidon.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fposeidon.close()
            fposeidon=open('/home/pi/poseidon/poseidon',"w")
            fposeidon.write("cmd:take argument1:"+arg3+" argument2:0 argument3:0\x0a")
            fposeidon.close()
            break
        else:
            time.sleep(0.1)
            fposeidon.close()

def control_led(arg1,arg2,arg3):
    while arg1 != 'null':
        fzeus = open('/home/pi/zeus/zeus',"r")
        cmd = fzeus.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fzeus.close()
            fzeus=open('/home/pi/zeus/zeus',"w")
            fzeus.write("cmd:led argument1:"+arg1[0]+" argument2:"+arg1[1]+" argument3:"+arg1[2]+'\x0a')
            fzeus.close()
            break
        else:
            time.sleep(0.1)
    while arg2 != 'null':
        fhades = open('/home/pi/hades/hades',"r")
        cmd = fhades.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fhades.close()
            fhades=open('/home/pi/hades/hades',"w")
            fhades.write("cmd:led argument1:"+arg2[0]+" argument2:"+arg2[1]+" argument3:"+arg2[2]+'\x0a')
            fhades.close()
            break
        else:
            time.sleep(0.1)
            fhades.close()
    while arg3 != 'null':
        fposeidon = open('/home/pi/poseidon/poseidon',"r")
        cmd = fposeidon.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fposeidon.close()
            fposeidon=open('/home/pi/poseidon/poseidon',"w")
            fposeidon.write("cmd:led argument1:"+arg3[0]+" argument2:"+arg3[1]+" argument3:"+arg3[2]+'\x0a')
            fposeidon.close()
            break
        else:
            time.sleep(0.1)
            fposeidon.close()


def getlocation(god):
    if god != 'zeus' and god != 'hades' and god != 'poseidon':return [-1,-1,-1]
    countred=0
    red_x_sum=0.0
    red_y_sum=0.0
    
    countblue=0
    blue_x_sum=0.0
    blue_y_sum=0.0
    os.system('python picp.py '+god)
    red=Image.open("red.jpg")
    red_array=red.load()
    for xred in range(400):
        for yred in range(400):
            if red_array[xred,yred] != 0:
                countred=countred+1
                red_x_sum=red_x_sum+xred
                red_y_sum=red_y_sum+yred

    blue=Image.open("blue.jpg")
    blue_array=blue.load()
    for xblue in range(400):
        for yblue in range(400):
            if blue_array[xblue,yblue] != 0:
                countblue=countblue+1
                blue_x_sum=blue_x_sum+xblue
                blue_y_sum=blue_y_sum+yblue
    red_x=red_x_sum/countred
    red_y=red_y_sum/countred
    blue_x=blue_x_sum/countblue
    blue_y=blue_y_sum/countblue
    d = math.degrees(math.atan((red_y-blue_y)/(red_x-blue_x)))
    if red_x-blue_x < 0 and red_y-blue_y > 0 :
        d = d+180
    if red_x-blue_x < 0 and red_y-blue_y < 0 :
        d = d-180
    d = d+90
    while d < 0:
        d=d+360
    while d > 360:
        d=d-360
    return [(red_x+blue_x)/2,(red_y+blue_y)/2,d]

def control_location(arg1,arg2,arg3):
    if arg1 != 'null':
        zeus_tl = [float(arg1[1:4]),float(arg1[5:8]),float(arg1[9:12])]
        zeus_cl = getlocation('zeus')
        if zeus_cl == [-1,-1,-1]:return -1
        zeus_x = zeus_tl[0]-zeus_cl[0]
        zeus_y = zeus_tl[1]-zeus_cl[1]
        zeus_degrees = math.degrees(math.atan(zeus_y/zeus_x))
        if zeus_x < 0 and zeus_y >0 :
            zeus_degrees = zeus_degrees+180
        if zeus_x < 0 and zeus_y <0 :
            zeus_degrees = zeus_degrees-180
        while zeus_degrees < 0:
            zeus_degrees=zeus_degrees+360
        while zeus_degrees > 360:
            zeus_degrees=zeus_degrees-360

        zeus_one = zeus_cl[2]-zeus_degrees
        zeus_two = math.sqrt(math.pow(zeus_x,2)+math.pow(zeus_y,2))
        zeus_three= zeus_degrees-zeus_tl[2]
        print int(zeus_cl[0]),int(zeus_cl[1]),int(zeus_cl[2]),
        print '   ',

    if arg2 !='null':
        hades_tl = [float(arg2[1:4]),float(arg2[5:8]),float(arg2[9:12])]
        hades_cl = getlocation('hades')
        if hades_cl == [-1,-1,-1]:return -1
        hades_x = hades_tl[0]-hades_cl[0]
        hades_y = hades_tl[1]-hades_cl[1]
        hades_degrees = math.degrees(math.atan(hades_y/hades_x))
        if hades_x < 0 and hades_y >0 :
            hades_degrees = hades_degrees+180
        if hades_x < 0 and hades_y <0 :
            hades_degrees = hades_degrees-180
        while hades_degrees < 0:
            hades_degrees=hades_degrees+360
        while hades_degrees > 360:
            hades_degrees=hades_degrees-360

        hades_one = hades_cl[2]-hades_degrees
        hades_two = math.sqrt(math.pow(hades_x,2)+math.pow(hades_y,2))
        hades_three = hades_degrees-hades_tl[2]
        print int(hades_cl[0]),int(hades_cl[1]),int(hades_cl[2]),
        print '   ',

    if arg3 !='null':
        poseidon_tl = [float(arg3[1:4]),float(arg3[5:8]),float(arg3[9:12])]
        poseidon_cl = getlocation('poseidon')
        if poseidon_cl == [-1,-1,-1]:return -1
        poseidon_x = poseidon_tl[0]-poseidon_cl[0]
        poseidon_y = poseidon_tl[1]-poseidon_cl[1]
        poseidon_degrees = math.degrees(math.atan(poseidon_y/poseidon_x))
        if poseidon_x < 0 and poseidon_y >0 :
            poseidon_degrees = poseidon_degrees+180
        if poseidon_x < 0 and poseidon_y <0 :
            poseidon_degrees = poseidon_degrees-180
        while poseidon_degrees < 0:
            poseidon_degrees=poseidon_degrees+360
        while poseidon_degrees > 360:
            poseidon_degrees=poseidon_degrees-360

        poseidon_one = poseidon_cl[2]-poseidon_degrees
        poseidon_two = math.sqrt(math.pow(poseidon_x,2)+math.pow(poseidon_y,2))
        poseidon_three = poseidon_degrees-poseidon_tl[2]
        print int(poseidon_cl[0]),int(poseidon_cl[1]),int(poseidon_cl[2]),
        print '   '

    while arg1 != 'null':
        fzeus = open('/home/pi/zeus/zeus')
        cmd = fzeus.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fzeus.close()
            if zeus_one <=0:
                argument1 = 'd'
                argument2 ='35'
            else: 
                argument1 = 'a'
                argument2 ='47'
            argument3 =abs(zeus_one)/320
            fzeus=open('/home/pi/zeus/zeus',"w")
            fzeus.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fzeus.close()
            break
        else:
            time.sleep(0.1)

    while arg2 != 'null':
        fhades = open('/home/pi/hades/hades')
        cmd = fhades.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fhades.close()
            if hades_one <=0:argument1 = 'd'
            else: argument1 = 'a'
            argument2 ='45'
            argument3 =abs(hades_one)/320
            fhades=open('/home/pi/hades/hades',"w")
            fhades.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fhades.close()
            break
        else:
            time.sleep(0.1)
            fhades.close()

    while arg3 != 'null':
        fposeidon = open('/home/pi/poseidon/poseidon')
        cmd = fposeidon.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fposeidon.close()
            if poseidon_one <=0:
                argument1 = 'd'
                argument2 ='55'
            else:
                argument1 = 'a'
                argument2 ='40'
            argument3 =abs(poseidon_one)/320
            fposeidon=open('/home/pi/poseidon/poseidon',"w")
            fposeidon.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fposeidon.close()
            break
        else:
            time.sleep(0.1)
            fposeidon.close()

    while arg1 != 'null':
        fzeus = open('/home/pi/zeus/zeus')
        cmd = fzeus.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fzeus.close()
            argument1='w'
            argument2 ='50'
            argument3 =zeus_two/155
            fzeus=open('/home/pi/zeus/zeus',"w")
            fzeus.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fzeus.close()
            break
        else:
            time.sleep(0.1)
            fzeus.close()

    while arg2 != 'null':
        fhades = open('/home/pi/hades/hades')
        cmd = fhades.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fhades.close()
            argument1='w'
            argument2 ='50'
            argument3 =hades_two/155
            fhades=open('/home/pi/hades/hades',"w")
            fhades.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fhades.close()
            break
        else:
            time.sleep(0.1)
            fhades.close()

    while arg3 != 'null':
        fposeidon = open('/home/pi/poseidon/poseidon')
        cmd = fposeidon.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fposeidon.close()
            argument1='w'
            argument2 ='50'
            argument3 =poseidon_two/155
            fposeidon=open('/home/pi/poseidon/poseidon',"w")
            fposeidon.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fposeidon.close()
            break
        else:
            time.sleep(0.1)
            fposeidon.close()


    while arg1 != 'null':
        fzeus = open('/home/pi/zeus/zeus')
        cmd = fzeus.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fzeus.close()
            if zeus_three <=0:
                argument1 = 'd'
                argument2 = '35'
            else: 
                argument1 = 'a'
                argument2 = '47'
            argument3 =abs(zeus_three)/320
            fzeus=open('/home/pi/zeus/zeus',"w")
            fzeus.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fzeus.close()
            break
        else:
            time.sleep(0.1)
            fzeus.close()

    while arg2 != 'null':
        fhades = open('/home/pi/hades/hades')
        cmd = fhades.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fhades.close()
            if hades_three <=0:argument1 = 'd'
            else: argument1 = 'a'
            argument2 ='45'
            argument3 =abs(hades_three)/320
            fhades=open('/home/pi/hades/hades',"w")
            fhades.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fhades.close()
            break
        else:
            time.sleep(0.1)
            fhades.close()

    while arg3 != 'null':
        fposeidon = open('/home/pi/poseidon/poseidon')
        cmd = fposeidon.readline()
        if cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a' or cmd=='cmd:done argument1:0 argument2:0 argument3:0':
            fposeidon.close()
            if poseidon_three <=0:
                argument1 = 'd'
                argument2 ='55'
            else: 
                argument1 = 'a'
                argument2 ='40'
            argument3 =abs(poseidon_three)/320
            fposeidon=open('/home/pi/poseidon/poseidon',"w")
            fposeidon.write("cmd:walk argument1:"+argument1+" argument2:"+argument2+" argument3:"+str(argument3)+'\x0a')
            fposeidon.close()
            break
        else:
            time.sleep(0.1)
            fposeidon.close()
    return 0



f=open("/root/Desktop/behaviors")
inloop=0
loopnumber=-1
loop=[]
lines=f.readlines();
f.close()
for line in lines:
    if line.split()[0] == 'loop':
        inloop=1
        loopnumber=int(line.split()[1])
        loop=[]
    elif line.split()[0] == 'pool':
        inloop=0
        if loopnumber == 0:
            while True:
                for i in loop:
                    if i.split()[0] == 'wait':
                        time.sleep(float(i.split()[1]))
                    elif i.split()[0] == 'location':
                        if control_location(i.split()[1],i.split()[2],i.split()[3])!=0:
                            print 'Can\'t find gods\' location '
                            break
                    elif i.split()[0] == 'fan':
                          control_fan(i.split()[1],i.split()[2],i.split()[3])
                    elif i.split()[0] == 'take':
                          control_take(i.split()[1],i.split()[2],i.split()[3])
                    elif i.split()[0] == 'turn':
                          control_turn(i.split()[1],i.split()[2],i.split()[3])
                    elif i.split()[0] == 'led':
                          control_led(i.split()[1],i.split()[2],i.split()[3])
                    else:
                        pass
        for j in range(loopnumber):
            for i in loop:
                if i.split()[0] == 'wait':
                    time.sleep(float(i.split()[1]))
                elif i.split()[0] == 'location':
                    if control_location(i.split()[1],i.split()[2],i.split()[3])!=0:
                        print 'Can\'t find gods\' location '
                        break
                elif i.split()[0] == 'fan':
                    control_fan(i.split()[1],i.split()[2],i.split()[3])
                elif i.split()[0] == 'take':
                    control_take(i.split()[1],i.split()[2],i.split()[3])
                elif i.split()[0] == 'turn':
                    control_turn(i.split()[1],i.split()[2],i.split()[3])
                elif i.split()[0] == 'led':
                    control_led(i.split()[1],i.split()[2],i.split()[3])
                else:
                    pass
        loopnumber=-1
        loop=[]
    elif inloop != 0:
        loop.append(line)

    else:
        if line.split()[0] == 'wait':
            time.sleep(float(line.split()[1]))
        elif line.split()[0] == 'location':
            if control_location(line.split()[1],line.split()[2],line.split()[3])!=0:
                print 'Can\'t find gods\' location '
                break
        elif line.split()[0] == 'fan':
            control_fan(line.split()[1],line.split()[2],line.split()[3])
        elif line.split()[0] == 'take':
            control_take(line.split()[1],line.split()[2],line.split()[3])
        elif line.split()[0] == 'turn':
            control_turn(line.split()[1],line.split()[2],line.split()[3])
        elif line.split()[0] == 'led':
            control_led(line.split()[1],line.split()[2],line.split()[3])
        else:
            pass