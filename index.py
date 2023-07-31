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

@app.route('/')
def home():
    return render_template('setup.html')


@app.route('/status', methods=['GET'])
def status():
     data = 'Server Status Ok'
     return Response(data, mimetype='application/json')
     

@app.route('/connect', methods=['POST'])
def connect():
    req = request.get_json()
    port = req['port']
    baudrate = req['baudrate']
    session["port"] = req['port']
    session["baudrate"] = req['baudrate']
    try:
        time_now = datetime.datetime.now()
        # ser = serial.Serial(port)
        # ser.flush()
        # ser.baudrate = baudrate
        # ser.open()
        ser = serial.Serial(
        # Serial Port to read the data from
        port=port,
        #Rate at which the information is shared to the communication channel
        baudrate = baudrate,
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
        # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
        # Number of serial commands to accept before timing out
        timeout=1
        )
        ser.open()
        if ser.is_open == True:
            #  return 'CONNECTED' 
             return render_template("index.html")            
    except:
        msg = "Not Connected to \t" + port
        print(color.RED + "Something went wrong " + color.END + "\n")
    finally:
        print(color.BLUE + "Operation finished \t ")
      
    # return 'DISCONNECTED'
    return render_template("index.html")            




@app.route('/get-data', methods=['POST'])
def get_data():
    port = session["port"]
    baudrate = session['baudrate']
    
    msg = ""
    temperature = str(random.randrange(1,100))
    humidity = str(random.randrange(1,100))
    moisture = str(random.randrange(1,100))
    print(type(temperature))
    muck = temperature + "," + humidity + "," + moisture
    print(color.BOLD + "Arduino Serial Master\t " + port  + color.END + "\n")
    try:
        time_now = datetime.datetime.now()
        # ser = serial.Serial(port)
        # ser.flush()
        # ser.baudrate = baudrate
        # ser.open()
        ser = serial.Serial(
        # Serial Port to read the data from
        port=port,
        #Rate at which the information is shared to the communication channel
        baudrate = baudrate,
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
        # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
        # Number of serial commands to accept before timing out
        timeout=1
        )
        ser.open()
        if ser.is_open == True:
            while 1:
                data = ser.readline()
                print(data)
            print(color.GREEN + "Arduino PORT:\t " + port + color.END + "Time" + time_now + "\n")
        elif ser.is_open == False:
            print(color.CYAN +  "PORT Closed:\t  " + port + color.END + "Time" + time_now + "\n")                
    except:
        msg = "Not Connected to \t" + port 
        print(color.RED + "Something went wrong " + msg + color.END + "\n")
    finally:
        print(color.BLUE + "Operation finished \t ")
    return muck



@app.route('/start-motor', methods=['POST'])
def start_motor():
    port = session["port"]
    baudrate = session['baudrate']
    try:
        time_now = datetime.datetime.now()
        # ser = serial.Serial(port)
        # ser.flush()
        # ser.baudrate = baudrate
        # ser.open()
        ser = serial.Serial(
        # Serial Port to read the data from
        port=port,
        #Rate at which the information is shared to the communication channel
        baudrate = baudrate,
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
        # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
        # Number of serial commands to accept before timing out
        timeout=1
        )
        ser.open()
        if ser.is_open == True:
             ser.write("HIGH".encode())
             return 'CONNECTED' 
            #  return render_template("index.html")            
    except:
        msg = "Not Connected to \t" + port
        print(color.RED + "Something went wrong " + color.END + "\n")
    finally:
        print(color.BLUE + "Operation finished \t ")
      
    return 'HIGH'
    # return render_template("index.html")            


@app.route('/stop-motor', methods=['POST'])
def stop_motor():
    port = session["port"]
    baudrate = session['baudrate']
    try:
        time_now = datetime.datetime.now()
        # ser = serial.Serial(port)
        # ser.flush()
        # ser.baudrate = baudrate
        # ser.open()
        ser = serial.Serial(
        # Serial Port to read the data from
        port=port,
        #Rate at which the information is shared to the communication channel
        baudrate = baudrate,
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
        # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
        # Number of serial commands to accept before timing out
        timeout=1
        )
        ser.open()
        if ser.is_open == True:
             ser.write("LOW".encode())
             return 'CONNECTED' 
            #  return render_template("index.html")            
    except:
        msg = "Not Connected to \t" + port
        print(color.RED + "Something went wrong " + color.END + "\n")
    finally:
        print(color.BLUE + "Operation finished \t ")
      
    return 'LOW'
    # return render_template("index.html")            





@app.route('/application')
def application():
   return render_template('index.html')



@app.route('/map')
def map():
   return render_template('map.html')


@app.route('/chart')
def chart():
   return render_template('chart.html')


@app.route('/setup')
def setup():
   return render_template('setup.html')




# main driver function
if __name__ == '__main__':

    logger.debug("Server Starting ")
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)