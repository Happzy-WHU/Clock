#coding=utf-8
import json
import DataBaseOperation
import Administrator
import User
import CJsonEncoder

userData = [{
    'U_Id' : "2",
    'Password' : "4"
}
]
adData = [{
    "A_Id" : "1",
    "Password" : "1"
}]

userJSON = json.dumps(userData)
adJSON = json.dumps(adData)

def userLogin():
    user_dic = json.loads(userJSON)

    findList = ["C_Id","U_Id","U_Name","Password","Sex","Age","Birth","Phone","Adress"]  # 要获取的表项
    firstIndex = ["U_ID","Password"]  # 根据此表项查找
    lastIndex = [user_dic[0]['U_Id'],user_dic[0]['Password']]  # 对应上表项的指

    s = DataBaseOperation.findInDatabase(findList, firstIndex, lastIndex, "user")
    if len(s) == 0:
        return
    for row in s:
       j1 = json.dumps(User.User(row).__dict__,
            ensure_ascii = False, sort_keys = True, indent = 4, cls = CJsonEncoder.CJsonEncoder)
    return j1

def adLogin():
    ad_dic = json.loads(adJSON)

    findList = ["C_Id","A_Id","A_Name","Password","Sex","Age","Birth","Phone","Adress"]  # 要获取的表项
    firstIndex = ["A_Id", "Password"]  # 根据此表项查找
    lastIndex = [ad_dic[0]['A_Id'], ad_dic[0]['Password']]  # 对应上表项的指

    s = DataBaseOperation.findInDatabase(findList, firstIndex, lastIndex, "administrator")

    if len(s)==0:
        return
    for row in s:
        if row[6] != None:
            row[6] = row[6].strftime('%Y-%m-%d %H:%M:%S')
        j1 = json.dumps(Administrator.Admin(row).__dict__
                        ,ensure_ascii=False,sort_keys=True, indent=4,cls=CJsonEncoder.CJsonEncoder)
    return j1


userLogin()
adLogin()