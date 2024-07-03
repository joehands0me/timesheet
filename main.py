import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("deltek_bot.ui", self)


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("deltek_bot.ui")
window = MainWindow()
window.show()
app.exec()
