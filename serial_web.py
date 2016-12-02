import flask
import serial
from time import sleep

app = flask.Flask(__name__)
app.debug = True

def event_barcodecliente():
    messageid = 0
    ser = serial.Serial('/dev/ttyACM0', 9600)
    #ser.port = 0
    #ser.baudrate = 9600
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 0
    try:
        ser.open()
    except serial.SerialException, e:
         yield 'event:error\n' + 'data:' + 'Serial port error({0}): {1}\n\n'.format(e.errno, e.strerror)
         messageid = messageid + 1
    str_list = []
    while True:
        sleep(0.01)
        nextchar = ser.read()
        if nextchar:
            str_list.append(nextchar)
        else:
            if len(str_list) > 0:
                yield 'id:' + str(messageid) + '\n' + 'data:' + ''.join(str_list) + '\n\n'
                messageid = messageid + 1
                str_list = []

@app.route('/barcodecliente')
def barcodecliente():
    newresponse = flask.Response(event_barcodecliente(), mimetype="text/event-stream")
    newresponse.headers.add('Access-Control-Allow-Origin', '*')
    newresponse.headers.add('Cache-Control', 'no-cache')
    return newresponse

if __name__ == '__main__':
    app.run(port=5000, threaded=True)
