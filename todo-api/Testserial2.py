import serial
import json 
f=open('output.txt', 'w')
g=open('arq.txt', 'w')
ser = serial.Serial('/dev/ttyACM0', 9600)
x=ser.read(50)
f.write(x)
json.dump(x,g)
f.close()
