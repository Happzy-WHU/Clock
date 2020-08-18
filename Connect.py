import requests
import json
def sendJSON(portname,data):
    url="http://127.0.0.1:5000/v1"+portname
    response=requests.post(url, json=data)
    return response.json()

