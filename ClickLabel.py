from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtWidgets import QLabel
class ClickLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()