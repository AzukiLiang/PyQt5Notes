from PyQt5 import QtWidgets, QtCore, QtGui
from _butthonsTest import Ui_MainWindow
import sys
from PyQt5.QtCore import pyqtSlot
from functools import wraps


class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.setShortcut('Alt+D')
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setArrowType(QtCore.Qt.UpArrow)
        self.commandLinkButton.setText("www.baidu.com")
        self.checkBox.setTristate()
        self.checkBox.setCheckState(QtCore.Qt.PartiallyChecked)

        self.pushButton.clicked.connect(self.printLogit)
        self.toolButton.clicked.connect(self.printLogit)
        self.commandLinkButton.clicked.connect(self.printLogit)
        self.radioButton.clicked.connect(self.printLogit)
        self.radioButton_2.clicked.connect(self.printLogit)
        self.radioButton_3.clicked.connect(self.printLogit)
        self.checkBox.clicked.connect(self.printLogit)

    # @pyqtSlot()
    # def on_pushButton_clicked(self):
    #     butStr = self.sender().objectName() + ' has been clicked'
    #     print(butStr)


    def printLogit(self):
        butStr = self.sender().objectName() + ' has been clicked'
        print(butStr)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
