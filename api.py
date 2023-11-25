import subprocess
import os
from flask import Flask
app = Flask(__name__)

@app.route('/search/<val>', methods=['GET'])
def search(val):
    file = open("/app/text", "r")
    lines = file.readlines()
    file.close()
    result_dict = {}
    for line in lines:
        key,value = line.split(',')[0] , line.strip().split(',')[-1]
        result_dict[key] = value
    try:
        return result_dict[val]
    except KeyError:
        return "Not Found"

@app.route('/',methods=['GET'])
def size():
    result = os.popen('du -sh /opt')
    return str(result.read().split('\t')[0])
if __name__ == '__main__':
     app.run(host='0.0.0.0',port=105)