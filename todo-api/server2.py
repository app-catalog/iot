import serial
import json
from flask import Flask, request


app = Flask(__name__)

#@app.route('/todo/api/v1.0/project')
@app.route("/")

def get_project():
    return json.dump(serial.Serial('/dev/tty/ACM0',9600))
    #return time.ctime()
                     
if __name__ == "__main__" :
    app.run(port=5000, debug=True, host='0.0.0.0')


