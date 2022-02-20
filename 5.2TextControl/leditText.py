from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from _leditTest import Ui_MainWindow


class leditTestWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(leditTestWindow, self).__init__(parent)
        self.setupUi(self)
        # self.lineEdit.setText('这是一个LineText控件测试')

        # 导入文本校验器： 整数校验器、浮点数校验器与其他自定义校验器
        from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator

        self.lineEditInt.setPlaceholderText('请在此处输入1~99的整数')
        # 实例化整形验证器，并设置范围为1-99，并在lineEditInt控件中设置该验证器
        intValidator = QIntValidator()
        intValidator.setRange(1, 99)
        self.lineEditInt.setValidator(intValidator)

        self.lineEditDouble.setPlaceholderText('请在此处输入-180~180的两位小数')
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-180, 180)
        # The string is written as a standard number (i.e. 0.015)， not in scientific form
        # While you want to use scientific form, you'd better use QDoubleValidator.ScientificNotation(i.e. 1.5E-2)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置浮点型校验器保留两位小数
        doubleValidator.setDecimals(2)
        self.lineEditDouble.setValidator(doubleValidator)

        self.lineEditRegExp.setPlaceholderText('请在此处输入邮箱')
        # The QRegExp class provides pattern matching using regular expressions
        from PyQt5.QtCore import QRegExp
        reg = QRegExp('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
        regExpValidator = QRegExpValidator(self)
        regExpValidator.setRegExp(reg)
        self.lineEditRegExp.setValidator(regExpValidator)

        self.dataMaskLiedt.installEventFilter(self)
        self.dataMaskLiedt.setPlaceholderText('请输入日期：形如xxxx-xx-xx')

        self.timeMaskLiedt.setInputMask('00:00:00')
        self.SenMaskLiedt.setInputMask('>AAAA-AAAA-AAAA-0000')

        self.pushButton.clicked.connect(self.showMessage)

    def showMessage(self):
        from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
        # 使用information()方法弹出信息提示
        QMessageBox.information(ledittest, "提示框", self.dataMaskLiedt.text(), QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)

    def setDataMask(self):
        # print(self.dataMaskLiedt.text())
        # self.dataMaskLiedt.setInputMask('0000-00-00')
        self.dataMaskLiedt.setPlaceholderText('请输入日期：形如xxxx-xx-xx')

    # 事件过滤器，借此可以给lineEdit控件新增焦点进入和焦点失去的事件
    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a0 == self.dataMaskLiedt:
            if a1.type() == QEvent.FocusIn:
                print(111)
                self.dataMaskLiedt.setInputMask('0000-00-00')
                return True
            elif a1.type() == QEvent.FocusOut:
                if self.dataMaskLiedt.text() == '--':
                    print(222)
                    self.dataMaskLiedt.setInputMask('')
                    print(self.dataMaskLiedt.text())
                    self.dataMaskLiedt.setPlaceholderText('请输入日期：形如xxxx-xx-xx')
                    return True
            return False
        return False


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ledittest = leditTestWindow()
    ledittest.show()
    sys.exit(app.exec_())  # paladina
