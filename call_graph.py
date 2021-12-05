# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from graph import Ui_graph
from PyQt5.QtCore import pyqtSignal,Qt
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
#from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout


class Graph(QtWidgets.QMainWindow): #Auxiliary class to display pop-up for inputting range
    def __init__(self,parent = None):
        super(Graph, self).__init__(parent)
        page = QWidget()
        page.setMinimumSize(QSize(350, 320))
        page.setWindowTitle("Enter range")
        page.start = QLabel(page)
        page.start.setText('Start:')
        page.end = QLabel(page)
        page.end.setText('End:')
        page.step = QLabel(page)
        page.step.setText('Step size:')
        self.button = QPushButton('Plot', page)
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit1.move(80,20)
        page.start.move(20,15)
        self.edit1.move(80,80)
        page.end.move(20,85)
        self.edit1.move(80,140)
        page.step.move(20,145)
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.edit1)
        vbox1.addWidget(self.edit2)
        vbox1.addWidget(self.edit3)
        vbox1.addWidget(self.button)
        page.setLayout(vbox1)
        self.setCentralWidget(page)
        self.button.clicked.connect(lambda:self.clicked())

    def clicked(self):
        l = float(self.edit1.text())
        r = float(self.edit2.text())
        s = float(self.edit3.text())
        x = np.arange(l,r,s)
        print(x)
        s = GraphPageWindow.var
        print("In Second")
        print(s)
        y = eval(s)
        pg.setConfigOption('background', 'w')      # sets background white
        pg.setConfigOption('foreground', 'k')      # sets axis color to black
        pw = pg.plot(x,y,pen = 'k')
        pw.setTitle('y = f(x)')
        pw.setLabel('bottom', 'x -->')           	# x-label
        pw.setLabel('left', 'y = f(x) -->')             # y-label

