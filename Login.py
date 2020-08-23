# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import QRect,QMetaObject,QCoreApplication,QSize
from PyQt5.QtGui import QFont,QPixmap,QIcon
from PyQt5.QtWidgets import QFrame,QLabel,QPushButton,QWidget,QLineEdit,QErrorMessage,QToolButton


from src import resources,ClickLabel,Connect,SendJSON



class Ui_Login(QWidget):
    def __init__(self, WidgetStack, UIStack):
        self.WidgetStack = WidgetStack
        self.UIStack = UIStack

    WidgetStack = None
    UIStack = None
    hasShow = True

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1013, 772)
        Widget.setMinimumSize(QSize(492, 522))
        Widget.setMaximumSize(QSize(1076, 845))
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
        self.frame = QFrame(Widget)
        self.frame.setGeometry(QRect(240, 120, 491, 521))
        self.frame.setStyleSheet("Frame{hiden();}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(160, 70, 161, 61))
        self.label.setObjectName("label")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(80, 420, 321, 41))
        self.pushButton.setStyleSheet("font: 75 14pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setGeometry(QRect(70, 190, 351, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QRect(70, 280, 351, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = ClickLabel.ClickLabel(self.frame)
        self.label_2.setGeometry(QRect(90, 340, 91, 31))
        font = QFont()
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
        self.label_3.setGeometry(QRect(310, 340, 91, 31))
        font = QFont()
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
        self.toolButton = QToolButton(Widget)
        self.toolButton.setGeometry(QRect(420, 40, 131, 121))
        self.toolButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/resources/people.png"), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(64, 64))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QCoreApplication.translate
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
                err = QErrorMessage(self.frame)
                err.setStyleSheet("color:#880000;background:white;")
                err.showMessage("错误的用户名密码！")
            return
        s = res["token"]
        if s!=None and s!="":
            with open("token", mode="w") as f:
                f.write(s)
            self.jumpToHome()
        else:
            err = QErrorMessage(self.frame)
            err.setStyleSheet("color:#880000;background:white;")
            err.showMessage("错误的用户名密码！")

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






