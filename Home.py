# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from src import ClickLabel, resources, SendJSON, Connect, Stage, Message
import time
from datetime import datetime
import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import sys
import base64

class Ui_Home(object):
    def __init__(self, WidgetStack, UIStack):
        self.WidgetStack = WidgetStack
        self.UIStack = UIStack

    WidgetStack = None
    UIStack = None
    hasRun = False
    hasShow = True
    capTime = 0
    stage1 = Stage.stage()
    stage2 = Stage.stage()
    typeStack=[]
    midStack=[]
    pressCount=0
    processCount=0

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
        self.pushButton_5.setGeometry(QtCore.QRect(30, 611, 55, 53))
        self.pushButton_5.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "border:none;background:url(:/resources/clock.png)}")
        self.pushButton_5.setText("")
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 0, 891, 772))
        self.stackedWidget.setStyleSheet("*{\n"
                                         "font-size:24px;\n"
                                         "font-family:Century Gothic;\n"
                                         "\n"
                                         "}\n"
                                         "#Apply{ \n"
                                         "    \n"
                                         "}\n"
                                         "QFrame{\n"
                                         "\n"
                                         "    background-color: rgb(231, 231, 231);\n"
                                         "border-radius:15px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton{\n"
                                         "background:#49ebff;\n"
                                         "border-radius:60px;\n"
                                         "}\n"
                                         "QLabel{\n"
                                         "color:black;\n"
                                         "background:rgb(231, 231, 231);\n"
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
                                         "QDialog{\n"
                                         "color:black;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.stackedWidget.setObjectName("stackedWidget")
        self.TakePhoto1 = QtWidgets.QWidget()
        self.TakePhoto1.setObjectName("TakePhoto1")
        self.label_showcam = QtWidgets.QLabel(self.TakePhoto1)
        self.label_showcam.setGeometry(QtCore.QRect(290, 120, 291, 291))
        self.label_showcam.setObjectName("label_showcam")
        self.label_showcam.setStyleSheet("background:url(:/resources/camera.png)")

        self.pushButton_8 = QtWidgets.QPushButton(self.TakePhoto1)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 540, 131, 41))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "    \n"
                                        "background-color: rgb(50, 199, 255);\n"
                                        "border-radius:15px;\n"
                                        "font-color:white;\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_pz = QtWidgets.QPushButton(self.TakePhoto1)
        self.pushButton_pz.setGeometry(QtCore.QRect(370, 600, 131, 41))
        self.pushButton_pz.setStyleSheet("QPushButton{\n"
                                         "    \n"
                                         "background-color: rgb(50, 199, 255);\n"
                                         "border-radius:15px;\n"
                                         "font-color:white;\n"
                                         "}")
        self.pushButton_pz.setObjectName("pushButton_pz")
        self.stackedWidget.addWidget(self.TakePhoto1)
        self.TakePhoto2 = QtWidgets.QWidget()
        self.TakePhoto2.setObjectName("TakePhoto2")
        self.label_show = QtWidgets.QLabel(self.TakePhoto2)
        self.label_show.setGeometry(QtCore.QRect(120, 20, 791, 661))
        self.label_show.setObjectName("label_show")
        self.pushButton_13 = QtWidgets.QPushButton(self.TakePhoto2)
        self.pushButton_13.setGeometry(QtCore.QRect(370, 650, 131, 41))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
                                         "    \n"
                                         "background-color: rgb(50, 199, 255);\n"
                                         "border-radius:15px;\n"
                                         "font-color:white;\n"
                                         "}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget.addWidget(self.TakePhoto2)
        self.Modify2 = QtWidgets.QWidget()
        self.Modify2.setStyleSheet("")
        self.Modify2.setObjectName("Modify2")
        self.frame_4 = QtWidgets.QFrame(self.Modify2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 891, 772))
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
        self.splitter_3.setGeometry(QtCore.QRect(60, 50, 771, 681))
        self.splitter_3.setStyleSheet("QLabel{\n"
                                      "color: rgb(58, 55, 144);\n"
                                      "background:rgb(255, 255, 255);\n"
                                      "selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "\n"
                                      "font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
                                      "}\n"
                                      "QSplitter{background:rgb(231, 231, 231);\n"
                                      "color:rgb(231, 231, 231);}")
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_22 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_22.setObjectName("label_22")
        self.label_23 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setObjectName("label_23")
        self.label_21 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("")
        self.label_21.setObjectName("label_21")
        self.label_25 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setObjectName("label_25")
        self.label_34 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setObjectName("label_34")
        self.label_35 = ClickLabel.ClickLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("")
        self.label_35.setObjectName("label_35")
        self.stackedWidget.addWidget(self.Modify2)
        self.Apply = QtWidgets.QWidget()
        self.Apply.setObjectName("Apply")
        self.frame_5 = QtWidgets.QFrame(self.Apply)
        self.frame_5.setGeometry(QtCore.QRect(60, 50, 771, 681))
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
                                   "background:rgb(255, 255, 255);\n"
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
        self.label_24 = ClickLabel.ClickLabel(self.frame_5)
        self.label_24.setGeometry(QtCore.QRect(310, 70, 141, 31))
        self.label_24.setStyleSheet("\n"
                                    "font: 80 16pt \"Bahnschrift SemiBold\";\n"
                                    "font-weight: bold; \n"
                                    "color: rgb(56, 56, 56);")
        self.label_24.setObjectName("label_24")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setGeometry(QtCore.QRect(190, 140, 371, 41))
        self.lineEdit.setStyleSheet("border-color: rgb(167, 167, 167);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 440, 371, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 570, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background:(55,199,255)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 240, 371, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 340, 371, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.stackedWidget.addWidget(self.Apply)
        self.Modify1 = QtWidgets.QWidget()
        self.Modify1.setStyleSheet("")
        self.Modify1.setObjectName("Modify1")
        self.frame_9 = QtWidgets.QFrame(self.Modify1)
        self.frame_9.setGeometry(QtCore.QRect(0, 0, 891, 772))
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
        self.splitter_9.setGeometry(QtCore.QRect(60, 50, 771, 681))
        self.splitter_9.setStyleSheet("QLabel{\n"
                                      "color: rgb(58, 55, 144);\n"
                                      "background:rgb(255, 255, 255);\n"
                                      "selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "\n"
                                      "font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
                                      "}\n"
                                      "QSplitter{background:rgb(231, 231, 231);\n"
                                      "color:rgb(231, 231, 231);}")
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
        self.label_54.setStyleSheet("")
        self.label_54.setObjectName("label_54")
        self.label_55 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("")
        self.label_55.setObjectName("label_55")
        self.label_56 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("")
        self.label_56.setObjectName("label_56")
        self.label_57 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("")
        self.label_57.setObjectName("label_57")
        self.label_58 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("")
        self.label_58.setObjectName("label_58")
        self.label_59 = ClickLabel.ClickLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("")
        self.label_59.setObjectName("label_59")

        self.stackedWidget.addWidget(self.Modify1)
        self.Leave = QtWidgets.QWidget()
        self.Leave.setStyleSheet("color:0x000000")
        self.Leave.setObjectName("Leave")
        self.frame_10 = QtWidgets.QFrame(self.Leave)
        self.frame_10.setGeometry(QtCore.QRect(60, 50, 771, 681))
        self.frame_10.setStyleSheet("\n"
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
                                    "background:rgb(255, 255, 255);\n"
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
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_14 = ClickLabel.ClickLabel(self.frame_10)
        self.label_14.setGeometry(QtCore.QRect(60, 145, 141, 41))
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
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_10)
        self.dateEdit.setGeometry(QtCore.QRect(210, 150, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.frame_10)
        self.timeEdit_2.setGeometry(QtCore.QRect(550, 270, 161, 31))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_17 = ClickLabel.ClickLabel(self.frame_10)
        self.label_17.setGeometry(QtCore.QRect(60, 265, 141, 41))
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
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_10)
        self.timeEdit.setGeometry(QtCore.QRect(210, 270, 161, 31))
        self.timeEdit.setObjectName("timeEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_10)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 335, 651, 241))
        self.plainTextEdit.setStyleSheet("background:rgb(231, 231, 231)\n"
                                         "")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_16 = ClickLabel.ClickLabel(self.frame_10)
        self.label_16.setGeometry(QtCore.QRect(400, 265, 141, 41))
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
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_10)
        self.dateEdit_2.setGeometry(QtCore.QRect(550, 150, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDisplayFormat("yyyy-MM-dd")
        self.label_13 = ClickLabel.ClickLabel(self.frame_10)
        self.label_13.setGeometry(QtCore.QRect(60, 25, 141, 41))
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
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 615, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background:(55,199,255)")
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox = QtWidgets.QComboBox(self.frame_10)
        self.comboBox.setGeometry(QtCore.QRect(210, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("病假")
        self.comboBox.addItem("事假")
        self.comboBox.addItem("其他")
        self.label_15 = ClickLabel.ClickLabel(self.frame_10)
        self.label_15.setGeometry(QtCore.QRect(400, 145, 141, 41))
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
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.Leave)
        self.Count = QtWidgets.QWidget()
        self.Count.setObjectName("Count")
        self.frame_6 = QtWidgets.QFrame(self.Count)
        self.frame_6.setGeometry(QtCore.QRect(60, 50, 771, 215))
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
                                   "    \n"
                                   "background:rgb(255, 255, 255);\n"
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
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = ClickLabel.ClickLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(300, 40, 181, 41))
        self.label.setStyleSheet("\n"
                                 "font: 80 16pt \"Bahnschrift SemiBold\";\n"
                                 "font-weight: bold; \n"
                                 "color: rgb(56, 56, 56);")
        self.label.setObjectName("label")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_10.setGeometry(QtCore.QRect(600, 130, 91, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.frame_6)
        self.dateEdit_3.setGeometry(QtCore.QRect(90, 130, 461, 41))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.dateEdit_3.setDate(QtCore.QDate.currentDate())
        self.dateEdit_3.setDisplayFormat("yyyy-MM")
        self.splitter = QtWidgets.QSplitter(self.Count)
        self.splitter.setGeometry(QtCore.QRect(60, 270, 771, 441))
        self.splitter.setStyleSheet("QLabel{\n"
                                    "color: rgb(58, 55, 144);\n"
                                    "background:rgb(255, 255, 255);\n"
                                    "selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "\n"
                                    "font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
                                    "}\n"
                                    "QSplitter{background:rgb(231, 231, 231);\n"
                                    "color:rgb(231, 231, 231);}")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_26 = ClickLabel.ClickLabel(self.splitter)
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
        self.label_36 = ClickLabel.ClickLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(58, 55, 144);\n"
                                    "selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "\n"
                                    "font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
                                    "")
        self.label_36.setObjectName("label_36")
        self.label_27 = ClickLabel.ClickLabel(self.splitter)
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
        self.label_28 = ClickLabel.ClickLabel(self.splitter)
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
        self.frame_8.setGeometry(QtCore.QRect(60, 50, 771, 215))
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
                                   "background:rgb(255, 255, 255);\n"
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
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_29 = ClickLabel.ClickLabel(self.frame_8)
        self.label_29.setGeometry(QtCore.QRect(300, 40, 181, 41))
        self.label_29.setStyleSheet("\n"
                                    "font: 80 16pt \"Bahnschrift SemiBold\";\n"
                                    "font-weight: bold; \n"
                                    "color: rgb(56, 56, 56);")
        self.label_29.setObjectName("label_29")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_11.setGeometry(QtCore.QRect(600, 130, 91, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame_8)
        self.dateEdit_4.setGeometry(QtCore.QRect(90, 130, 461, 41))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.splitter_5 = QtWidgets.QSplitter(self.Search)
        self.splitter_5.setGeometry(QtCore.QRect(60, 270, 771, 441))
        self.splitter_5.setStyleSheet("QLabel{\n"
                                      "color: rgb(58, 55, 144);\n"
                                      "background:rgb(255, 255, 255);\n"
                                      "selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "\n"
                                      "font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
                                      "}\n"
                                      "QSplitter{background:rgb(231, 231, 231);\n"
                                      "color:rgb(231, 231, 231);}")
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.label_30 = ClickLabel.ClickLabel(self.splitter_5)
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
        self.label_31 = ClickLabel.ClickLabel(self.splitter_5)
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
        self.label_32 = ClickLabel.ClickLabel(self.splitter_5)
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
        self.label_33 = ClickLabel.ClickLabel(self.splitter_5)
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
        self.frame_7.setGeometry(QtCore.QRect(60, 50, 731, 621))
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
                                   "background:rgb(255, 255, 255);\n"
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
                                   "QLabel{\n"
                                   "color: rgb(58, 55, 144);\n"
                                   "background:rgb(255, 255, 255);\n"
                                   "selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_2 = ClickLabel.ClickLabel(self.frame_7)
        self.label_2.setGeometry(QtCore.QRect(300, 40, 141, 41))
        self.label_2.setStyleSheet("\n"
                                   "font: 80 16pt \"Bahnschrift SemiBold\";\n"
                                   "font-weight: bold; \n"
                                   "color: rgb(56, 56, 56);")
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_7)
        self.listWidget.setGeometry(QtCore.QRect(50, 130, 631, 431))
        self.listWidget.setStyleSheet("QListWidget\n"
                                      "{\n"
                                      "    color:rgb(200,200,200);\n"
                                      "    border:3px solid gray;\n"
                                      "    padding:20px 0px 0px 0px;\n"
                                      "font-weight: bold; \n"
                                      "}\n"
                                      "/**列表项*/\n"
                                      "QListWidget::item\n"
                                      "{\n"
                                      "    color:rgb(100,100,100);\n"
                                      "    height:40px;\n"
                                      "    padding-left:20px;\n"
                                      "    border:0px solid gray;\n"
                                      "\n"
                                      "}\n"
                                      "/**列表项扫过*/\n"
                                      "QListWidget::item:hover\n"
                                      "{\n"
                                      "    color:rgb(0,0,0);\n"
                                      "   \n"
                                      "}\n"
                                      "/**列表项选中*/\n"
                                      "QListWidget::item::selected:active\n"
                                      "{ \n"
                                      "    color:blue;\n"
                                      "    border-width:0;\n"
                                      "}\n"
                                      "QListWidget::item:selected\n"
                                      "{\n"
                                      "    color:blue;\n"
                                      "    border-width:0;\n"
                                      "}")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()

        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()

        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.stackedWidget.addWidget(self.Message1)
        self.Message2 = QtWidgets.QWidget()
        self.Message2.setObjectName("Message2")
        self.frame_11 = QtWidgets.QFrame(self.Message2)
        self.frame_11.setGeometry(QtCore.QRect(60, 355, 771, 291))
        self.frame_11.setStyleSheet("\n"
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
                                    "background:rgb(255, 255, 255);\n"
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
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_11)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 10, 751, 261))
        self.plainTextEdit_2.setStyleSheet("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_12.setGeometry(QtCore.QRect(310, 615, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background:(55,199,255)")
        self.pushButton_12.setObjectName("pushButton_12")
        self.splitter_8 = QtWidgets.QSplitter(self.Message2)
        self.splitter_8.setGeometry(QtCore.QRect(60, 50, 771, 300))
        self.splitter_8.setStyleSheet("QLabel{\n"
                                      "color: rgb(58, 55, 144);\n"
                                      "background:rgb(255, 255, 255);\n"
                                      "selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "\n"
                                      "font: 75 16pt \"Adobe Garamond Pro Bold\";\n"
                                      "}\n"
                                      "QSplitter{background:rgb(231, 231, 231);\n"
                                      "color:rgb(231, 231, 231);}")
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.label_48 = ClickLabel.ClickLabel(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_48.setObjectName("label_48")
        self.label_49 = ClickLabel.ClickLabel(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("")
        self.label_49.setObjectName("label_49")
        self.label_53 = ClickLabel.ClickLabel(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("")
        self.label_53.setObjectName("label_53")
        self.pushButton_14 = QtWidgets.QPushButton(self.Message2)
        self.pushButton_14.setGeometry(QtCore.QRect(370, 670, 131, 41))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
                                         "    \n"
                                         "background-color: rgb(50, 199, 255);\n"
                                         "border-radius:15px;\n"
                                         "font-color:white;\n"
                                         "}")
        self.pushButton_14.setObjectName("pushButton_14")

        self.checkBox = QtWidgets.QCheckBox(self.Message2)
        self.checkBox.setGeometry(QtCore.QRect(120, 670, 131, 41))
        self.checkBox.setObjectName("checkBox")

        self.stackedWidget.addWidget(self.Message2)

        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(100)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "智慧考勤"))
        self.pushButton_8.setText(_translate("Form", "打 卡"))
        self.pushButton_pz.setText(_translate("Form", "识 别"))
        self.pushButton_13.setText(_translate("Form", "返 回"))
        self.label_22.setText(_translate("Form", "UID"))
        self.label_23.setText(_translate("Form", "手机号"))
        self.label_21.setText(_translate("Form", "修改密码"))
        self.label_25.setText(_translate("Form", "加入组织"))
        self.label_34.setText(_translate("Form", "注销登陆"))
        self.label_35.setText(_translate("Form", "返回"))
        self.label_24.setText(_translate("Form", "组 织 申 请"))
        self.lineEdit.setPlaceholderText(_translate("Form", "申请人姓名"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "组织编号"))
        self.pushButton_6.setText(_translate("Form", "提 交"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "申请人编号"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "组织名称"))
        self.label_54.setText(_translate("Form", "头像"))
        self.label_55.setText(_translate("Form", "昵称"))
        self.label_56.setText(_translate("Form", "性别"))
        self.label_57.setText(_translate("Form", "生日"))
        self.label_58.setText(_translate("Form", "年龄"))
        self.label_59.setText(_translate("Form", "更多"))
        self.label_14.setText(_translate("Form", "开始日期:"))
        self.label_17.setText(_translate("Form", "开始时间:"))
        self.label_16.setText(_translate("Form", "结束时间:"))
        self.label_13.setText(_translate("Form", "请假类型:"))
        self.pushButton_9.setText(_translate("Form", "提 交"))
        self.label_15.setText(_translate("Form", "结束日期:"))
        self.label.setText(_translate("Form", "月 度 统 计"))
        self.pushButton_10.setText(_translate("Form", "查询"))
        self.label_26.setText(_translate("Form", "迟到统计："))
        self.label_36.setText(_translate("Form", "早退统计："))
        self.label_27.setText(_translate("Form", "缺勤统计："))
        self.label_28.setText(_translate("Form", "请假统计："))
        self.label_29.setText(_translate("Form", "考 勤 统 计"))
        self.pushButton_11.setText(_translate("Form", "查询"))
        self.label_30.setText(_translate("Form", "上班打卡时间："))
        self.label_31.setText(_translate("Form", "下班打卡时间："))
        self.label_32.setText(_translate("Form", "当天迟到次数："))
        self.label_33.setText(_translate("Form", "当天缺勤次数："))
        self.label_2.setText(_translate("Form", "消 息 列 表"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "01    <未读>您还没有收到消息！"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "02    <已读>6666666666"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.plainTextEdit_2.setPlainText(_translate("Form", "消息内容："))
        self.pushButton_12.setText(_translate("Form", "提 交"))
        self.label_48.setText(_translate("Form", "CID"))
        self.label_49.setText(_translate("Form", "发送时间"))
        self.label_53.setText(_translate("Form", "发送人"))
        self.pushButton_14.setText(_translate("Form", "返 回"))
        self.checkBox.setText("同意加入")
        self.pushButton.clicked.connect(lambda: self.onPushButtonClick())
        self.pushButton_2.clicked.connect(lambda: self.onPushButton_2Click())
        self.pushButton_3.clicked.connect(lambda: self.onPushButton_3Click())
        self.pushButton_4.clicked.connect(lambda: self.onPushButton_4Click())
        self.pushButton_5.clicked.connect(lambda: self.onPushButton_5Click())
        # self.pushButton_8.clicked.connect(lambda: self.start())
        self.pushButton_13.clicked.connect(lambda: self.onPushButton_13Click())
        self.pushButton_9.clicked.connect(lambda: self.onPushButton_9Click())
        # 统计
        self.pushButton_10.clicked.connect(lambda: self.onPushButton_10Click())
        # 申请加入组织
        self.pushButton_6.clicked.connect(lambda: self.onPushButton_6Click())
        self.pushButton_14.clicked.connect(lambda :self.onPushButton_14Click())

        self.label_59.clicked.connect(lambda: self.onLabel_59Click())
        self.label_25.clicked.connect(lambda: self.onLabel_25Click())
        self.label_35.clicked.connect(lambda: self.onLabel_35Click())
        self.label_21.clicked.connect(lambda: self.onLabel_21Click())
        self.label_34.clicked.connect(lambda: self.onLabel_34Click())

        self.label_55.clicked.connect(lambda: self.onLabel_7Click())

        self.label_56.clicked.connect(lambda: self.onLabel_8Click())

        self.label_57.clicked.connect(lambda: self.onLabel_9Click())
        # self.label_showcam.clicked.connect(self.start)
        self.pushButton_8.clicked.connect(self.start)
        self.listWidget.itemClicked.connect(lambda :self.onItemClick())
        self.listWidget.itemDoubleClicked.connect(lambda :self.onItemDoubleClick(0))

    def start(self, event):
        self.pressCount+=1
        self.capTime = 0
        self.cap = cv2.VideoCapture(0)
        self.timer.timeout.connect(self.capPicture)

    def capPicture(self):
        if (self.hasRun == False):
            self.MyJump()
            self.hasRun = True
        if (self.cap.isOpened()):
            ret, img = self.cap.read()
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            cv2.imwrite("1.png", img)
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)

            self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label_showcam.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.label_showcam.width(), self.label_showcam.height()))
            self.pushButton_pz.clicked.connect(self.shibie)

    def shibie(self):
        pixmap = QPixmap("1.png")  # 按指定路径找到图片
        self.label_show.setPixmap(pixmap)
        self.cap.release()
        self.jumpToTakePhoto2()
        self.label_showcam.setPixmap(QPixmap("resources/camera.jpg"));
        if self.processCount<self.pressCount:
            self.solvePicture()
            self.processCount +=1


    def judgeTodayFirst(self, file_name):
        # 如果是昨天或以前修改或者文件为空表示今天第一次修改
        file_times_access = time.localtime(os.path.getatime(file_name))
        year_access = file_times_access.tm_year
        month_access = file_times_access.tm_mon
        day_access = file_times_access.tm_mday
        print(datetime.now().year.__class__)
        if datetime.now().year > year_access:
            return True
        if datetime.now().month > month_access:
            return True
        if datetime.now().day > day_access:
            return True
        if os.path.getsize(file_name) == 0:
            return True
        return False

    def solvePicture(self):
        with open('1.png', 'rb') as f:
            img = base64.b64encode(f.read()).decode()
        arr = []
        arr.append(img)
        tim_now = datetime.now()
        s = tim_now.strftime('%Y-%m-%d %H:%M:%S')
        s_hour = int(tim_now.strftime('%H'))
        if s_hour <= 6 or s_hour >= 18 or (s_hour >= 12 and s_hour < 13):
            self.hasShow=not self.hasShow
            if self.hasShow==False:
                reply = QMessageBox.information \
                    (self.frame, "Error", "不在打卡时间！", QMessageBox.Yes | QMessageBox.No)
            return

        arr.append(s)

        if s_hour < 12:  # 上午
            self.stage1.check(s_hour)
            self.stage1.judgeThree1(s_hour)
            arr.append(str(self.stage1.isLate))
            arr.append(str(self.stage1.isEarly))
            arr.append(str(self.stage1.isAbsent))
            if self.judgeTodayFirst("1"):
                arr.append("1")
                arr.append(True)
                self.stage1.writeToFile("1",True)
            else:
                arr.append("2")
                arr.append(False)
                self.stage1.writeToFile("1",False)
        else:  # 下午

            self.stage2.check(s_hour)
            self.stage2.judgeThree1(s_hour)
            arr.append(str(self.stage2.isLate))
            arr.append(str(self.stage2.isEarly))
            arr.append(str(self.stage2.isAbsent))
            if self.judgeTodayFirst("2"):
                self.stage1.writeToFile("2",True)
                arr.append("3")
                if True == self.judgeTodayFirst("1"):
                    arr.append(True)
                else:
                    arr.append(False)
            else:
                self.stage1.writeToFile("2",False)
                arr.append("4")
                arr.append(False)

        res = Connect.sendJSON("/check", SendJSON.getCheckJSON(arr))
        if res["msg"] == "ok":
            if self.capTime == 0:
                err = QtWidgets.QErrorMessage(self.frame)
                err.setStyleSheet("color:green;background:white;")
                err.showMessage("打卡成功！")
                self.capTime = 1
                self.jumpToHome()

        else:
            if self.capTime == 0:
                err = QtWidgets.QErrorMessage(self.frame)
                err.setStyleSheet("color:red;background:white;")
                err.showMessage("打卡失败！")
                self.capTime = 1

            #
        # self.label_54.clicked.connect(lambda: self.onLabel_4Click()) #待实现

        # <editor-fold desc="Click事件">

    def onPushButtonClick(self):
        self.jumpToHome()

    def onPushButton_2Click(self):
        res = Connect.sendJSON("/info", {})
        self.label_22.setText("UID:          " + res["uid"])
        self.label_55.setText("昵称:          " + res["name"])
        self.label_56.setText("性别:          " + res["sex"])
        self.label_57.setText("生日:          " + res["birth"])
        s = self.label_57.text()[13:len(self.label_57.text())].replace("-", "")
        print(s)
        self.setAge(s)
        self.jumpToModify1()

    def onPushButton_3Click(self):
        self.jumpToCount()

    def onPushButton_4Click(self):
        self.listWidget.clear()
        res = Connect.sendJSON("/messages", {})
        arr = Message.getApplyMessage(res["apply"])
        arr.extend(Message.getInviteMessage(res["invite"]))
        arr.extend(Message.getNormalMessage(res["msg"]))
        print(arr)
        arr = Message.sortMessages(arr)
        for i in range(len(arr)):
            s2 = "<" + arr[i].time + ">"
            if(len(self.typeStack)<len(arr)):
                self.typeStack.append("")
            if (len(self.midStack) < len(arr)):
                self.midStack.append("")
            self.midStack[i] = arr[i].mid
            if str(arr[i].__class__) == '<class \'src.Message.ApplyMessage\'>':
                item = QtWidgets.QListWidgetItem()
                item.setText(str(self.listWidget.count()) + "    " + "加入" + arr[i].cname + "的申请   " + s2)
                self.listWidget.addItem(item)
                self.typeStack[i]="2"
            elif str(arr[i].__class__) == '<class \'src.Message.InviteMessage\'>':
                item = QtWidgets.QListWidgetItem()
                item.setText(str(self.listWidget.count()) + "    " + "加入" + arr[i].cname + "的邀请   " + s2)
                self.listWidget.addItem(item)
                self.typeStack[i]="3"

            elif str(arr[i].__class__) == '<class \'src.Message.NormalMessage\'>':
                item = QtWidgets.QListWidgetItem()
                item.setText(str(self.listWidget.count()) + "    " + arr[i].content + "    " + s2)
                self.listWidget.addItem(item)
                self.typeStack[i]="1"
        self.jumpToMessage1()

    def onItemDoubleClick(self,s):
        index = self.listWidget.currentRow()
        type=self.typeStack[index]
        mid = self.midStack[index]
        self.hasShow = not self.hasShow
        if self.hasShow == False:
            if s==0:
                s1="是否不再显示此消息!"
                s2=3
            else:
                s1="是否同意加入该公司"
                s2=2
            reply = QMessageBox.information \
                (self.frame, "Question", s1, QMessageBox.Yes | QMessageBox.No)
            if reply==QMessageBox.Yes:
                arr = []
                arr.append(mid)
                arr.append(type)
                arr.append(s2)
                res = Connect.sendJSON("/read", {"id": mid})
                if res["msg"] == "ok":
                    self.onPushButton_4Click()

    def onItemClick(self):
        print(self.listWidget.currentRow())
        print(self.typeStack)
        print(self.midStack)
        if self.typeStack[self.listWidget.currentRow()]=="2":
            self.jumpToMessage2()

    def onPushButton_5Click(self):
        self.jumpToLeave()

    def onPushButton_6Click(self):
        arr = []
        arr.append(self.lineEdit_2.text())
        arr.append(self.lineEdit_4.text())
        Connect.sendJSON("/addCompany", SendJSON.getAddCompanyJSON(arr))

    def onPushButton_9Click(self):
        arr = []
        arr.append(self.comboBox.currentText())
        arr.append(self.dateEdit.text() + " " + self.timeEdit.text())
        arr.append(self.dateEdit_2.text() + " " + self.timeEdit_2.text())
        arr.append(self.plainTextEdit.toPlainText())
        res = Connect.sendJSON("/leave", SendJSON.getLeaveJSON(arr))
        if res["msg"] != "ok":
            self.hasShow = not self.hasShow
            if self.hasShow == False:
                err = QtWidgets.QErrorMessage(self.frame)
                err.setStyleSheet("color:red;background:white;")
                err.showMessage("发送失败！")
        else:
            self.hasShow = not self.hasShow
            if self.hasShow == False:
                err = QtWidgets.QErrorMessage(self.frame)
                err.setStyleSheet("color:green;background:white;")
                err.showMessage("发送成功！")

    def onPushButton_10Click(self):
        arr = []
        arr.append(self.dateEdit_3.text())
        res = Connect.sendJSON("/attend", SendJSON.getAttendJSON(arr))
        if res["msg"] == "ok":
            return  # 待完善
        else:
            self.hasShow = not self.hasShow
            if self.hasShow == False:
                err = QtWidgets.QErrorMessage(self.frame)
                err.setStyleSheet("color:red;background:white;")
                err.showMessage("查询失败！")

    def onPushButton_13Click(self):
        self.jumpToHome()

    def onPushButton_14Click(self):
        if self.checkBox.isChecked():
            self.onItemDoubleClick(1)
        self.jumpToMessage1()


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
        arr = []
        arr.append(self.label_55.text()[13:len(self.label_55.text())])
        arr.append("0")
        arr.append("0")
        res = Connect.sendJSON("/modify", SendJSON.getModifyJSON(arr))
        print(res)
        if res["msg"] != "ok":
            self.label_55.setText("昵称")

    def onLabel_8Click(self):
        self.sexDialog()
        arr = []
        arr.append("")
        arr.append(self.label_56.text()[13:len(self.label_56.text())])
        arr.append("")
        res = Connect.sendJSON("/modify", SendJSON.getModifyJSON(arr))
        print(res)
        if res["msg"] != "ok":
            self.label_56.setText("性别")

    def onLabel_9Click(self):
        if True == self.setAge(None):
            arr = []
            arr.append("")
            arr.append("")
            arr.append(self.label_57.text()[13:len(self.label_57.text())])
            res = Connect.sendJSON("/modify", SendJSON.getModifyJSON(arr))
            if res["msg"] != "ok":
                self.label_57.setText("生日")
                self.label_58.setText("年龄")

        # </editor-fold>

        # <editor-fold desc="jump事件">

    def sexDialog(self):
        self.hasShow = not self.hasShow
        if self.hasShow == False:
            items = ('男', '女')
            item, ok = QtWidgets.QInputDialog.getItem \
                (self.stackedWidget, "性别", '性别', items, False)
            if ok and item:
                self.label_56.setText("性别:          " + item)

    def nameDialog(self):
        self.hasShow = not self.hasShow
        if self.hasShow == False:
            text, ok = QtWidgets.QInputDialog.getText \
                (self.stackedWidget, '昵称', '输入昵称：')
            if ok:
                self.label_55.setText("昵称:          " + str(text))

    def judgeDateIsRight(self, date):
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
                        born = year + '-' + month + '-' + day
                        if self.judgeDateIsRight(born) == False:
                            err = QtWidgets.QErrorMessage(self.stackedWidget)
                            err.showMessage("输入的日期不合法！")
                        else:
                            self.label_57.setText("生日:          " + born)
                            return year + month + day

    def calculate_age(self, birth_s):
        birth_d = datetime.strptime(birth_s, "%Y%m%d")
        today_d = datetime.now()
        birth_t = birth_d.replace(year=today_d.year)
        if today_d > birth_t:
            age = today_d.year - birth_d.year
        else:
            age = today_d.year - birth_d.year - 1

        return age

    def setAge(self, born):
        if born == None:
            born = self.birthDialog()
        if born != None:
            age = self.calculate_age(born)
            self.label_58.setText('年龄:          ' + str(age))
            return True
        return False

    def jumpToHome(self):
        if (self.hasRun == False):
            self.MyJump()
            self.hasRun = True
        self.stackedWidget.setCurrentIndex(0)

    def jumpToModify1(self):
        if (self.hasRun == False):
            self.MyJump()
            self.hasRun = True
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
        self.hasRun = False
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
        self.WidgetStack[0].hide()

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