class GraphPageWindow(Ui_graph,QtWidgets.QMainWindow):
        chooseSignal = pyqtSignal(str)
        def __init__(self):
            super(GraphPageWindow, self).__init__()
            self.setupUi(self)
            self.b0.clicked.connect(lambda:self.display_screen('0'))
            self.b0.clicked.connect(lambda:self.storage('0',1))
            self.b1.clicked.connect(lambda:self.display_screen('1'))
            self.b1.clicked.connect(lambda:self.storage('1',1))
            self.b2.clicked.connect(lambda:self.display_screen('2'))
            self.b2.clicked.connect(lambda:self.storage('2',1))
            self.b3.clicked.connect(lambda:self.display_screen('3'))
            self.b3.clicked.connect(lambda:self.storage('3',1))
            self.b4.clicked.connect(lambda:self.display_screen('4'))
            self.b4.clicked.connect(lambda:self.storage('4',1))
            self.b5.clicked.connect(lambda:self.display_screen('5'))
            self.b5.clicked.connect(lambda:self.storage('5',1))
            self.b6.clicked.connect(lambda:self.display_screen('6'))
            self.b6.clicked.connect(lambda:self.storage('6',1))
            self.b7.clicked.connect(lambda:self.display_screen('7'))
            self.b7.clicked.connect(lambda:self.storage('7',1))
            self.b8.clicked.connect(lambda:self.display_screen('8'))
            self.b8.clicked.connect(lambda:self.storage('8',1))
            self.b9.clicked.connect(lambda:self.display_screen('9'))
            self.b9.clicked.connect(lambda:self.storage('9',1))
            self.decimal.clicked.connect(lambda:self.display_screen('.'))
            self.decimal.clicked.connect(lambda:self.storage('.',1))
            self.add.clicked.connect(lambda:self.display_screen(' + '))
            self.add.clicked.connect(lambda:self.storage(' + ',1))
            self.substract.clicked.connect(lambda:self.display_screen(' - '))
            self.substract.clicked.connect(lambda:self.storage(' - ',1))
            self.plus_minus.clicked.connect(lambda:self.display_screen('-'))
            self.plus_minus.clicked.connect(lambda:self.storage('-',1))
            self.multiply.clicked.connect(lambda:self.display_screen(' X '))
            self.multiply.clicked.connect(lambda:self.storage(' * ',1))
            self.divide.clicked.connect(lambda:self.display_screen(' / '))
            self.divide.clicked.connect(lambda:self.storage(' / ',1))
            self.log.clicked.connect(lambda:self.display_screen(' log( '))
            self.log.clicked.connect(lambda:self.storage(' np.log10(',1))
            self.ln.clicked.connect(lambda:self.display_screen(' ln( '))
            self.ln.clicked.connect(lambda:self.storage(' (np.log10(math.e))**(-1) * np.log10( ',1))
            self.pi.clicked.connect(lambda:self.display_screen('pi'))
            self.pi.clicked.connect(lambda:self.storage('np.pi',1))
            self.e.clicked.connect(lambda:self.display_screen('e'))
            self.e.clicked.connect(lambda:self.storage('np.e',1))
            self.b_open.clicked.connect(lambda:self.display_screen(' ( '))
            self.b_open.clicked.connect(lambda:self.storage(' ( ',1))
            self.sin.clicked.connect(lambda:self.display_screen(' sin( '))
            self.sin.clicked.connect(lambda:self.storage(' np.sin( ',1))
            self.cos.clicked.connect(lambda:self.display_screen(' cos( '))
            self.cos.clicked.connect(lambda:self.storage(' np.cos( ',1))
            self.tan.clicked.connect(lambda:self.display_screen(' tan( '))
            self.tan.clicked.connect(lambda:self.storage(' np.tan( ',1))
            self.sq_root.clicked.connect(lambda:self.display_screen(' sqrt( '))
            self.sq_root.clicked.connect(lambda:self.storage(' math.sqrt( ',1))
            self.sin1.clicked.connect(lambda:self.display_screen(' arcsin( '))
            self.sin1.clicked.connect(lambda:self.storage('math.asin( ',1))
            self.cos1.clicked.connect(lambda:self.display_screen(' arccos( '))
            self.cos1.clicked.connect(lambda:self.storage(' math.acos( ',1))
            self.tan1.clicked.connect(lambda:self.display_screen(' arctan( '))
            self.tan1.clicked.connect(lambda:self.storage(' math.atan( ',1))
            self.power.clicked.connect(lambda:self.display_screen(' ^ '))
            self.power.clicked.connect(lambda:self.storage(' ** ',1))
            self.b_close.clicked.connect(lambda:self.display_screen(' ) '))
            self.b_close.clicked.connect(lambda:self.storage(' ) ',1))
            self.clear.clicked.connect(self.display.clear)
            self.clear.clicked.connect(lambda:self.storage("",3))
            self.back.clicked.connect(self.display.clear)
            self.back.clicked.connect(lambda:self.display_screen2(self.prev_disp))
            self.back.clicked.connect(lambda:self.storage1(self.store))
            self.equal.clicked.connect(self.calculation)
            self.x.clicked.connect(lambda:self.display_screen(' x '))
            self.x.clicked.connect(lambda:self.storage(' x ',1))
            self.plot.clicked.connect(self.plott)
            self.display.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:black;")
            self.display.setReadOnly(True)
            self.display.setAlignment(QtCore.Qt.AlignRight)
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
        var = ""
        store= ""
        prev_disp = ""
        stack = []
        stack_disp = []
        temp = []
        flag = 0
        def graphing(self):
            self.flag = 1
            print("Welcome to graphs")
            print("Enter the equation f(x) : ")
            self.display.setText("Enter the equation f(x) : ")
            self.store = ""
        def plott(self):
            x = np.arange(1,2,0.1) #Just to check if equation enter for plotting is syntactically correct or not
            try:
                y = eval(self.store)
            except SyntaxError:
                print("Improper Equation entered")
                self.display.setText("Improper Equation entered")
            else:
                GraphPageWindow.var = self.store
                self.dialog = Graph(self)	#Calling the Graph class to display a Range requesting pop-up
                self.dialog.setWindowTitle('Please Enter Range of y = f(x)')
                print(self.store)
                self.dialog.show()

        def storage1(self,value):
            try:
                self.stack.pop()
            except IndexError:
                self.store = ""
            else:
                self.temp = self.stack
                self.store = ''.join(self.temp)

        def storage(self,value,k):
            if k is 1 :
                self.store=self.store + value
            elif k is 3:
                self.flag = 0
                self.stack=[]
                self.stack_disp=[]
                self.store=""
            print (self.store)
            self.stack.append(value)

        def display_screen(self,value):
            self.display.insert(value)
            self.stack_disp.append(value)

        def display_screen1(self,value):
            self.display.setText(value)
            self.stack_disp.append(value)

        def display_screen2(self,value):
            try:
                self.stack_disp.pop()
            except IndexError:
                self.display_screen1("")
                self.flag = 0
            else:
                if(self.flag == 1):
                    self.display.setText("Enter the equation f(x) : ")
                    self.temp = self.stack_disp
                    value = ''.join(self.temp)
                    self.display.insert(value)
                else:
                    self.temp = self.stack_disp
                    value = ''.join(self.temp)
                    self.display.setText(value)

        def display_error(self,value):
            self.display.setText(value)
            self.stack_disp.append(value)

        def disp_res(self,value):
            self.display.setText(value)
            self.stack_disp.append(value)

        def calculation(self):
            screen_value=self.store
            screen_value=str(screen_value)
            print(''.join(self.stack))
            try:
                i = 0
                while i < len(screen_value):
                    print(f"i1: {i}")
                    i = screen_value.find("1j",i)
                    print(f"i: {i}")
                    if i == -1:
                        print("Nothing complex")
                        break
                    elif(i == 0 or screen_value[i-1] < '0' or screen_value[i-1] > '9'):
                        print("Okay only 1j")
                    else:
                        if(i):
                            screen_value = screen_value[:i] + screen_value[i+1:]
                    i += 2
                print(f"final_value:  {screen_value}")
                final_value=eval(screen_value)
            except ZeroDivisionError:
                print("Math Error : Division by Zero")
                self.stack.append('#') #Done so as to pop once in order to remove the error message from disp and secondly to pop the wrong input
                self.display_error("Math Error : Division by Zero")
            except ValueError:
                print("Math Error :No negatives in sqrt/log ,cos-1 & sin-1 b/w -1 & 1")
                self.stack.append('#')
                self.display_error("Math Error :No negatives in sqrt/log ,cos-1 & sin-1 b/w -1 & 1 ")
            except SyntaxError:
                print("Improper equation entered")
                self.stack.append('#')
                self.display_error("Improper equation entered")
            except AttributeError:
                print("Input Error : Please enter proper input")
                self.stack.append('#')
                self.display_error("Input Error : Please enter proper input")
            else:
                final_value=str(final_value)
                self.store=final_value
                self.stack.append(final_value)
                print(self.store)
                self.disp_res(" = " + final_value)

