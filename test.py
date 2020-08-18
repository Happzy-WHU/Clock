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

@app.route('/v1/leave',methods=["post","get"])
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

# @app.route('/v1/info',methods=["post","get"])
# def f7():
#     print(request.get_json())
#     return {"msg":"ok"}

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)