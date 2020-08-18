#coding=utf-8
from datetime import datetime,date
class ApplyMessage:
    def __init__(self,mes):
        self.time = mes["applytime"]
        self.hasRead = mes["read"]
        self.status = mes["process"]
        #cname空着
        self.cname = mes["cname"]
        self.mid=mes["id"]

    time=""
    hasRead=0
    mid=0

    cname=""
    status=0

class InviteMessage:
    def __init__(self,mes):
        self.time = mes["invitetime"]
        self.cid = mes["cid"]
        self.hasRead = mes["read"]
        self.cname = mes["cname"]
        self.mid=mes["id"]


    time = ""
    hasRead = 0
    mid=0

    cid=""
    cname=""
    status=0
    content="   我们公司正在招聘人才欢迎你加入我们公司！"

class NormalMessage:
    def __init__(self,mes):
        self.time = mes["sendtime"]
        self.hasRead = mes["read"]
        self.content = mes["postmessage"]
        self.mid=mes["id"]

    time = ""
    hasRead = 0
    mid=0

    content=""

def getApplyMessage(arr):
    ret=[]
    for o in arr:
        ret.append(ApplyMessage(o))
    return ret

def getInviteMessage(arr):
    ret = []
    for o in arr:
        ret.append(InviteMessage(o))
    return ret

def getNormalMessage(arr):
    ret = []
    for o in arr:
        ret.append(NormalMessage(o))
    return ret

def foreNew(str1,str2):

    str1 = datetime.strptime(str1,"%Y-%m-%d %H:%M:%S")
    str2 = datetime.strptime(str2,"%Y-%m-%d %H:%M:%S")
    if (str1-str2).days >= -0:
        return True
    else:
        return False


def sortArr(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if foreNew(arr[i].time,arr[j].time)!=True:
                tem =arr[i]
                arr[i]=arr[j]
                arr[j]=tem

    return arr

def sortMessages(arr):
    arr1=[]
    arr2=[]
    print(arr)
    for i in range(len(arr)):
        if arr[i].hasRead==1:
            arr2.append(arr[i])
        else:
            arr1.append(arr[i])

    arr1=sortArr(arr1)
    arr2=sortArr(arr2)
    arr1.extend(arr2)
    return arr1