#class Graph(QtWidgets.QMainWindow): #Auxiliary class to display pop-up for inputting range
#    def __init__(self,parent = None):
#        super(Graph, self).__init__(parent)
#        page = QWidget()
#        page.setMinimumSize(QSize(350, 320))
#        page.setWindowTitle("Enter range")
#        page.start = QLabel(page)
#        page.start.setText('Start:')
#        page.end = QLabel(page)
#        page.end.setText('End:')
#        page.step = QLabel(page)
#        page.step.setText('Step size:')
#        self.button = QPushButton('Plot', page)
#        self.edit1 = QLineEdit()
#        self.edit2 = QLineEdit()
#        self.edit3 = QLineEdit()
#        self.edit1.move(80,20)
#        page.start.move(20,15)
#        self.edit1.move(80,80)
#        page.end.move(20,85)
#        self.edit1.move(80,140)
#        page.step.move(20,145)
#        vbox1 = QVBoxLayout()
#        vbox1.addWidget(self.edit1)
#        vbox1.addWidget(self.edit2)
#        vbox1.addWidget(self.edit3)
#        vbox1.addWidget(self.button)
#        page.setLayout(vbox1)
#        self.setCentralWidget(page)
#        self.button.clicked.connect(lambda:self.clicked())

#    def clicked(self):
#        l = float(self.edit1.text())
#        r = float(self.edit2.text())
#        s = float(self.edit3.text())
#        x = np.arange(l,r,s)
#        print(x)
#        s = GraphPageWindow.var
#        print("In Second")
#        print(s)
#        y = eval(s)
#        pg.setConfigOption('background', 'w')      # sets background white
#        pg.setConfigOption('foreground', 'k')      # sets axis color to black
#        pw = pg.plot(x,y,pen = 'k')
#        pw.setTitle('y = f(x)')
#        pw.setLabel('bottom', 'x -->')           	# x-label
#        pw.setLabel('left', 'y = f(x) -->')             # y-label

#class GraphPageWindow(QWidget,Ui_graph):
# #定义点击信号
#    chooseSignal = pyqtSignal(str)
#    def __init__(self,parent=None):
#        super(GraphPageWindow, self).__init__(parent)
#        self.setupUi(self)
#        self.initUI()

#    def initUI(self):
#        self.selectwindow.currentIndexChanged.connect(self.showDialog)
#        self.display.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:black;")
#        self.display.setReadOnly(True)
#        self.display.setAlignment(QtCore.Qt.AlignRight)
#        self.chan.clicked.connect(lambda:self.change())
#        self.d0.clicked.connect(lambda:self.storage('0'))
#        self.d1.clicked.connect(lambda:self.storage('1'))
#        self.d2.clicked.connect(lambda:self.storage('2'))
#        self.d3.clicked.connect(lambda:self.storage('3'))
#        self.d4.clicked.connect(lambda:self.storage('4'))
#        self.d5.clicked.connect(lambda:self.storage('5'))
#        self.d6.clicked.connect(lambda:self.storage('6'))
#        self.d7.clicked.connect(lambda:self.storage('7'))
#        self.d8.clicked.connect(lambda:self.storage('8'))
#        self.d9.clicked.connect(lambda:self.storage('9'))
#        self.point.clicked.connect(lambda:self.storage('.'))
#        self.sub.clicked.connect(lambda:self.storage('-'))
#        self.add.clicked.connect(lambda:self.storage('+'))
#        self.mul.clicked.connect(lambda:self.storage('*'))
#        self.divi.clicked.connect(lambda:self.storage('/'))
#        self.ant.clicked.connect(lambda:self.storage1('np.negative(','',0))
#        self.x.clicked.connect(lambda:self.storage('x'))
#        self.y.clicked.connect(lambda:self.storage('y'))
#        self.lef.clicked.connect(lambda:self.storage('('))
#        self.rig.clicked.connect(lambda:self.storage(')'))
#        self.abso.clicked.connect(lambda:self.storage1('abs(','',0))
#        self.pi.clicked.connect(lambda:self.storage('np.pi'))
#        self.e.clicked.connect(lambda:self.storage('np.e'))
#        self.rand.clicked.connect(lambda:self.storage('rand'))
#        self.equ.clicked.connect(lambda:self.calculation())
#        self.back.clicked.connect(lambda:self.change_click(0))
#        self.sin.clicked.connect(lambda:self.change_click(1))
#        self.cos.clicked.connect(lambda:self.change_click(2))
#        self.tan.clicked.connect(lambda:self.change_click(3))
#        self.sqrt.clicked.connect(lambda:self.change_click(4))
#        self.extract.clicked.connect(lambda:self.change_click(5))
#        self.inde.clicked.connect(lambda:self.change_click(6))
#        self.tind.clicked.connect(lambda:self.change_click(7))
#        self.log.clicked.connect(lambda:self.change_click(8))
#        self.ln.clicked.connect(lambda:self.change_click(9))
#        self.c.clicked.connect(lambda:self.displayclear())
#        self.ce.clicked.connect(lambda:self.clear_enter())
#        self.dele.clicked.connect(lambda:self.clear_back())
#        self.plot.clicked.connect(self.plott)

