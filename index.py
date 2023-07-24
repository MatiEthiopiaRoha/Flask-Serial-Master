from flask import Flask,Response,request, jsonify
import datetime
import time
import logging as logger
import serial

logger.basicConfig(level="DEBUG")


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

app = Flask(__name__)


# ser = serial.Serial('COM3')
#ser.flush()
time_now = datetime.datetime.now()
@app.route('/')
def home():
    return '''SERIAL API MASTER
'''



@app.route('/status', methods=['POST'])
def status():
     data = 'Server Status Ok'
     return Response(data, mimetype='application/json')
     



# main driver function
if __name__ == '__main__':

    logger.debug("Server Starting ")
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)