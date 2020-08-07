from PyQt5 import QtWidgets,QtCore
class ClickLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()