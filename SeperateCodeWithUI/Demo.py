from PyQt5 import QtWidgets, QtGui, QtCore
from ui_Demo import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMessage)

    def showMessage(self):
        from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
        # 使用information()方法弹出信息提示
        QMessageBox.information(mainWindow, "提示框", "欢迎进入PyQt5编程世界", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # 设置窗口风格
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
