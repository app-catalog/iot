import serial
import json 
f=open('input', 'w')
g=open('out', 'w')
ser = serial.Serial('/dev/ttyACM0', 9600)
x=ser.read(50)
f.write(x)
json.dump(x,g)
f.close()
