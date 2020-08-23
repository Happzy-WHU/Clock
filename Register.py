# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import QRect,QMetaObject,QCoreApplication,QSize
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QFrame,QLabel,QPushButton,QLineEdit,QErrorMessage,QToolButton


# from src import Login
from src import resources,Connect,SendJSON

class Ui_Register(object):
    def __init__(self, WidgetStack, UIStack):
        self.WidgetStack = WidgetStack
        self.UIStack = UIStack

    WidgetStack = None
    UIStack = None

    hasShow = True


    

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1013, 772)
        Form.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"}\n"
"#Form{ \n"
"    background: url(:/resources/background.jpg);\n"
"}\n"
"\n"
"QFrame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QToolButton{\n"
"background:#49ebff;\n"
"border-radius:60px;\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"QPushButton{\n"
"background:#49ebff;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"background:white;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}"
"QErrorMessage{\n"
"color:red;\n"
"}\n"
                           )
        self.frame = QFrame(Form)
        self.frame.setGeometry(QRect(240, 120, 491, 521))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setGeometry(QRect(100, 140, 301, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(160, 50, 191, 41))
        self.label.setObjectName("label")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QRect(100, 240, 301, 31))
        self.lineEdit_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QRect(100, 320, 301, 41))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(30, 440, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setGeometry(QRect(280, 440, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.toolButton = QToolButton(Form)
        self.toolButton.setGeometry(QRect(420, 30, 131, 121))
        self.toolButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/resources/people.png"), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(64, 64))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "智慧考勤"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.label.setText(_translate("Form", "请输入个人信息"))
        self.lineEdit_2.setText(_translate("Form", ""))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Passwoed"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Email Address"))
        self.pushButton.setText(_translate("Form", "注 册"))
        self.pushButton_2.setText(_translate("Form", "返 回"))

        self.pushButton_2.clicked.connect(lambda: self.onPushButton_2Click())
        self.pushButton.clicked.connect(lambda :self.onPushButton_Click())

        self.lineEdit_2.textChanged.connect(self.textChanged2)
        self.lineEdit_6.textChanged.connect(self.textChanged6)
        self.lineEdit.textChanged.connect(self.textChanged)

        #self.pushButton_2.clicked.connect(lambda: self.onPushButtonClick()) #注册接口

    def textChanged2(self, text):
        self.lineEdit_2.setText(text)
    def textChanged6(self, text):
        self.lineEdit_6.setText(text)
    def textChanged(self, text):
        self.lineEdit.setText(text)

    def onPushButton_Click(self):
        arr=[]
        arr.append(self.lineEdit_6.text())
        arr.append(self.lineEdit_2.text())
        arr.append(self.lineEdit.text())
        arr.append(100)
        print(SendJSON.getRegisterJSON(arr))
        res = Connect.sendJSON("/client/register",SendJSON.getRegisterJSON(arr))
        if res==None:
            self.hasShow = not self.hasShow
            if self.hasShow == False:
                err = QErrorMessage(self.frame)
                err.setStyleSheet("color:#880000;background:white;")
                err.showMessage("注册失败！")
            return
        if res["msg"]=="ok":
            self.hasShow = not self.hasShow
            if self.hasShow == False:
                err = QErrorMessage(self.frame)
                err.setStyleSheet("color:green;background:white;")
                err.showMessage("注册成功！")


    def onPushButton_2Click(self):
        self.jumpToLogin()

    def jumpToLogin(self):
        hasFind = False
        import src.Login
        self.WidgetStack[3].hide()
        for ui in self.UIStack:
            print(ui.__class__.__name__)
            if ui.__class__.__name__ == "Ui_Login":
                ui.setupUi(self.WidgetStack[1])
                ui.retranslateUi(self.WidgetStack[1])
                hasFind = True
        if hasFind == False:
            newUi = src.Login.Ui_Login(self.WidgetStack, self.UIStack)
            newUi.setupUi(self.WidgetStack[1])
            newUi.retranslateUi(self.WidgetStack[1])
            self.UIStack.append(newUi)
        self.WidgetStack[1].show()



