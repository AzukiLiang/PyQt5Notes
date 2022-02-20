from PyQt5 import QtWidgets

import second
import third
from first import Ui_MainWindow


class secondWindow(QtWidgets.QMainWindow, second.Ui_MainWindow):

    def __init__(self, parent=None):
        super(secondWindow, self).__init__(parent)
        self.setupUi(self)


class thirdWindow(QtWidgets.QMainWindow, third.Ui_MainWindow):

    def __init__(self, parent=None):
        super(thirdWindow, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open)

    def open(self):
        self.second = secondWindow()
        self.second.show()
        self.third = thirdWindow()
        self.third.show()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
