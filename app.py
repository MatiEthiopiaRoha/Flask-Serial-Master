from flask import *
import datetime
import time
import logging as logger
import serial
import random
from flask_session import *


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


app = Flask(__name__,static_folder='static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)




@app.route('/index', methods=['POST'])
def setup():
       req = request.get_json()
       port = req['port']
       baudrate = req['baudrate']
       print(port)
       print(baudrate)
       ser = serial.Serial()
       ser.baudrate = 9600
       ser.port = 'COM4'
       ser.open()
       print(ser.is_open)

       while 1:
              line = ser.readline()
              output = line.decode()
              print(output)
       return render_template('index.html')


       
       
       
       
       
       
# main driver function
if __name__ == '__main__':

    logger.debug("Server Starting ")
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)