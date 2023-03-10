import json
from flask import Flask, Response

app = Flask(__name__)
@app.route('/alkuluku/<luku>')

def onkoAlkuluku(luku):
    try:
        luku = int(luku)
        for i in range(2, int(luku/2)+ 1):
            if luku%i == 0:
                response = {
                    "Number" : luku,
                    "IsPrime" : "false"
                }
                json_response = json.dumps(response)
                http_response = Response(response=json_response, status=200, mimetype="application/json")
                return http_response
            else:
                response = {
                    "Number" : luku,
                    "IsPrime" : "true"
                }
                json_response = json.dumps(response)
                http_response = Response(response=json_response, status=200, mimetype="application/json")
                return http_response

    except ValueError:
        response = {
            "message" : "not a number",
            "status" : 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response
@app.errorhandler(404)
def pageNotFound(error_code):
    response = {
        "message":"invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)