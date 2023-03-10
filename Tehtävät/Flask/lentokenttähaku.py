import json
from flask import Flask, Response
import mysql.connector
def getName(icao):
    sql = f"select name from airport where ident = '{icao}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]
def getMunicipality(icao):
    sql = f"select municipality from airport where ident = '{icao}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]
yhteys = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="matkalippupeli",
         user="root",
         password="1234",
         autocommit=True
         )
app = Flask(__name__)
@app.route("/kenttä/<icao>")


def run(icao):
    try:
        response = {
            "ICAO" : icao,
            "Name" : getName(icao),
            "Municipality": getMunicipality(icao)
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=200, mimetype="application/json")
        return http_response
    except :
        response = {
            "message": "invalid ICAO",
            "status": 400
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