import requests
from requests.auth import HTTPBasicAuth
import json
import os
def sendJSON(portname,data):
    url="http://175.24.118.43:5000/v1"+portname
    with open("token") as f:
        s = f.read()
        try:
            if portname=="/token":
                response=requests.post(url, json=data)
            if portname=="/client/register" or portname == "/message/userdeal_message" or portname == "/attendance/clock" or portname == "/modify":
                response=requests.post(url, auth = HTTPBasicAuth(s,''),json=data)
            if portname=="/message/usershow_message":
                response = requests.post(url, auth=HTTPBasicAuth(s, ''))

            if portname=="/monthsta/monthstaquery" or portname == "/apply/orguseradd" or portname == "/off/off_apply":
                response = requests.get(url, auth=HTTPBasicAuth(s, ''),json=data)
            if portname=="/user":
                response = requests.get(url, auth=HTTPBasicAuth(s, ''))
        except requests.exceptions.ConnectionError:
            return None
        f.close()


    print(response.status_code)
    if response.status_code>=200 and response.status_code<300:
        return response.json()
    else:
        return None

