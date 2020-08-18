#coding=utf-8
import json

def getAddCompanyJSON(arr):
    s =  {
			"cid": None,
			"cname": None
    }

    s["cid"] = arr[0]
    s["cname"] = arr[1]
    return s

def getAttendJSON(arr):
    s =  {
            "month": None
    }

    s["month"] = arr[0]
    return s

def getCheckJSON(arr):
    s =  {
        "picture": None,
        "time":None,
        "isLate": None,
        "isEarly": None,
        "isAbsent": None,
        "stage":None,
        "isFirst":None
    }

    s["picture"] = arr[0]
    s["time"] = arr[1]
    s["isLate"] = arr[2]
    s["isEarly"] = arr[3]
    s["isAbsent"] = arr[4]
    s["stage"]=arr[5]
    s["isFirst"]=arr[6]

    return s


def getLeaveJSON(arr):
    s =  {
            "type": None,
            "Off_Tim":None,
            "Offend_Tim": None,
            "describe":None
        }

    s["type"] = arr[0]
    s["Off_Tim"] = arr[1]
    s["Offend_Tim"] = arr[2]
    s["describe"] = arr[3]
    return s

def getLoginJSON(arr):
    s = {
        "username": None,
        "passwprd": None,
    }

    s["username"] = arr[0]
    s["passwprd"] = arr[1]

    return s

def getModifyJSON(arr):
    s = {
            "name": None,
            "sex": None,
            "birth": None
        }

    s["name"] = arr[0]
    s["sex"] = arr[1]
    s["birth"] = arr[2]

    return s

def getRegisterJSON(arr):
    s = {
            "username": None,
            "password": None,
            "email": None
        }

    s["username"] = arr[0]
    s["password"] = arr[1]
    s["email"] = arr[2]
    return s

def getMessageJSON(arr):
    s = {
        "id": None,
        "type": None,
        "proc": None
    }

    s["id"] = arr[0]
    s["type"] = arr[1]
    s["proc"] = arr[2]
    return s