#    var = ""
#    store= ""
#    mid = ""
#    middle = []
#    symbel = []
#    open = []
#    close = -1
#    p = 0 #point
#    left = 0 #left bracket
#    state = 0 #the number state of last number
#    s = 0  #flag last input is or not is symbel
#    calcul = 0
#    replace = 0


#    def showDialog(self):
#        print("change")
#        ss = self.selectwindow.currentText()
#        if ss == 'time':
# #发射点击信号
#            self.chooseSignal.emit('time')
#        elif ss == 'standard':
#            self.chooseSignal.emit('standard')
#        elif ss == 'graph':
#            self.chooseSignal.emit('graph')
#        elif ss == 'scientific':
#            self.chooseSignal.emit('scientific')
#        elif ss == 'programmer':
#            self.chooseSignal.emit('programmer')

#    def storage(self,value):
#        if value > '0' and value <= '9':
#            if self.state == 2:
#                self.state = 0
#            if self.mid == ')':
#                self.middle = self.middle[0:self.close]
#                self.close = self.open[-1]
#                self.open.pop()
#            if self.mid == '(':
#                self.middle.append(self.mid)
#                self.close = -1
#            if self.state == 1:
#                self.state = 0
#                self.mid = ""
#            if self.s == 1:
#                self.middle.append(self.mid)
#                self.mid = ""
#                self.s = 0
#            if len(self.mid) > 0 and self.p == 0:
#                if self.mid == '(' or self.mid == ')':
#                    self.mid = value
#                elif eval(self.mid) == 0:
#                    self.mid = value
#                else:
#                    self.mid = self.mid + value
#            else:
#                self.mid = self.mid + value
#            self.display_screen(self.mid)
#        elif value == '-' or value == '+' or value == '*' or value == '/':
#            if self.state == 2:
#                del self.middle[self.replace]
#                self.open.remove(self.replace)
#                self.dmov_open(self.replace)
#                self.state = 0
#                self.middle.pop()
#                self.s = 1
#                return
#            elif self.mid == '(':
#                self.middle.append(self.mid)
#                self.middle.append('0')
#                self.close = -1
#            elif self.mid == ')':
#                self.middle.append(self.mid)
#                self.close = self.open[-1]
#                self.open.pop()
#                if self.state == 1:
#                    self.state = 0
#            elif len(self.mid) > 0 and self.s == 0:
#                if self.state == 1:
#                    self.state = 0
#                self.middle.append(self.mid)
#            if len(self.middle) > 0:
#                self.store = self.display0_show()
#                if self.s == 0:
#                    self.mid = value
#                    self.s = 1
#                elif self.s == 1:
#                    self.mid = value
#        elif value == '.':
#            if self.mid == ')':
#                self.middle = self.middle[0:self.close]
#                self.close = self.open[-1]
#                self.open.pop()
#            elif self.mid == '(':
#                self.middle.append(self.mid)
#                self.close = -1
#            if self.p == 0:
#                if len(self.mid) == 0 or self.state == 1:
#                    self.mid = "0"
#                    self.state = 0
#                self.mid = self.mid + value
#                self.p = 1
#            self.display_screen(self.mid)
#        elif value == '0':
#            if self.state == 2:
#                self.state = 0
#            elif self.mid == ')':
#                self.middle = self.middle[0:self.close]
#                self.close = self.open[-1]
#                self.open.pop()
#                self.mid = ''
#            elif self.mid == '(':
#                self.middle.append(self.mid)
#                self.close = -1
#                self.mid = ''
#            elif self.state == 1:
#                self.state = 0
#                self.mid = ""
#            elif self.s == 1:
#                self.middle.append(self.mid)
#                self.mid = ""
#                self.s = 0
#            if len(self.mid) == 0:
#                self.mid = self.mid + value
#            elif len(self.mid) != 0 and eval(self.mid) > 0 and self.p == 0:
#                self.mid = self.mid + value
#            elif len(self.mid) != 0 and self.p == 1:
#                self.mid = self.mid + value
#            self.display_screen(self.mid)
#        elif value == '(':
#            if self.state == 2:
#                self.open.append(len(self.middle))
#                self.middle.append(value)
#                self.state = 0
#                self.mid = '('
#                return
#            if len(self.mid) > 0:
#                if self.mid == ')':
#                    self.middle = self.middle[0:self.close]
#                    self.open.append(self.close)
#                    self.mid = '('
#                    self.close = -1
#                elif self.mid == '(' or self.s == 1:
#                    self.open.append(len(self.middle))
#                    self.middle.append('(')
#                    self.close = -1
#                elif self.state == 0 and self.s == 0:
#                    self.open.append(len(self.middle))
#                    self.middle.append('(')
#                    self.state = 1
#                    self.close = -1
#                elif self.state == 1:
#                    self.open.append(len(self.middle))
#                    self.middle.append(value)
#                    self.close = -1
#            else:
#                if len(self.middle) == 0:
#                    self.mid = value
#                    self.open.append(0)
#                elif self.middle[-1] == '(' or self.middle[-1] == '+' or self.middle[-1] == '-' or self.middle[-1] == '*' or self.middle[-1] == '/':
#                    self.close = -1
#                    self.mid = value
#                elif self.middle[-1][-1] == ')':
#                    self.middle = self.middle[0:self.close]
#                    self.mid = value
#                    self.close = -1
#        elif value == ')':
#            if len(self.open) > 0:
#                if self.s == 1:
#                    i = self.section_calculate(self.middle[self.open[-1] + 1:-1])
#                    self.middle.append(self.mid)
#                    self.middle.append(i)
#                    self.mid = value
#                    self.close = self.open[-1]
#                elif self.mid == '(':
#                    self.middle.append(self.mid)
#                    self.middle.append('0')
#                    self.mid = value
#                    self.close = self.open[-1]
#                elif self.mid != '':
#                    if self.mid == ')':
#                        self.open.pop()
#                    self.middle.append(self.mid)
#                    self.mid = value
#                    self.close = self.open[-1]
#                elif self.mid == '':
#                    s = self.middle[-1]
#                    if s == '(':
#                        self.middle.append(0)
#                        self.mid = value
#                        self.close = self.open[-1]
#                    elif s != '+' and s != '-' and s != '*' and s != '/':
#                        self.middle.append(self.mid)
#                        self.mid = value
#                        self.close = self.open[-1]
#                    else:
#                        i = eval(self.middle[self.open[-1] + 1:-1])
#                        self.middle.append(self.mid)
#                        self.middle.append(str(i))
#                        self.close = self.open[-1]
#                        if self.mid == ')':
#                            self.open.pop()
#                        self.mid = value
#        elif value == 'np.e' or value == 'np.pi' or value == 'rand' or value == 'x':
#            if value == 'rand':
#                i = np.random.rand()
#                value = str(i)
#            if self.s == 1:
#                self.middle.append(self.mid)
#                self.mid = value
#                self.state = 1
#                self.s = 0
#            elif self.mid == '':
#                s = ''
#                if len(self.middle) > 0:
#                    s = self.middle[-1]
#                if s == ')':
#                    self.middle = self.middle[0:close]
#                    self.close = -1
#                    self.mid = value
#                    self.state = 1
#                elif s == '':
#                    self.mid = value
#                    self.state = 1
#                elif s != '(' and s != '+' and s != '-' and s != '*' and s != '/':
#                    self.mid = value
#                    self.state = 1
#                else:
#                    self.mid = value
#                    self.state = 1
#            elif self.mid == '(' or s == '+' or s == '-' or s == '*' or s == '/':
#                if self.mid == '(':
#                    self.open.append(len(self.middle))
#                    self.close = -1
#                self.middle.append(self.mid)
#                self.mid = value
#                self.state = 1
#            elif self.mid == ')':
#                self.middle = self.middle[0:close]
#                self.close = -1
#                self.mid = value
#                self.state = 1
#            elif self.mid != '':
#                self.mid = value
#                self.state = 1

