#coding=utf-8
import requests
import base64
#将图片数据转成base64格式
with open('User/5.jpg', 'rb') as f:
    img = base64.b64encode(f.read()).decode()
image = []
image.append(img)
res = {"pic":image,"uid":"5"}
#访问服务
_ = requests.post("http://127.0.0.1:5000/upload_pic",data=res)
print(_.json())