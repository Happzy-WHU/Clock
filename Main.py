#coding=utf-8
from src import resources

from PyQt5 import QtCore, QtGui, QtWidgets
import src.Login

import sys
UIStack = []

app=QtWidgets.QApplication(sys.argv)
LoginWidget = QtWidgets.QWidget()
HomeWidget = QtWidgets.QWidget()
PasswordWidget = QtWidgets.QWidget()
RegisterWidget = QtWidgets.QWidget()
ResetWidget = QtWidgets.QWidget()


WidgetStack = []
WidgetStack.append(HomeWidget)
WidgetStack.append(LoginWidget)
WidgetStack.append(PasswordWidget)
WidgetStack.append(RegisterWidget)
WidgetStack.append(ResetWidget)


ui=src.Login.Ui_Login(WidgetStack,UIStack)    #这里改成你自己的项目名称，如果你没特意改过，就默认就行
ui.setupUi(LoginWidget)
ui.retranslateUi(LoginWidget)

UIStack.append(ui)
print(len(UIStack))

LoginWidget.show()
sys.exit(app.exec_())

LoginWidget.show()
sys.exit(app.exec_())