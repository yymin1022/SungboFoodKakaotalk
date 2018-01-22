import os
import parse

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["오늘중식", "오늘석식"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"오늘중식":
        returnValue = parse.lunch()
        dataSend = {
            "message": {
                "text": returnValue
            },
            "keyboard": {
                "type" : "buttons",
        	"buttons" : ["오늘중식", "오늘석식"]
            }
        }
    elif content == u"오늘석식":
        returnValue = parse.dinner()
        dataSend = {
            "message": {
                "text": returnValue
            },
            "keyboard": {
                "type" : "buttons",
        	"buttons" : ["오늘중식", "오늘석식"]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
