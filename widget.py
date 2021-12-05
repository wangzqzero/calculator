## This Python file uses the following encoding: utf-8

from PyQt5.QtWidgets import *
from mainwindow import MainWindow
from call_standard import StandardPageWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

