import pymysql.cursors
# 连接数据库
connect = pymysql.connect("localhost","root","12345678","attendsystem" )

# 获取游标
cursor = connect.cursor()

#<editor-fold desc="增加">
def insertIntoDatabase(firstList,lastList,tablename):
    if(len(firstList)!=len(lastList)):
        print("insertIntoDatabase输入参数错误")
        return
    s=""
    r=""
    for index in range(len(firstList)):
        if index == 0:
            s = firstList[0]
            r = lastList[0]
        else:
            s = s + "," + firstList[index]
            r = r + "," + lastList[index]
    sql = "INSERT INTO "+tablename+" ("+s+") VALUES ("+r+");"
    print(sql)

    cursor.execute(sql)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')

def testInsert():
    firstList=["c_id","U_id","U_name","password","sex","age","birth","phone","adress"]
    lastList=["\"01\"","\"1\"","\"3\"","\"4\"","\"5\"", "20", "\"1998-01-01\"", "\"8\"","\"9\""]
    insertIntoDatabase(firstList,lastList,"User")
#testInsert()

#</editor-fold>

#<editor-fold desc="删除">
def deleteFromDatabase(firstIndex,lastIndex,tableName):
    if(len(firstIndex)!=len(lastIndex)):
        print("deleteFromDatabase输入参数错误")
        return

    for index in range(len(firstIndex)):
        r = firstIndex[index] + "=" + lastIndex[index]
        if index != (len(firstIndex) - 1):
            r = r + " and "
    sql = "DELETE FROM "+ tableName +" WHERE "+ r + ";"
    cursor.execute(sql)
    connect.commit()
    print('成功删除', cursor.rowcount, '条数据')

def testDelete():
    firstIndex = ["c_id"]  # 根据此表项查找
    lastIndex = ["\"01\""]  # 对应上表项的指
    deleteFromDatabase(firstIndex,lastIndex,"user")


#</editor-fold>

#<editor-fold desc="修改">
def modifyDatabase(firstList,lastList,firstIndex,lastIndex,tableName):
    if (len(firstIndex) != len(lastIndex) )| (len(firstList) != len(lastList)):
        print("modifyDatabase输入参数错误")
        return
    r=""
    s=""
    for index in range(len(firstList)):
        r = r + firstList[index] + "=\"" + lastList[index] +"\""
        if index != (len(firstList) - 1):
            r = r + " , "

    for index in range(len(firstIndex)):
        s = s + firstIndex[index] + "=\"" + lastIndex[index] +"\""
        if index != (len(firstIndex) - 1):
            s = s + " and "

    sql = "UPDATE " + tableName + " SET " + r + " WHERE " + s +";"
    print(sql)
    cursor.execute(sql)
    connect.commit()
    print('成功修改', cursor.rowcount, '条数据')

def testModify():
    firstIndex=["u_id","c_id"]
    lastIndex=["2","02"]
    firstList=["U_name","sex"]
    lastList=["小明","男"]
    modifyDatabase(firstList,lastList,firstIndex,lastIndex,"User")

#</editor-fold>

#<editor-fold desc="查询">
def findInDatabase(findList,firstIndex,lastIndex,tableName):
    if(len(firstIndex)!=len(lastIndex)):
        print("findInDatabase输入参数错误")
        return
    s = ""
    r = ""

    for item in findList:
        if len(s) == 0:
            s = item
        else:
            s = s + "," + item

    for index in range(len(firstIndex)):
        r = r + firstIndex[index] + "=" + lastIndex[index]
        if index != (len(firstIndex)-1):
            r = r + " and "

    sql = "SELECT "+ s +" FROM "+tableName + " WHERE " + r + ";"
    #print(sql)
    cursor.execute(sql)

    s = s.replace(",",":%s  ") + ":%s"
    returnList=[]
    for row in cursor.fetchall():
        print(s % row)
        returnList.append(row)
    print('共查找出', cursor.rowcount, '条数据')
    return returnList


def testFind():
    findList = ["u_name","u_id", "age"]    #要获取的表项
    firstIndex = ["c_id","u_id"]   #根据此表项查找
    lastIndex = ["\"02\"","1"]  #对应上表项的指
    s = findInDatabase(findList,firstIndex,lastIndex,"user")
    for row in s:
        for index in range(len(findList)):
            print(row[index])

# testFind()

#</editor-fold>