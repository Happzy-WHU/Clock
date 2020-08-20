# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src import resources,ClickLabel,Connect,SendJSON



class Ui_Login(QtWidgets.QWidget):
    def __init__(self, WidgetStack, UIStack):
        self.WidgetStack = WidgetStack
        self.UIStack = UIStack

    WidgetStack = None
    UIStack = None
    hasShow = True

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1013, 772)
        Widget.setMinimumSize(QtCore.QSize(492, 522))
        Widget.setMaximumSize(QtCore.QSize(1076, 845))
        Widget.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"}\n"
"#Widget{ \n"
"background: url(:/resources/background.jpg)\n"
"}\n"
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
"}\n"
"\n"
"QPushLabel:hover{\n"
"background:red;\n"
"border-radius:15px;\n"
"\n"
"}")
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(240, 120, 491, 521))
        self.frame.setStyleSheet("Frame{hiden();}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 70, 161, 61))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 420, 321, 41))
        self.pushButton.setStyleSheet("font: 75 14pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 190, 351, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 280, 351, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = ClickLabel.ClickLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(53, 228, 255);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 12pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = ClickLabel.ClickLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(310, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(53, 228, 255);\n"
"\n"
"font: 75 12pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(Widget)
        self.toolButton.setGeometry(QtCore.QRect(420, 40, 131, 121))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "智慧考勤"))
        self.label.setText(_translate("Widget", "LOGIN  HERE"))
        self.pushButton.setText(_translate("Widget", "登  录"))
        self.lineEdit.setPlaceholderText(_translate("Widget", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Widget", "Password"))
        self.label_2.setText(_translate("Widget", "账号注册"))
        self.label_3.setText(_translate("Widget", "忘记密码"))

        self.pushButton.clicked.connect(lambda:self.onPushButtonClick())
        self.label_2.clicked.connect(lambda:self.onLabel_2Click())
        self.label_3.clicked.connect(lambda:self.onLabel_3Click())
        self.lineEdit_2.textChanged.connect(self.textChanged2)
        self.lineEdit.textChanged.connect(self.textChanged)

    def textChanged(self,text):
        self.lineEdit.setText(text)
    def textChanged2(self,text):
        self.lineEdit_2.setText(text)

    def onPushButtonClick(self):
        arr=[]
        arr.append(self.lineEdit.text())
        arr.append(self.lineEdit_2.text())
        arr.append(100)

        print(SendJSON.getLoginJSON(arr))

        res = Connect.sendJSON("/token",SendJSON.getLoginJSON(arr))
        if res==None:
            self.hasShow=not self.hasShow
            if self.hasShow==False:
                reply = QtWidgets.QMessageBox.information \
                (self.frame, "error", "错误的用户名密码", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            return
        s = res["token"]
        if s!=None and s!="":
            with open("token", mode="w") as f:
                f.write(s)
            self.jumpToHome()
        else:
            reply = QtWidgets.QMessageBox.information \
                (self.frame, "error", "错误的用户名密码", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    def onLabel_2Click(self):
        self.jumpToRegister()

    def onLabel_3Click(self):
        self.jumpToPassword()


    def jumpToRegister(self):
        hasFind = False
        import src.Register
        self.WidgetStack[1].hide()
        for ui in self.UIStack:
            print(ui.__class__.__name__)
            if ui.__class__.__name__ == "Ui_Register":
                ui.setupUi(self.WidgetStack[3])
                ui.retranslateUi(self.WidgetStack[3])
                hasFind = True
        if hasFind == False:
            newUi = src.Register.Ui_Register(self.WidgetStack,self.UIStack)
            newUi.setupUi(self.WidgetStack[3])
            newUi.retranslateUi(self.WidgetStack[3])
            self.UIStack.append(newUi)
        self.WidgetStack[3].show()

    def jumpToHome(self):
        
        hasFind = False
        import src.Home
        self.WidgetStack[1].hide()
        
        for ui in self.UIStack:
            print(ui.__class__.__name__)
            if ui.__class__.__name__ == "Ui_Home":
                ui.setupUi(self.WidgetStack[0])
                ui.retranslateUi(self.WidgetStack[0])
                hasFind=True
        if hasFind == False:
            newUi = src.Home.Ui_Home(self.WidgetStack,self.UIStack)
            newUi.setupUi(self.WidgetStack[0])
            newUi.retranslateUi(self.WidgetStack[0])
            self.UIStack.append(newUi)
        self.WidgetStack[0].show()

    def jumpToPassword(self):
        hasFind = False
        import src.Password
        self.WidgetStack[1].hide()

        for ui in self.UIStack:
            print(ui.__class__.__name__)
            if ui.__class__.__name__ == "Ui_Password":
                ui.setupUi(self.WidgetStack[2])
                ui.retranslateUi(self.WidgetStack[2])
                hasFind = True
        if hasFind == False:
            newUi = src.Password.Ui_Password(self.WidgetStack, self.UIStack)
            newUi.setupUi(self.WidgetStack[2])
            newUi.retranslateUi(self.WidgetStack[2])
            self.UIStack.append(newUi)
        self.WidgetStack[2].show()