#    def change(self):
#        s = self.sin.text()
#        if s == 'sin':
#            self.sin.setText('sin-1')
#            self.cos.setText('cos-1')
#            self.tan.setText('tan-1')
#            self.extract.setText('3√x')
#            self.inde.setText('y√x')
#            self.sqrt.setText('X^3')
#            self.log.setText('logyx')
#            self.ln.setText('e^x')
#            self.tind.setText('2^x')
#        else:
#            self.sin.setText('sin')
#            self.cos.setText('cos')
#            self.tan.setText('tan')
#            self.extract.setText('√x')
#            self.inde.setText('x^y')
#            self.sqrt.setText('X^2')
#            self.log.setText('log')
#            self.ln.setText('ln')
#            self.tind.setText('10^x')

#    def change_click(self,value):
#        s = self.sin.text()
#        if s == 'sin':
#            if value == 0:
#                self.storage1('1/(','',0)
#            if value == 1:
#                self.storage1('math.sin(','',0)
#            if value == 2:
#                self.storage1('math.cos(','',0)
#            if value == 3:
#                self.storage1('math.tan(','',0)
#            if value == 4:
#                self.storage1('math.pow(','2',2)
#            if value == 5:
#                self.storage1('math.pow(','(1/2)',2)
#            if value == 6:
#                self.storage2('math.pow(')
#            if value == 7:
#                self.storage1('math.pow(10,','',0)
#            if value == 8:
#                self.storage1('math.log10(','',0)
#            if value == 9:
#                self.storage1('math.log(','',0)
#        else:
#            if value == 0:
#                self.storage1('1/(','',0)
#            if value == 1:
#                self.storage1('math.arcsin(','',0)
#            if value == 2:
#                self.storage1('math.arccos(','',0)
#            if value == 3:
#                self.storage1('math.arctan(','',0)
#            if value == 4:
#                self.storage1('math.pow(','3',2)
#            if value == 5:
#                self.storage1('math.pow(','(1/3)',2)
#            if value == 6:
#                self.storage2('math.pow(')
#            if value == 7:
#                self.storage1('math.pow(2,','',0)
#            if value == 8:
#                self.storage2('math.log(')
#            if value == 9:
#                self.storage1('math.pow(np.e','',0)
#            self.change()

