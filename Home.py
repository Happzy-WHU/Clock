# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src import ClickLabel,resources
import time

class Ui_Home(object):
    def __init__(self, WidgetStack, UIStack):
        self.WidgetStack = WidgetStack
        self.UIStack = UIStack

    WidgetStack = None
    UIStack = None
    hasRun = False
    hasShow = True


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1013, 772)
        Form.setStyleSheet("background:rgb(231, 231, 231)")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 120, 772))
        self.frame.setStyleSheet("background : rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 55, 54))
        self.pushButton.setStyleSheet("\n"
"QPushButton{\n"
"border:none;\n"
"background:url(:/resources/home.png);}\n"
"")
        self.pushButton.setText("")
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 235, 55, 55))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton{\n"
"border:none;\n"
"background:url(:/resources/user.png)}")
        self.pushButton_2.setText("")
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 360, 55, 55))
        self.pushButton_4.setStyleSheet("\n"
"QPushButton{\n"
"border:none;\n"
"background:url(:/resources/message.png)}")
        self.pushButton_4.setText("")
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 486, 55, 55))
        self.pushButton_3.setStyleSheet("\n"
"QPushButton{\n"
"border:none;background:url(:/resources/chart.png)}\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 611, 55, 55))
        self.pushButton_5.setStyleSheet("\n"
"QPushButton{\n"
"border:none;background:url(:/resources/clock.png)}")
        self.pushButton_5.setText("")
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 20, 801, 701))
        self.stackedWidget.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"\n"
"}\n"
"#Apply{ \n"
"    \n"
"}\n"
"QFrame{\n"
"    \n"
"    background-color: rgb(240, 255, 162);\n"
"    background-color: white;\n"
"    background-color: #49ebff;\n"
"    \n"
"    background-color: rgb(181, 236, 255);\n"
"    background-color: rgb(226, 226, 226);\n"
"    background-color: rgb(231, 231, 231);\n"
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
"    \n"
"background-color: rgb(119, 174, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(106, 107, 189);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"\n"
"\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.TakePhoto1 = QtWidgets.QWidget()
        self.TakePhoto1.setObjectName("TakePhoto1")
        self.graphicsView = QtWidgets.QGraphicsView(self.TakePhoto1)
        self.graphicsView.setGeometry(QtCore.QRect(210, 110, 291, 291))
        self.graphicsView.setStyleSheet("background:url(:/resources/camera.png)")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_8 = QtWidgets.QPushButton(self.TakePhoto1)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 540, 131, 41))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    \n"
"background-color: rgb(50, 199, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget.addWidget(self.TakePhoto1)
        self.TakePhoto2 = QtWidgets.QWidget()
        self.TakePhoto2.setObjectName("TakePhoto2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.TakePhoto2)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 20, 761, 581))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton_13 = QtWidgets.QPushButton(self.TakePhoto2)
        self.pushButton_13.setGeometry(QtCore.QRect(290, 610, 131, 41))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    \n"
"background-color: rgb(50, 199, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget.addWidget(self.TakePhoto2)
        self.Modify2 = QtWidgets.QWidget()
        self.Modify2.setObjectName("Modify2")
        self.frame_4 = QtWidgets.QFrame(self.Modify2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 800, 701))
        self.frame_4.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"\n"
