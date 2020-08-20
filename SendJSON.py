#coding=utf-8
import json

def getAddCompanyJSON(arr):
    s =  {
	"cid": None,
	"cname": None,
    "applytime": None,
    "read":None,
    "proc":None
    }


    s["cid"] = arr[0]
    s["cname"] = arr[1]
    s["applytime"]=arr[2]
    s["read"]=arr[3]
    s["proc"]=arr[4]
    return s

def getAttendJSON(arr):
    s =  {
            "Mid": None
    }

    s["Mid"] = arr[0]
    return s

def getCheckJSON(arr):
    s =  {
        "pic": None,
        "type":None,
        "isFirst":None
    }

    s["pic"] = arr[0]
    s["type"] = arr[1]
    s["isFirst"] = arr[2]
    return s


def getLeaveJSON(arr):
    s =  {
        "starttime": None,
        "endtime": None,
        "proc": None,
        "type": None,
        "applytime": None,
        "Offday":None,
        "desc": None,

    }

    s["starttime"] = arr[0]
    s["endtime"] = arr[1]
    s["proc"] = arr[2]
    s["type"] = arr[3]
    s["applytime"] = arr[4]
    s["Offday"] = arr[5]
    s["desc"] = arr[6]
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
            "account": None,
            "secret": None,
        "nickname":None,
        "type":None
        }

    s["account"] = arr[0]
    s["secret"] = arr[1]
    s["nickname"]=arr[2]
    s["type"]=arr[3]
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

def getLoginJSON(arr):
    s={
        "account":None,
        "scret":None,
        "type":None
    }
    s["account"] = arr[0]
    s["secret"] = arr[1]
    s["type"] = arr[2]
    return s