#    def storage1(self,s,value,k):
#        if self.state == 2:
#           j = self.middle[self.replace + 1,-1]
#           self.mid = self.section_calculate(j)
#           self.state = 0
#        if k == 0:
#            if self.mid != '' and self.state == 0:
#                if s == 'math.log10(' or s == 'math.log(':
#                    try:
#                        eval(self.mid)
#                    except:
#                        self.mid = self.mid
#                    else:
#                        if eval(self.mid) < 0:
#                            self.invalid_input()
#                            return
#                if self.s == 1:
#                    if self.mid == '+' or self.mid == '-':
#                        self.display0_show()
#                        i = eval(self.store)
#                        self.middle.append(self.mid)
#                        self.close = len(self.middle)
#                        self.open.append(self.close)
#                        self.middle.append(s)
#                        self.middle.append(str(i))
#                        self.state = 1
#                        self.s = 0
#                        self.mid = ')'
#                    else:
#                        i = self.recent_calculate(1)
#                        self.middle.append(self.mid)
#                        self.close = len(self.middle)
#                        self.open.append(self.close)
#                        self.middle.append(s)
#                        self.middle.append(i)
#                        self.state = 1
#                        self.s = 0
#                        self.mid = ')'
#                elif self.mid == '(':
#                    self.open.append(len(self.middle))
#                    self.middle.append(self.mid)
#                    self.close = len(self.middle)
#                    self.open.append(self.close)
#                    self.middle.append(s)
#                    self.middle.append('0')
#                    self.mid = ')'
#                    self.state = 1
#                elif self.mid == ')':
#                    self.mov_open(self.close)
#                    self.insert_open(self.close)
#                    self.middle.insert(self.close,s)
#                    self.middle.append(self.mid)
#                    self.open.pop()
#                    self.state = 1
#                else:
#                    self.close = len(self.middle)
#                    self.open.append(self.close)
#                    self.middle.append(s)
#                    self.middle.append(self.mid)
#                    self.mid = ')'
#                    self.state = 1
#                    self.p = 0
#            elif self.mid != '' and self.state == 1:
#                if self.mid == ')':
#                    self.mov_open(self.close)
#                    self.insert_open(self.close)
#                    self.middle.insert(self.close,s)
#                    self.middle.append(self.mid)
#                    self.open.pop()
#                else:
#                    self.close = len(self.middle)
#                    self.open.append(self.close)
#                    self.middle.append(s)
#                    self.middle.append(self.mid)
#                    self.mid = ')'
#                    self.p = 0
#            elif self.mid == '':
#                if s == 'math.log10(' or s == 'math.log(':
#                    self.invalid_input()
#                    return
#                self.close = len(self.middle)
#                self.open.append(self.close)
#                self.middle.append(s)
#                self.middle.append('0')
#                self.mid = ')'
#                self.state = 1
#        if k == 2:
#            if self.mid != '' and self.state == 0:
#                if self.s == 1:
#                    if self.mid == '+' or self.mid == '-':
#                        self.display0_show()
#                        i = eval(self.store)
#                        self.middle.append(self.mid)
#                        self.close = len(self.middle)
#                        self.open.append(self.close)
#                        self.middle.append(s)
#                        self.middle.append(str(i))
#                        self.middle.append(',')
#                        self.middle.append(value)
#                        self.state = 1
#                        self.s = 0
#                        self.mid = ')'
#                    else:
#                        i = self.recent_calculate(1)
#                        self.middle.append(self.mid)
#                        self.close = len(self.middle)
#                        self.open.append(self.close)
#                        self.middle.append(s)
#                        self.middle.append(i)
#                        self.middle.append(',')
#                        self.middle.append(value)
#                        self.state = 1
#                        self.s = 0
#                        self.mid = ')'
#                elif self.mid == '(':
#                    self.open.append(len(self.middle))
#                    self.middle.append(self.mid)
#                    self.close = len(self.middle)
#                    self.open.append(self.close)
#                    self.middle.append(s)
#                    self.middle.append('0,')
#                    self.middle.append(value)
#                    self.mid = ')'
#                    self.state = 1

