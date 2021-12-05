# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from programmer import Ui_programmer
from PyQt5.QtCore import pyqtSignal,Qt

class ProgrammerPageWindow(QWidget,Ui_programmer):
 #定义点击信号
    chooseSignal = pyqtSignal(str)
    def __init__(self,parent=None):
        super(ProgrammerPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
#        self.setLayout(self.gridLayout)
        self.selectwindow.currentIndexChanged.connect(self.showDialog)

    def showDialog(self):
        ss = self.selectwindow.currentText()
        if ss == 'time':
 #发射点击信号
            self.chooseSignal.emit('time')
        elif ss == 'standard':
            self.chooseSignal.emit('standard')
        elif ss == 'graph':
            self.chooseSignal.emit('graph')
        elif ss == 'scientific':
            self.chooseSignal.emit('scientific')
        elif ss == 'programmer':
            self.chooseSignal.emit('programmer')

