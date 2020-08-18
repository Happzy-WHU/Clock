from PyQt5 import  QtWidgets,QtCore
class ClickList(QtWidgets.QListWidget):
    def __init__(self):
        QtWidgets.QListWidget.__init__(self)
        self.add_items()
        self.itemClicked.connect(self.item_click)

    def add_items(self):
        for item_text in ['item1', 'item2', 'item3']:
            item = QtWidgets.QListWidgetItem(item_text)
            self.addItem(item)

    def item_click(self, item):
        print
        item, str(item.text())