#                elif self.mid == ')':
#                    self.mov_open(self.close)
#                    self.middle.insert(self.close,s)
#                    self.middle.append(self.mid)
#                    self.open.pop()
#                    self.middle.append(',')
#                    self.middle.append(value)
#                    self.state = 1
#                else:
#                    self.close = len(self.middle)
#                    self.open.append(self.close)
#                    self.middle.append(s)
#                    self.middle.append(self.mid)
#                    self.middle.append(',' + value)
#                    self.mid = ')'
#                    self.state = 1
#            elif self.mid != '' and self.state == 1:
#                if self.mid == ')':
#                    self.middle.insert(self.close,s)
#                    self.mov_open(self.close)
#                    self.insert_open(self.close)
#                    self.middle.append(self.mid)
#                    self.open.pop()
#                    self.middle.append(',' + value)
#                else:
#                    self.close = len(self.middle)
#                    self.open.append(self.close)
#                    self.middle.append(s)
#                    self.middle.append(self.mid)
#                    self.middle.append(',' + value)
#                    self.mid = ')'
#            elif self.mid == '':
#                self.close = len(self.middle)
#                self.open.append(self.close)
#                self.middle.append(s)
#                self.middle.append('0')
#                self.middle.append(',' + value)
#                self.mid = ')'
#                self.state = 1

#    def storage2(self,value):
#        if self.mid == '':
#            self.replace = len(self.middle)
#            self.open.append(self.replace)
#            self.middle.append(value)
#            self.middle.append('0,')
#            self.state = 2
#        if self.mid != '' and self.state == 0:
#            if self.s == 1:
#                if self.mid == '+' or self.mid == '-':
#                    self.replace = 0
#                    self.middle.insert(0,value)
#                    self.append(',')
#                    self.state = 2
#                    self.mov_open(0)
#                    self.open.insert(0,0)
#                    self.mid = ''
#                else:
#                    i = self.recent_calculate(0)
#                    self.mov_open(i)
#                    self.insert_open(i)
#                    self.replace = i
#                    self.middle.insert(i,value)
#                    self.insert_open(i)
#                    self.middle.append(',')
#                    self.state = 2
#                    self.mid = ''
#            elif self.mid == '(':
#                self.open.append(len(self.middle))
#                self.middle.append(self.mid)
#                self.replace = len(self.middle)
#                self.middle.append(value)
#                self.middle.append('0')
#                self.middle.append(',')
#                self.mid = ''
#                self.state = 2
#            elif self.mid == ')':
#                self.mov_open(self.close)
#                self.insert_open(self.close)
#                self.replace = self.close
#                self.middle.insert(self.close,value)
#                self.middle.append(self.mid)
#                self.open.pop()
#                self.middle.append(',')
#                self.mid = ''
#                self.close = self.close + 1
#                self.state = 2
#            else:
#                self.replace = len(self.middle)
#                self.open.append(self.replace)
#                self.middle.append(value)
#                self.middle.append(self.mid)
#                self.middle.append(',')
#                self.mid = ''
#                self.state = 2
#                self.p = 0
#                print(self.middle)
#        if self.mid != '' and self.state == 1:
#            if self.mid == ')':
#                self.replace = self.close
#                self.mov_open(self.replace)
#                self.insert_open(self.replace)
#                self.middle.insert(self.close,value)
#                self.middle.append(self.mid)
#                self.open.pop()
#                self.middle.append(',')
#                self.close = -1
#                self.mid = ''
#                self.state = 2
#            else:
#                self.replace = len(self.middle)
#                self.open.append(self.replace)
#                self.middle.append(value)
#                self.middle.append(self.mid)
#                self.middle.append(',')
#                self.mid = ''
#                self.state = 2
#                self.p = 0
#        if self.state == 2:
#            self.middle[self.replace] = value

