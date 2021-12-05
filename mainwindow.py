from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from call_graph import GraphPageWindow
from call_time import TimePageWindow
from call_standard import StandardPageWindow
from call_scientific import ScientificPageWindow
#from call_programmer import ProgrammerPageWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(470,630)
        self.setFixedSize(470,630)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.layout.setContentsMargins(0,0,0,0)
        self.Stack = QStackedWidget()
        self.layout.addWidget(self.Stack)
        self.timePageUi = TimePageWindow()
        self.graphPageUi = GraphPageWindow()
        self.standardPageUi = StandardPageWindow()
        self.scientificPageUi = ScientificPageWindow()
#        self.programmerPageUi = ProgrammerPageWindow()

        self.Stack.addWidget(self.standardPageUi)
        self.Stack.addWidget(self.scientificPageUi)
        self.Stack.addWidget(self.timePageUi)
        self.Stack.addWidget(self.graphPageUi)
#        self.Stack.addWidget(self.programmerPageUi)

        self.scientificPageUi.chooseSignal.connect(self.showDialog)
        self.timePageUi.chooseSignal.connect(self.showDialog)
        self.graphPageUi.chooseSignal.connect(self.showDialog)
        self.standardPageUi.chooseSignal.connect(self.showDialog)
#        self.programmerPageUi.chooseSignal.connect(self.showDialog)

    def showDialog(self,msg):
        if msg == 'standard':
            self.Stack.setCurrentIndex(0)
            self.standardPageUi.displayclear()
            self.standardPageUi.selectwindow.setCurrentIndex(0)
        elif msg == 'scientific':
            self.Stack.setCurrentIndex(1)
            self.scientificPageUi.selectwindow.setCurrentIndex(1)
            self.scientificPageUi.displayclear()
        elif msg == 'time':
            self.Stack.setCurrentIndex(2)
            self.timePageUi.selectwindow.setCurrentIndex(3)
        elif msg == 'graph':
            self.Stack.setCurrentIndex(3)
            self.graphPageUi.selectwindow.setCurrentIndex(2)
        elif msg == 'programmer':
            self.Stack.setCurrentIndex(4)
            self.programmerPageUi.selectwindow.setCurrentIndex(3)
