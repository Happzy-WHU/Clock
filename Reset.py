# -*- coding: utf-8 -*-


from PyQt5.QtCore import QRect,QMetaObject,QCoreApplication,QSize
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QFrame,QLabel,QPushButton,QLineEdit,QToolButton



from src import resources

class Ui_Reset(object):
    def __init__(self, WidgetStack, UIStack):
        self.WidgetStack = WidgetStack
        self.UIStack = UIStack

    WidgetStack = None
    UIStack = None

    def setupUi(self, reset):
        reset.setObjectName("reset")
        reset.resize(1013, 772)
        reset.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"}\n"
"#reset{ \n"
"    background: url(:/resources/background.jpg)\n"
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
        self.frame = QFrame(reset)
        self.frame.setGeometry(QRect(240, 120, 491, 521))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setGeometry(QRect(50, 180, 351, 41))
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QRect(50, 300, 351, 41))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(170, 80, 101, 41))
        self.label.setObjectName("label")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(120, 410, 231, 41))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QToolButton(reset)
        self.toolButton.setGeometry(QRect(420, 40, 131, 121))
        self.toolButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/resources/people.png"), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(64, 64))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(reset)
        QMetaObject.connectSlotsByName(reset)

    def retranslateUi(self, reset):
        _translate = QCoreApplication.translate
        reset.setWindowTitle(_translate("reset", "Form"))
        self.lineEdit.setPlaceholderText(_translate("reset", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("reset", "Verify Pssword"))
        self.label.setText(_translate("reset", "设置密码"))
        self.pushButton.setText(_translate("reset", "确 认"))

        self.pushButton.clicked.connect(lambda:self.onPushButtonClick())

    def onPushButtonClick(self):
        self.jumpToLogin()

    def jumpToLogin(self):
        hasFind = False
        import src.Login
        self.WidgetStack[4].hide()
        
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