#    def calculation(self):
#        self.display0_show()
#        if len(self.store) == 0:
#            self.displayclear()
#            return
#        if self.s == 0:
#            if len(self.mid) > 0 and self.mid != '-':
#                self.store = self.store + self.mid
#                if self.mid == ')':
#                    self.open.pop()
#            else:
#                self.store = self.store[0:-1]
#        if len(self.open) > 0:
#            for i in range(len(self.open)):
#                self.store = self.store + ')'
#        screen_value=self.store
#        self.displayclear()
#        screen_value=str(screen_value)
#        try:
#            final_value=eval(screen_value)
#        except ZeroDivisionError:
#            self.display_error("Math Error : Division by Zero")
#        except ValueError:
#            self.display_error("Math Error :No negatives in sqrt/log ,cos-1 & sin-1 b/w -1 & 1 ")
#        except SyntaxError:
#            self.display_error("Improper equation entered")
#        except AttributeError:
#            self.display_error("Input Error : Please enter proper input")
#        else:
#            final_value=str(final_value)
#            self.mid = final_value
#            self.state = 1
#            self.display_screen(final_value)

#    def display_screen(self,value):
#        self.display.setText(value)

#    def display_error(self,value):
#        self.display.setText(value)

#    def display0_show(self):
#        self.store = ""
#        for i in self.middle:
#            self.store = self.store + i
#        return self.store

#    def show_screen(self):
#        self.store = ""
#        for i in self.middle:
#            if len(i) > 0 and i[-1] == '(':
#                if i[0] == 'n':
#                    self.store = self.store + i[3:]
#                elif i[0] == 'm':
#                    self.store = self.store + i[5:]
#            self.store = self.store + i
#        return self.store

#    def displayclear(self):
#        self.display.setText('0')
#        self.middle.clear()
#        self.mid = ""
#        self.p = 0
#        self.s = 0
#        self.left = 0
#        self.symbel.clear()
#        self.store = ""
#        self.close = -1
#        self.state = 0
#        self.open.clear()
#        self.replace = 0
#        self.calcul = 0

#    def invalid_input(self):
#        s = self.store
#        self.displayclear()
#        self.display_screen('无效输入')

#    def recent_calculate(self,k):
#        le = len(self.middle)
#        ri = 0
#        j = 0
#        for i in range(le - 1,-1,-1):
#            j = i
#            if self.middle[i] == '+' or self.middle[i] == '-':
#                break
#            if self.middle[i] == ')':
#                ri += 1
#                continue
#            if self.middle[i][-1] == '(':
#                if ri == 0:
#                    break
#                ri -= 1
#                continue
#        m = self.middle[j+1:]
#        if k == 0:
#            if j > 0:
#                return j + 1
#            return j
#        return section_calculate(m)

#    def section_calculate(self,value):
#        s = ''
#        for i in value:
#            s = s + i
#        return str(eval(s))

#    def mov_open(self,k):
#        for i in self.open:
#            if i >= k:
#                i += 1

#    def dmov_open(self,k):
#        for i in self.open:
#            if i >= k:
#                i -= 1

#    def insert_open(self,k):
#        j = 0
#        for i in self.open:
#            if i < k:
#                j = i
#            else:
#                self.open.insert(j,k)
#                return
#        if len(self.open) == 0:
#            self.open.append(k)

#    def clear_enter(self):
#        if self.s == 1 or self.mid == '(' or self.mid == ')':
#            return
#        self.mid = ""
#        if self.state == 1:
#            self.state = 0
#        if self.p == 1:
#            self.p = 0
#        self.display_screen(self.mid)

#    def clear_back(self):
#        if self.store == "" and self.display.text() != "":
#            self.displayclear()
#            return
#        if self.state == 1:
#            return
#        if len(self.mid) > 0:
#            if self.mid[-1] == '.':
#                self.p = 0
#            if self.s == 1:
#                self.s = 0
#            self.mid = self.mid[0:-1]
#        self.display_screen(self.mid)

#    def plott(self):
#        self.display0_show()
#        if len(self.store) == 0:
#            self.displayclear()
#            return
#        if self.s == 0:
#            if len(self.mid) > 0 and self.mid != '-':
#                self.store = self.store + self.mid
#                if self.mid == ')':
#                    self.open.pop()
#            else:
#                self.store = self.store[0:-1]
#        if len(self.open) > 0:
#            for i in range(len(self.open)):
#                self.store = self.store + ')'
#        print(self.store)
#        x = np.arange(1,2,0.1) #Just to check if equation enter for plotting is syntactically correct or not
#        try:
#            y = eval(self.store)
#        except SyntaxError:
#            print("Improper Equation entered")
#            self.display.setText("Improper Equation entered")
#        else:
#            print("kk")
#            GraphPageWindow.var = self.store
#            self.dialog = Graph(self)	#Calling the Graph class to display a Range requesting pop-up
#            self.dialog.setWindowTitle('Please Enter Range of y = f(x)')
#            self.dialog.show()
