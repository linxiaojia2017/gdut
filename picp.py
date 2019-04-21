#!/usr/bin/python
from PIL import Image
import os
import sys
import time

while 1:
    f=open('/home/pi/'+sys.argv[1]+'/'+sys.argv[1])
    cmd=f.readline()
    f.close()
    if cmd=='cmd:done argument1:0 argument2:0 argument3:0' or cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a':
        break
    else:
        time.sleep(0.1)
os.system('echo cmd:led argument1:l argument2:r argument3:f > /home/pi/'+sys.argv[1]+'/'+sys.argv[1])
while 1:
    f=open('/home/pi/'+sys.argv[1]+'/'+sys.argv[1])
    cmd=f.readline()
    f.close()
    if cmd=='cmd:done argument1:0 argument2:0 argument3:0' or cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a':
        break
    else:
        time.sleep(0.1)
os.system("sudo raspistill -o testred.jpg -w 400 -h 400 -t 250")
while 1:
    f=open('/home/pi/'+sys.argv[1]+'/'+sys.argv[1])
    cmd=f.readline()
    f.close()
    if cmd=='cmd:done argument1:0 argument2:0 argument3:0' or cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a':
        break
    else:
        time.sleep(0.1)
os.system('echo cmd:led argument1:l argument2:f argument3:f > /home/pi/'+sys.argv[1]+'/'+sys.argv[1])
while 1:
    f=open('/home/pi/'+sys.argv[1]+'/'+sys.argv[1])
    cmd=f.readline()
    f.close()
    if cmd=='cmd:done argument1:0 argument2:0 argument3:0' or cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a':
        break
    else:
        time.sleep(0.1)

img1 = Image.open('testred.jpg')

Img1 = img1.convert('L')
Img1.save("testred1.jpg")

threshold1 = 230
table1 = []
for i in range(256):
    if i < threshold1:
        table1.append(0)
    else:
        table1.append(1)
photo1 = Img1.point(table1, '1')
photo1.save("red.jpg")

while 1:
    f=open('/home/pi/'+sys.argv[1]+'/'+sys.argv[1])
    cmd=f.readline()
    f.close()
    if cmd=='cmd:done argument1:0 argument2:0 argument3:0' or cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a':
        break
    else:
        time.sleep(0.1)
os.system('echo cmd:led argument1:l argument2:f argument3:b > /home/pi/'+sys.argv[1]+'/'+sys.argv[1])

while 1:
    f=open('/home/pi/'+sys.argv[1]+'/'+sys.argv[1])
    cmd=f.readline()
    f.close()
    if cmd=='cmd:done argument1:0 argument2:0 argument3:0' or cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a':
        break
    else:
        time.sleep(0.1)

os.system("sudo raspistill -o testblue.jpg -w 400 -h 400 -t 250")
img2 = Image.open('testblue.jpg')

while 1:
    f=open('/home/pi/'+sys.argv[1]+'/'+sys.argv[1])
    cmd=f.readline()
    f.close()
    if cmd=='cmd:done argument1:0 argument2:0 argument3:0' or cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a':
        break
    else:
        time.sleep(0.1)
os.system('echo cmd:led argument1:l argument2:f argument3:f > /home/pi/'+sys.argv[1]+'/'+sys.argv[1])

while 1:
    f=open('/home/pi/'+sys.argv[1]+'/'+sys.argv[1])
    cmd=f.readline()
    f.close()
    if cmd=='cmd:done argument1:0 argument2:0 argument3:0' or cmd=='cmd:done argument1:0 argument2:0 argument3:0\x0a':
        break
    else:
        time.sleep(0.1)
Img2 = img2.convert('L')
Img2.save("testblue1.jpg")

threshold2 = 230
table2 = []
for i in range(256):
    if i < threshold2:
        table2.append(0)
    else:
        table2.append(1)
photo2 = Img2.point(table2, '1')
photo2.save("blue.jpg")
