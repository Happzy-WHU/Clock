#coding=utf-8
from flask import request, Flask
import base64
import cv2
import numpy as np
import datetime
import time
import os.path
import Compare

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

count = 0
def getPicName():
    global count
    count += 1
    if count>=1000:
        count=0
    t = datetime.datetime.now()
    s = t.strftime("%Y%m%d%H%M%S")
    return s+str(count)+'.jpg'

def JudgeOnePerson(UID, pic_name):
    if not os.path.isfile("User/"+UID+".jpg"):
        return "0"

    argv=[]
    argv.append("Model")
    argv.append("User/"+UID+".jpg")
    argv.append("tem/"+pic_name)
    if Compare.main(Compare.parse_arguments(argv))==True:
        return "1"
    else:
        return "0"


@app.route("/upload_pic", methods=['POST','GET'])
def get_frame():
    #解析图片数据
    img = base64.b64decode(str(request.form['image']))
    image_data = np.fromstring(img, np.uint8)
    image_data = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    pic_name = getPicName()
    cv2.imwrite('tem/'+pic_name, image_data)
    print("收到图片")
    return JudgeOnePerson(str(request.form['UID']),pic_name)

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)