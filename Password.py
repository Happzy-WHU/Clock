# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Password.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src import resources

class Ui_Password(object):
    def __init__(self, WidgetStack, UIStack):
        self.WidgetStack = WidgetStack
        self.UIStack = UIStack

    WidgetStack = None
    UIStack = None
    def setupUi(self, password):
        password.setObjectName("password")
        password.resize(1013, 772)
        password.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"}\n"
"#password{ \n"
"    background:url(:/resources/background.jpg);\n"
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
        self.frame = QtWidgets.QFrame(password)
        self.frame.setGeometry(QtCore.QRect(240, 120, 491, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 70, 111, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 430, 231, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 190, 351, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 300, 351, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(320, 200, 101, 21))
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
        self.toolButton = QtWidgets.QToolButton(password)
        self.toolButton.setGeometry(QtCore.QRect(420, 40, 131, 121))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(password)
        QtCore.QMetaObject.connectSlotsByName(password)

    def retranslateUi(self, password):
        _translate = QtCore.QCoreApplication.translate
        password.setWindowTitle(_translate("password", "智慧考勤"))
        self.label.setText(_translate("password", "找回密码"))
        self.pushButton.setText(_translate("password", "下一步"))
        self.lineEdit.setPlaceholderText(_translate("password", "Phone Number"))
        self.lineEdit_2.setPlaceholderText(_translate("password", "Verification Code"))
        self.label_2.setText(_translate("password", "获取验证码"))

        self.pushButton.clicked.connect(lambda:self.onPushButtonClick())


    def onPushButtonClick(self):
        self.jumpToReset();

    def jumpToReset(self):
        hasFind = False
        import src.Reset
        self.WidgetStack[2].hide()
        
        for ui in self.UIStack:
            print(ui.__class__.__name__)
            if ui.__class__.__name__ == "Ui_Reset":
                ui.setupUi(self.WidgetStack[4])
                ui.retranslateUi(self.WidgetStack[4])
                hasFind = True
        if hasFind == False:
            newUi = src.Reset.Ui_Reset(self.WidgetStack,self.UIStack)
            newUi.setupUi(self.WidgetStack[4])
            newUi.retranslateUi(self.WidgetStack[4])
            self.UIStack.append(newUi)
        self.WidgetStack[4].show()