"}\n"
"#Apply{ \n"
"    \n"
"}\n"
"QFrame{\n"
"    \n"
"    background-color: rgb(240, 255, 162);\n"
"    background-color: white;\n"
"    background-color: #49ebff;\n"
"    \n"
"    background-color: rgb(181, 236, 255);\n"
"    background-color: rgb(226, 226, 226);\n"
"    background-color: rgb(231, 231, 231);\n"
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
"    \n"
"background-color: rgb(119, 174, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(106, 107, 189);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"\n"
"\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.splitter_3 = QtWidgets.QSplitter(self.frame_4)
        self.splitter_3.setGeometry(QtCore.QRect(0, 0, 573, 681))
        self.splitter_3.setStyleSheet("QLabel{\n"
"color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"}")
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_22 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_23.setObjectName("label_23")
        self.label_21 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_21.setObjectName("label_21")
        self.label_25 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_25.setObjectName("label_25")
        self.label_34 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_34.setObjectName("label_34")
        self.label_35 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_35.setObjectName("label_35")
        self.splitter_6 = QtWidgets.QSplitter(self.frame_4)
        self.splitter_6.setGeometry(QtCore.QRect(573, 0, 109, 681))
        self.splitter_6.setStyleSheet("QLabel{\n"
"color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"}")
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.label_36 = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_36.setFont(font)
        self.label_36.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_36.setStyleSheet("background:rgb(231, 231, 231)\n"
"")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = ClickLabel.ClickLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_38.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.label_39 = ClickLabel.ClickLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = ClickLabel.ClickLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.label_41 = ClickLabel.ClickLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.stackedWidget.addWidget(self.Modify2)
        self.Apply = QtWidgets.QWidget()
        self.Apply.setObjectName("Apply")
        self.frame_5 = QtWidgets.QFrame(self.Apply)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.frame_5.setStyleSheet("\n"
"*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"\n"
"}\n"
"#Apply{ \n"
"    \n"
"}\n"
"QFrame{\n"
"    \n"
"background:rgb(231, 231, 231);\n"
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
"    \n"
"background-color: rgb(119, 174, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(106, 107, 189);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"\n"
"\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setGeometry(QtCore.QRect(270, 60, 141, 31))
        self.label_24.setStyleSheet("\n"
"font: 80 16pt \"Bahnschrift SemiBold\";\n"
"font-weight: bold; \n"
"color: rgb(56, 56, 56);")
        self.label_24.setObjectName("label_24")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setGeometry(QtCore.QRect(150, 130, 371, 41))
        self.lineEdit.setStyleSheet("border-color: rgb(167, 167, 167);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 430, 371, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 560, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background:(55,199,255)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 230, 371, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 330, 371, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.stackedWidget.addWidget(self.Apply)
        self.Modify1 = QtWidgets.QWidget()
        self.Modify1.setObjectName("Modify1")
        self.frame_9 = QtWidgets.QFrame(self.Modify1)
        self.frame_9.setGeometry(QtCore.QRect(0, 0, 800, 701))
        self.frame_9.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"\n"
"}\n"
"#Apply{ \n"
"    \n"
"}\n"
"QFrame{\n"
"    \n"
"    background-color: rgb(240, 255, 162);\n"
"    background-color: white;\n"
"    background-color: #49ebff;\n"
"    \n"
"    background-color: rgb(181, 236, 255);\n"
"    background-color: rgb(226, 226, 226);\n"
"    background-color: rgb(231, 231, 231);\n"
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
"    \n"
"background-color: rgb(119, 174, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(106, 107, 189);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"\n"
"\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}\n"
"\n"
"")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.splitter_9 = QtWidgets.QSplitter(self.frame_9)
        self.splitter_9.setGeometry(QtCore.QRect(0, 0, 573, 681))
        self.splitter_9.setStyleSheet("QLabel{\n"
"color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"}")
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.label_54 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_54.setObjectName("label_54")
        self.label_55 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_55.setObjectName("label_55")
        self.label_56 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_56.setObjectName("label_56")
        self.label_57 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_58.setObjectName("label_58")
        self.label_59 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("background:rgb(231, 231, 231)")
        self.label_59.setObjectName("label_59")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_9)
        self.graphicsView_3.setGeometry(QtCore.QRect(573, 0, 109, 109))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_9)
        self.splitter_2.setGeometry(QtCore.QRect(573, 115, 109, 566))
        self.splitter_2.setStyleSheet("QLabel{\n"
"color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background:rgb(231, 231, 231);\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"}")
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_7 = ClickLabel.ClickLabel(self.splitter_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = ClickLabel.ClickLabel(self.splitter_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = ClickLabel.ClickLabel(self.splitter_2)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.splitter_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = ClickLabel.ClickLabel(self.splitter_2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.Modify1)
        self.Leave = QtWidgets.QWidget()
        self.Leave.setStyleSheet("color:0x000000")
        self.Leave.setObjectName("Leave")
        self.label_13 = QtWidgets.QLabel(self.Leave)
        self.label_13.setGeometry(QtCore.QRect(40, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Leave)
        self.label_14.setGeometry(QtCore.QRect(40, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Leave)
        self.label_15.setGeometry(QtCore.QRect(410, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Leave)
        self.label_16.setGeometry(QtCore.QRect(410, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Leave)
        self.label_17.setGeometry(QtCore.QRect(40, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_17.setObjectName("label_17")
        self.comboBox = QtWidgets.QComboBox(self.Leave)
        self.comboBox.setGeometry(QtCore.QRect(170, 75, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.dateEdit = QtWidgets.QDateEdit(self.Leave)
        self.dateEdit.setGeometry(QtCore.QRect(170, 195, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.Leave)
        self.dateEdit_2.setGeometry(QtCore.QRect(550, 195, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.Leave)
        self.timeEdit.setGeometry(QtCore.QRect(170, 315, 161, 31))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.Leave)
        self.timeEdit_2.setGeometry(QtCore.QRect(550, 315, 161, 31))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.Leave)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 380, 671, 241))
        self.plainTextEdit.setStyleSheet("background:white\n"
"")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_9 = QtWidgets.QPushButton(self.Leave)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 660, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background:(55,199,255)")
        self.pushButton_9.setObjectName("pushButton_9")
        self.stackedWidget.addWidget(self.Leave)
        self.Count = QtWidgets.QWidget()
        self.Count.setObjectName("Count")
        self.frame_6 = QtWidgets.QFrame(self.Count)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.frame_6.setStyleSheet("\n"
"*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"\n"
"}\n"
"#Apply{ \n"
"    \n"
"}\n"
"QFrame{\n"
"background-color: rgb(231, 231, 231);\n"
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
"    \n"
"background-color: rgb(119, 174, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(106, 107, 189);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(270, 40, 181, 41))
        self.label.setStyleSheet("\n"
"font: 80 16pt \"Bahnschrift SemiBold\";\n"
"font-weight: bold; \n"
"color: rgb(56, 56, 56);")
        self.label.setObjectName("label")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_10.setGeometry(QtCore.QRect(670, 130, 91, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.frame_6)
        self.dateEdit_3.setGeometry(QtCore.QRect(100, 130, 461, 41))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.splitter_4 = QtWidgets.QSplitter(self.frame_6)
        self.splitter_4.setGeometry(QtCore.QRect(50, 210, 571, 411))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_26 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_28.setObjectName("label_28")
        self.stackedWidget.addWidget(self.Count)
        self.Search = QtWidgets.QWidget()
        self.Search.setObjectName("Search")
        self.frame_8 = QtWidgets.QFrame(self.Search)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.frame_8.setStyleSheet("\n"
"*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"\n"
"}\n"
"#Apply{ \n"
"    \n"
"}\n"
"QFrame{\n"
"    \n"
"background:rgb(231, 231, 231);\n"
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
"    \n"
"background-color: rgb(119, 174, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(106, 107, 189);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_29 = QtWidgets.QLabel(self.frame_8)
        self.label_29.setGeometry(QtCore.QRect(270, 40, 181, 41))
        self.label_29.setStyleSheet("\n"
"font: 80 16pt \"Bahnschrift SemiBold\";\n"
"font-weight: bold; \n"
"color: rgb(56, 56, 56);")
        self.label_29.setObjectName("label_29")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_11.setGeometry(QtCore.QRect(670, 130, 91, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame_8)
        self.dateEdit_4.setGeometry(QtCore.QRect(100, 130, 461, 41))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.splitter_5 = QtWidgets.QSplitter(self.frame_8)
        self.splitter_5.setGeometry(QtCore.QRect(50, 210, 571, 411))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.label_30 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_33.setObjectName("label_33")
        self.stackedWidget.addWidget(self.Search)
        self.Message1 = QtWidgets.QWidget()
        self.Message1.setObjectName("Message1")
        self.frame_7 = QtWidgets.QFrame(self.Message1)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.frame_7.setStyleSheet("\n"
"*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"\n"
"}\n"
"#Apply{ \n"
"    \n"
"}\n"
"QFrame{\n"
"    \n"
"background:rgb(231, 231, 231);\n"
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
"    \n"
"background-color: rgb(119, 174, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(106, 107, 189);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 141, 41))
        self.label_2.setStyleSheet("\n"
"font: 80 16pt \"Bahnschrift SemiBold\";\n"
"font-weight: bold; \n"
"color: rgb(56, 56, 56);")
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_7)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 611, 411))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section{background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(119, 167, 255),stop:0.5 rgb(118, 106, 255),stop:1 rgb(190, 187, 255));color:rgb(66, 94, 125);padding-left: 1px;border: 1px solid rgb(149, 190, 255)}\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(232, 232, 232))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.stackedWidget.addWidget(self.Message1)
        self.Message2 = QtWidgets.QWidget()
        self.Message2.setObjectName("Message2")
        self.frame_3 = QtWidgets.QFrame(self.Message2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 791, 681))
        self.frame_3.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"\n"
"}\n"
"#Apply{ \n"
"    \n"
"}\n"
"QFrame{\n"
"    \n"
"background:rgb(231, 231, 231);\n"
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
"    \n"
"background-color: rgb(119, 174, 255);\n"
"border-radius:15px;\n"
"font-color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(106, 107, 189);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"\n"
"\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(170, 40, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 12pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(170, 100, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 12pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(170, 160, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 12pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 540, 131, 41))
        self.pushButton_7.setStyleSheet("background:rgb(50, 199, 255)")
        self.pushButton_7.setObjectName("pushButton_7")
        self.splitter = QtWidgets.QSplitter(self.frame_3)
        self.splitter.setGeometry(QtCore.QRect(50, 40, 161, 421))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(58, 55, 144);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.Message2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "智慧考勤"))
        self.pushButton_8.setText(_translate("Form", "打 卡"))
        self.pushButton_13.setText(_translate("Form", "返 回"))
        self.label_22.setText(_translate("Form", "UID"))
        self.label_23.setText(_translate("Form", "手机号"))
        self.label_21.setText(_translate("Form", "修改密码"))
        self.label_25.setText(_translate("Form", "加入公司"))
        self.label_34.setText(_translate("Form", "注销登陆"))
        self.label_35.setText(_translate("Form", "返回"))
        self.label_36.setText(_translate("Form", ""))
        self.label_37.setText(_translate("Form", "手机号                                 >"))
        self.label_38.setText(_translate("Form", "修改密码                             >"))
        self.label_39.setText(_translate("Form", "加入公司                             >"))
        self.label_40.setText(_translate("Form", "注销登陆                             >"))
        self.label_41.setText(_translate("Form", "返回                                      >"))
        self.label_24.setText(_translate("Form", "公 司 申 请"))
        self.lineEdit.setPlaceholderText(_translate("Form", "申请人姓名"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "公司编号"))
        self.pushButton_6.setText(_translate("Form", "提 交"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "申请人编号"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "公司名称"))
        self.label_54.setText(_translate("Form", "头像"))
        self.label_55.setText(_translate("Form", "昵称"))
        self.label_56.setText(_translate("Form", "性别"))
        self.label_57.setText(_translate("Form", "生日"))
        self.label_58.setText(_translate("Form", "年龄"))
        self.label_59.setText(_translate("Form", "更多"))
        self.label_7.setText(_translate("Form", ">"))
        self.label_8.setText(_translate("Form", ">"))
        self.label_9.setText(_translate("Form", ">"))
        self.label_10.setText(_translate("Form", ""))
        self.label_11.setText(_translate("Form", ">"))
        self.label_13.setText(_translate("Form", "请假类型:"))
        self.label_14.setText(_translate("Form", "开始日期:"))
        self.label_15.setText(_translate("Form", "结束日期:"))
        self.label_16.setText(_translate("Form", "结束时间:"))
        self.label_17.setText(_translate("Form", "开始时间:"))
        self.pushButton_9.setText(_translate("Form", "提 交"))
        self.label.setText(_translate("Form", "月 度 统 计"))
        self.pushButton_10.setText(_translate("Form", "查询"))
        self.label_26.setText(_translate("Form", "迟到统计："))
        self.label_27.setText(_translate("Form", "缺勤统计："))
        self.label_28.setText(_translate("Form", "请假统计："))
        self.label_29.setText(_translate("Form", "考 勤 统 计"))
        self.pushButton_11.setText(_translate("Form", "查询"))
        self.label_30.setText(_translate("Form", "上班打卡时间："))
        self.label_31.setText(_translate("Form", "下班打卡时间："))
        self.label_32.setText(_translate("Form", "迟到："))
        self.label_33.setText(_translate("Form", "旷工："))
        self.label_2.setText(_translate("Form", "消 息 列 表"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "发送人"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "发送时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "内容"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "查看状态"))
        self.pushButton_7.setText(_translate("Form", "返 回"))
        self.label_3.setText(_translate("Form", "ID："))
        self.label_4.setText(_translate("Form", "发送人："))
        self.label_5.setText(_translate("Form", "发送时间："))
        self.label_6.setText(_translate("Form", "内容："))

        self.pushButton.clicked.connect(lambda: self.onPushButtonClick())
        self.pushButton_2.clicked.connect(lambda: self.onPushButton_2Click())
        self.pushButton_3.clicked.connect(lambda: self.onPushButton_3Click())
        self.pushButton_4.clicked.connect(lambda: self.onPushButton_4Click())
        self.pushButton_5.clicked.connect(lambda: self.onPushButton_5Click())
        self.pushButton_8.clicked.connect(lambda: self.onPushButton_8Click())
        self.pushButton_13.clicked.connect(lambda: self.onPushButton_13Click())

        self.label_59.clicked.connect(lambda: self.onLabel_59Click())
        self.label_11.clicked.connect(lambda: self.onLabel_59Click())
        self.label_25.clicked.connect(lambda: self.onLabel_25Click())
        self.label_39.clicked.connect(lambda: self.onLabel_25Click())
        self.label_35.clicked.connect(lambda: self.onLabel_35Click())
        self.label_41.clicked.connect(lambda: self.onLabel_35Click())
        self.label_21.clicked.connect(lambda: self.onLabel_21Click())
        self.label_38.clicked.connect(lambda: self.onLabel_21Click())
        self.label_34.clicked.connect(lambda: self.onLabel_34Click())
        self.label_40.clicked.connect(lambda: self.onLabel_34Click())

        self.label_7.clicked.connect(lambda: self.onLabel_7Click())
        self.label_55.clicked.connect(lambda: self.onLabel_7Click())

        self.label_8.clicked.connect(lambda: self.onLabel_8Click())
        self.label_56.clicked.connect(lambda: self.onLabel_8Click())

        self.label_9.clicked.connect(lambda: self.onLabel_9Click())
        self.label_57.clicked.connect(lambda: self.onLabel_9Click())
        #
        # self.label_54.clicked.connect(lambda: self.onLabel_4Click()) #待实现

    # <editor-fold desc="Click事件">
    def onPushButtonClick(self):
        self.jumpToHome()
    def onPushButton_2Click(self):
        self.jumpToModify1()
    def onPushButton_3Click(self):
        self.jumpToCount()
    def onPushButton_4Click(self):
        self.jumpToMessage1()
    def onPushButton_5Click(self):
        self.jumpToLeave()
    def onPushButton_8Click(self):
        self.jumpToTakePhoto2()
    def onPushButton_13Click(self):
        self.jumpToHome()
    def onLabel_59Click(self):
        self.jumpToModify2()
    def onLabel_57Click(self):
        return
    def onLabel_25Click(self):
        self.jumpToApply()
    def onLabel_35Click(self):
        self.jumpToModify1()
    def onLabel_21Click(self):
        self.jumpToPassword()
    def onLabel_34Click(self):
        self.jumpToLogin()
    def onLabel_7Click(self):
        self.nameDialog()
    def onLabel_8Click(self):
        self.sexDialog()
    def onLabel_9Click(self):
        self.birthDialog()



    # </editor-fold>

    # <editor-fold desc="jump事件">
    def sexDialog(self):
        self.hasShow= not self.hasShow
        if self.hasShow == False:
            items = ('男', '女')
            item, ok = QtWidgets.QInputDialog.getItem\
                (self.stackedWidget, "性别", '性别', items, False)
            if ok and item:
                self.label_56.setText("性别:          " + item)

    def nameDialog(self):
        self.hasShow = not self.hasShow
        if self.hasShow == False:
            text, ok = QtWidgets.QInputDialog.getText\
                (self.stackedWidget, '昵称', '输入昵称：')
            if ok:
                self.label_55.setText("昵称:          "+str(text))

    def judgeDateIsRight(self,date):
        try:
            if ":" in date:
                time.strptime(date, "%Y-%m-%d %H:%M:%S")
            else:
                time.strptime(date, "%Y-%m-%d")
            return True
        except:
            return False

    def birthDialog(self):
        self.hasShow = not self.hasShow
        if self.hasShow == False:
            year, ok = QtWidgets.QInputDialog.getText \
                (self.stackedWidget, 'year', '输入年份：')
            if ok:
                month, ok = QtWidgets.QInputDialog.getText \
                    (self.stackedWidget, 'month', '输入月份：')
                if ok:
                    day, ok = QtWidgets.QInputDialog.getText \
                        (self.stackedWidget, 'day', '输入天数：')
                    if ok:
                        if self.judgeDateIsRight(year+'-'+month+'-'+day) == False:
                            err = QtWidgets.QErrorMessage(self.stackedWidget)
                            err.showMessage("输入的日期不合法！")
                        else:
                            self.label_57.setText("生日:          "+year+'-'+month+'-'+day)




    def jumpToHome(self):
        if (self.hasRun == False):
            self.MyJump()
            self.hasRun = True
        self.stackedWidget.setCurrentIndex(0)

    def jumpToModify1(self):
        if(self.hasRun==False):
            self.MyJump()
            self.hasRun=True
        self.stackedWidget.setCurrentIndex(4)

    def jumpToCount(self):
        if (self.hasRun == False):
            self.MyJump()
            self.hasRun = True
        self.stackedWidget.setCurrentIndex(6)

    def jumpToMessage1(self):
        if (self.hasRun == False):
            self.MyJump()
            self.hasRun = True
        self.stackedWidget.setCurrentIndex(8)

    def jumpToApply(self):
        self.stackedWidget.setCurrentIndex(3)

    def jumpToLeave(self):
        if (self.hasRun == False):
            self.MyJump()
            self.hasRun = True
        self.stackedWidget.setCurrentIndex(5)

    def jumpToTakePhoto2(self):
        self.stackedWidget.setCurrentIndex(1)

    def jumpToModify2(self):
        self.stackedWidget.setCurrentIndex(2)

    def jumpToSearch(self):
        self.stackedWidget.setCurrentIndex(7)

    def jumpToMessage2(self):
        self.stackedWidget.setCurrentIndex(9)

    def jumpToPassword(self):
        hasFind = False
        import src.Password
        self.WidgetStack[0].hide()
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

    def jumpToLogin(self):
        self.hasRun = False
        hasFind = False
        import src.Login
        self.WidgetStack[1].hide()

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

    def MyJump(self):
        self.WidgetStack[0].hide()
        for ui in self.UIStack:
            if ui.__class__.__name__ == "Ui_Home":
                ui.setupUi(self.WidgetStack[0])
                ui.retranslateUi(self.WidgetStack[0])
        self.WidgetStack[0].show()

    # </editor-fold>


