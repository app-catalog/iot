import serial
import json
import time
#f=open('output.txt', 'w')
#g=open('arq.txt', 'w')
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1:
    x=ser.readline()
    print x
#time.sleep(0.5)
#f.write(x)
#json.dump(x,g)
#f.close()
