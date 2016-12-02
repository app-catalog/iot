import serial
import json 

from flask import Flask, jsonify

app = Flask(__name__)

#project = open('out','r')
#x=project.read()

#@app.route('/todo/api/v1.0/project', methods=['GET'])
@app.route("/", methods=['GET'])

def get_project():
    #return jsonify({'project': project})
    ser = serial.Serial('/dev/ttyACM0', 9600)
    
    

    x=ser.read(50).strip
    
    return y

if __name__ == '__main__' :
    app.run(port=5000,debug=True, host='0.0.0.0')
    
