from flask import Flask,request, jsonify
import time
import logging as logger

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


@app.route('/')
def home():
    return '''SERIAL API MASTER
'''



@app.route('/head', methods=['POST'])
def head():
    req = request.get_json()
    dpt = req['dpt']
    ip = req['ip']
  
    # p = escpos.printer.Network(ip, port=9100)

    # print(ip)

    
    # p.text(color.BOLD + "THE BRICK HOUSE \t " + ip + color.END + "\n \n")
    # p.text("item" + " \t" +  "Quantity\n")
    # p.close()

    return ''



# main driver function
if __name__ == '__main__':

    logger.debug("Server Starting ")
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)