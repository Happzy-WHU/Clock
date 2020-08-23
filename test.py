#coding=utf-8
from flask import request, Flask
import base64
import cv2
import numpy as np
import datetime
import time
import os.path


app = Flask(__name__)


@app.route('/v1/modify',methods=["post","get"])
def f1():
    print(request.get_json())
    return {"msg":"ok"}

@app.route('/v1/register',methods=["post","get"])
def f2():
    print(request.get_json())
    return {"msg":"ok"}

@app.route('/v1/off/off_apply',methods=["post","get"])
def f3():
    print(request.get_json())
    return {"msg":"ok"}

@app.route('/v1/check',methods=["post","get"])
def f4():
    print(request.get_json())
    return {"msg":"ok"}

@app.route('/v1/attend',methods=["post","get"])
def f5():
    print(request.get_json())
    return {"msg":"ok"}

@app.route('/v1/addCompany',methods=["post","get"])
def f6():
    print(request.get_json())
    return {"msg":"ok"}

@app.route('/v1/info',methods=["post","get"])
def f7():
    print(request.get_json())
    return {"uid":"3232","name":"zs","sex":"男","birth":"2000-05-16"}

@app.route('/v1/messages',methods=["post","get"])
def f8():
    print(request.get_json())
    return {
    "apply": [
        {
            "applytime": "2020-08-17 00:00:00",
            "cid": 1,
            "id": 1,
            "process": 1,
            "read": 1,
            "uid": 2,
            "cname":"武汉大学"
        }
    ],
    "invite": [
        {
            "aemail": "ss",
            "cid": 1,
            "cname": "武汉大学",
            "id": 1,
            "invitetime": "2020-08-12 00:00:00",
            "process": 1,
            "read": 1,
            "uemail": "4"
        }
    ],
    "msg": [
        {
            "id": 1,
            "postmessage": "123",
            "process": 1,
            "read": 1,
            "sendtime": "2020-07-07 00:00:00",
            "touid": 2,
            "type": "1"
        }
    ]
}

@app.route('/v1/read',methods=["post","get"])
def f9():
    print(request.get_json())
    return {"msg":"ok"}

@app.route('/v1/token',methods=["post","get"])
def f10():
    print(request.get_json())
    return {"msg":"ok"}
# @app.route('/v1/info',methods=["post","get"])
# def f7():
#     print(request.get_json())
#     return {"msg":"ok"}

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)