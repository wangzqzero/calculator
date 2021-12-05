# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from scientific import Ui_scientific
from PyQt5.QtCore import pyqtSignal,Qt
import math
import cmath
import numpy as np

class ScientificPageWindow(QWidget,Ui_scientific):
 #定义点击信号
    chooseSignal = pyqtSignal(str)
    def __init__(self,parent=None):
        super(ScientificPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.m.setStyleSheet("QPushButton{color:rgb(200,200,200);}")
        self.selectwindow.currentIndexChanged.connect(self.showDialog)
        self.display.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:black;")
        self.display0.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:black;font-size:19px;font-weight:bold;font-family:Roman times;")
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display0.setReadOnly(True)
        self.display0.setAlignment(QtCore.Qt.AlignRight)
        self.chan.clicked.connect(lambda:self.change())
        self.d0.clicked.connect(lambda:self.storage('0'))
        self.d1.clicked.connect(lambda:self.storage('1'))
        self.d2.clicked.connect(lambda:self.storage('2'))
        self.d3.clicked.connect(lambda:self.storage('3'))
        self.d4.clicked.connect(lambda:self.storage('4'))
        self.d5.clicked.connect(lambda:self.storage('5'))
        self.d6.clicked.connect(lambda:self.storage('6'))
        self.d7.clicked.connect(lambda:self.storage('7'))
        self.d8.clicked.connect(lambda:self.storage('8'))
        self.d9.clicked.connect(lambda:self.storage('9'))
        self.point.clicked.connect(lambda:self.storage('.'))
        self.sub.clicked.connect(lambda:self.storage('-'))
        self.add.clicked.connect(lambda:self.storage('+'))
        self.mul.clicked.connect(lambda:self.storage('*'))
        self.divi.clicked.connect(lambda:self.storage('/'))
        self.ant.clicked.connect(lambda:self.storage1('np.negative(','',0))
        self.up.clicked.connect(lambda:self.storage1('math.ceil(','',0))
        self.down.clicked.connect(lambda:self.storage1('math.floor(','',0))
        self.estate.clicked.connect(lambda:self.storage1('math.factorial(','',0))
        self.lef.clicked.connect(lambda:self.storage('('))
        self.rig.clicked.connect(lambda:self.storage(')'))
        self.abso.clicked.connect(lambda:self.storage1('np.abs(','',0))
        self.pi.clicked.connect(lambda:self.storage('np.pi'))
        self.e.clicked.connect(lambda:self.storage('np.e'))
        self.rand.clicked.connect(lambda:self.storage('rand'))
        self.equ.clicked.connect(lambda:self.calculation())
        self.back.clicked.connect(lambda:self.change_click(0))
        self.sin.clicked.connect(lambda:self.change_click(1))
        self.cos.clicked.connect(lambda:self.change_click(2))
        self.tan.clicked.connect(lambda:self.change_click(3))
        self.sqrt.clicked.connect(lambda:self.change_click(4))
        self.extract.clicked.connect(lambda:self.change_click(5))
        self.inde.clicked.connect(lambda:self.change_click(6))
        self.tind.clicked.connect(lambda:self.change_click(7))
        self.log.clicked.connect(lambda:self.change_click(8))
        self.ln.clicked.connect(lambda:self.change_click(9))
        self.c.clicked.connect(lambda:self.displayclear())
        self.ce.clicked.connect(lambda:self.clear_enter())
        self.dele.clicked.connect(lambda:self.clear_back())
        self.mc.clicked.connect(lambda:self.m_clear())
        self.mr.clicked.connect(lambda:self.m_read())
        self.m1.clicked.connect(lambda:self.m_add())
        self.m2.clicked.connect(lambda:self.m_sub())
        self.ms.clicked.connect(lambda:self.m_save())

    store= ""
    mid = ""
    middle = []
    symbel = []
    memory = 0
    open = []
    close = -1
    p = 0 #point
    left = 0 #left bracket
    state = 0 #the number state of last number
    s = 0  #flag last input is or not is symbel
    calcul = 0
    replace = 0


    def showDialog(self):#发射点击信号
        ss = self.selectwindow.currentText()
        if ss == 'time':
            self.chooseSignal.emit('time')
        elif ss == 'standard':
            self.chooseSignal.emit('standard')
        elif ss == 'graph':
            self.chooseSignal.emit('graph')
        elif ss == 'scientific':
            self.chooseSignal.emit('scientific')
        elif ss == 'programmer':
            self.chooseSignal.emit('programmer')

    def storage(self,value):
        if value > '0' and value <= '9':
            if self.state == 2:
                self.state = 0
            if self.mid == ')':
                self.middle = self.middle[0:self.close]
                self.close = self.open[-1]
                self.open.pop()
            if self.mid == '(':
                self.middle.append(self.mid)
                self.close = -1
            if self.state == 1:
                self.state = 0
                self.mid = ""
            if self.s == 1:
                self.middle.append(self.mid)
                self.display0.setText(self.show_screen())
                self.mid = ""
                self.s = 0
            if len(self.mid) > 0 and self.p == 0:
                if self.mid == '(' or self.mid == ')':
                    self.mid = value
                elif eval(self.mid) == 0:
                    self.mid = value
                else:
                    self.mid = self.mid + value
            else:
                self.mid = self.mid + value
            self.display0.setText(self.show_screen() + self.mid)
            self.display_screen(self.mid)
        elif value == '-' or value == '+' or value == '*' or value == '/':
            if self.state == 2:
                del self.middle[self.replace]
                self.open.remove(self.replace)
                self.dmov_open(self.replace)
                self.state = 0
                self.middle.pop()
                self.s = 1
                return
            elif self.mid == '(':
                self.middle.append(self.mid)
                self.middle.append('0')
                self.close = -1
            elif self.mid == ')':
                self.middle.append(self.mid)
                self.close = self.open[-1]
                self.open.pop()
                if self.state == 1:
                    self.state = 0
            elif len(self.mid) > 0 and self.s == 0:
                if self.state == 1:
                    self.state = 0
                self.middle.append(self.mid)
            if len(self.middle) > 0:
                self.store = self.display0_show()
                if self.s == 0:
                    self.mid = value
                    self.s = 1
                elif self.s == 1:
                    self.mid = value
            if value == '+' or value == '-':
                if len(self.open) > 0:
                    self.display.setText(self.section_calculate(self.middle[self.open[-1] + 1:]))
                else:
                    self.display.setText(self.section_calculate(self.middle))
            else:
                self.display.setText(self.recent_calculate(1))
            self.display0.setText(self.show_screen() + self.mid)
        elif value == '.':
            if self.mid == ')':
                self.middle = self.middle[0:self.close]
                self.close = self.open[-1]
                self.open.pop()
            elif self.mid == '(':
                self.middle.append(self.mid)
                self.close = -1
            if self.p == 0:
                if len(self.mid) == 0 or self.state == 1:
                    self.mid = "0"
                    self.state = 0
                self.mid = self.mid + value
                self.p = 1
            self.display_screen(self.mid)
            self.display0.setText(self.show_screen() + self.mid)
        elif value == '0':
            if self.state == 2:
                self.state = 0
            elif self.mid == ')':
                self.middle = self.middle[0:self.close]
                self.close = self.open[-1]
                self.open.pop()
                self.mid = ''
            elif self.mid == '(':
                self.middle.append(self.mid)
                self.close = -1
                self.mid = ''
            elif self.state == 1:
                self.state = 0
                self.mid = ""
            elif self.s == 1:
                self.middle.append(self.mid)
                self.display0.setText(self.show_screen())
                self.mid = ""
                self.s = 0
            if len(self.mid) == 0:
                self.mid = self.mid + value
            elif len(self.mid) != 0 and eval(self.mid) > 0 and self.p == 0:
                self.mid = self.mid + value
            elif len(self.mid) != 0 and self.p == 1:
                self.mid = self.mid + value
            self.display_screen(self.mid)
            self.display0.setText(self.show_screen() + self.mid)
        elif value == '(':
            self.display.setText('0')
            if self.state == 2:
                self.open.append(len(self.middle))
                self.middle.append(value)
                self.state = 0
                self.mid = '('
                self.display0.setText(self.show_screen() + self.mid)
                return
            if len(self.mid) > 0:
                if self.mid == ')':
                    self.middle = self.middle[0:self.close]
                    self.open.append(self.close)
                    self.mid = value
                    self.close = -1
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.mid == '(' or self.s == 1:
                    self.open.append(len(self.middle))
                    self.middle.append(self.mid)
                    self.display0.setText(self.show_screen())
                    self.close = -1
                    self.mid = value
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.state == 0 and self.s == 0:
                    self.open.append(len(self.middle))
                    self.mid = value
                    self.state = 1
                    self.close = -1
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.state == 1:
                    self.open.append(len(self.middle))
                    self.mid = value
                    self.close = -1
                    self.display0.setText(self.show_screen() + self.mid)
            else:
                if len(self.middle) == 0:
                    self.mid = value
                    self.open.append(0)
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.middle[-1] == '(' or self.middle[-1] == '+' or self.middle[-1] == '-' or self.middle[-1] == '*' or self.middle[-1] == '/':
                    self.close = -1
                    self.mid = value
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.middle[-1][-1] == ')':
                    self.middle = self.middle[0:self.close]
                    self.mid = value
                    self.close = -1
                    self.display0.setText(self.show_screen() + self.mid)
        elif value == ')':
            if len(self.open) > 1 or (len(self.open) == 1 and self.mid != ')'):
                self.state = 0
                if self.s == 1:
                    i = self.section_calculate(self.middle[self.open[-1] + 1:-1])
                    self.middle.append(self.mid)
                    self.middle.append(i)
                    self.mid = value
                    self.display0.setText(self.show_screen() + self.mid)
                    self.close = self.open[-1]
                elif self.mid == '(':
                    self.middle.append(self.mid)
                    self.middle.append('0')
                    self.mid = value
                    self.close = self.open[-1]
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.mid != '':
                    if self.mid == ')':
                        self.open.pop()
                    self.middle.append(self.mid)
                    self.mid = value
                    self.close = self.open[-1]
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.mid == '':
                    s = self.middle[-1]
                    if s == '(':
                        self.middle.append(0)
                        self.mid = value
                        self.close = self.open[-1]
                        self.display0.setText(self.show_screen() + self.mid)
                    elif s != '+' and s != '-' and s != '*' and s != '/':
                        self.middle.append(self.mid)
                        self.mid = value
                        self.close = self.open[-1]
                        self.display0.setText(self.show_screen() + self.mid)
                    else:
                        i = eval(self.middle[self.open[-1] + 1:-1])
                        self.middle.append(self.mid)
                        self.middle.append(str(i))
                        self.close = self.open[-1]
                        if self.mid == ')':
                            self.open.pop()
                        self.mid = value
                        self.display0.setText(self.show_screen() + self.mid)
                self.display.setText(self.section_calculate(self.middle[self.open[-1] + 1:]))
        elif value == 'np.e' or value == 'np.pi' or value == 'rand' or value == 'm':
            if value == 'rand':
                i = np.random.rand()
                value = str(i)
            if value == 'm':
                value = str(self.memory)
            if self.s == 1:
                self.middle.append(self.mid)
                self.mid = value
                self.state = 1
                self.s = 0
            elif self.mid == '':
                s1 = ''
                if len(self.middle) > 0:
                    s1 = self.middle[-1]
                if s1 == ')':
                    self.middle = self.middle[0:close]
                    self.close = -1
                    self.mid = value
                    self.state = 1
                elif s1 == '':
                    self.mid = value
                    self.state = 1
                elif s1 != '(' and s1 != '+' and s1 != '-' and s1 != '*' and s1 != '/':
                    self.mid = value
                    self.state = 1
                else:
                    self.mid = value
                    self.state = 1
            elif self.mid == '(':
                self.open.append(len(self.middle))
                self.close = -1
                self.middle.append(self.mid)
                self.display0.setText(self.show_screen())
                self.mid = value
                self.state = 1
            elif self.mid == ')':
                self.middle = self.middle[0:self.close]
                self.close = -1
                self.mid = value
                self.state = 1
            elif self.mid != '':
                self.mid = value
                self.state = 1
            if self.mid[0] != 'n':
                self.display0.setText(self.show_screen() + self.mid)
                self.display.setText(self.mid)
            else:
                self.display0.setText(self.show_screen() + self.mid[3:])
                self.display.setText(self.mid[3:])

    def change(self):
        s = self.sin.text()
        if s == 'sin':
            self.sin.setText('sin-1')
            self.cos.setText('cos-1')
            self.tan.setText('tan-1')
            self.extract.setText('3√x')
            self.inde.setText('y√x')
            self.sqrt.setText('X^3')
            self.log.setText('logyx')
            self.ln.setText('e^x')
            self.tind.setText('2^x')
        else:
            self.sin.setText('sin')
            self.cos.setText('cos')
            self.tan.setText('tan')
            self.extract.setText('√x')
            self.inde.setText('x^y')
            self.sqrt.setText('X^2')
            self.log.setText('log')
            self.ln.setText('ln')
            self.tind.setText('10^x')

    def change_click(self,value):
        s = self.sin.text()
        if s == 'sin':
            if value == 0:
                self.storage1('1/(','',0)
            if value == 1:
                self.storage1('math.sin(','',0)
            if value == 2:
                self.storage1('math.cos(','',0)
            if value == 3:
                self.storage1('math.tan(','',0)
            if value == 4:
                self.storage1('math.pow(','2',2)
            if value == 5:
                self.storage1('math.pow(','(1/2)',2)
            if value == 6:
                self.storage2('math.pow(')
            if value == 7:
                self.storage1('math.pow(10,','',0)
            if value == 8:
                self.storage1('math.log10(','',0)
            if value == 9:
                self.storage1('math.log(','',0)
        else:
            if value == 0:
                self.storage1('1/(','',0)
            if value == 1:
                self.storage1('np.arcsin(','',0)
            if value == 2:
                self.storage1('np.arccos(','',0)
            if value == 3:
                self.storage1('np.arctan(','',0)
            if value == 4:
                self.storage1('math.pow(','3',2)
            if value == 5:
                self.storage1('math.pow(','(1/3)',2)
            if value == 6:
                self.storage2('math.pow(')
            if value == 7:
                self.storage1('math.pow(2,','',0)
            if value == 8:
                self.storage2('math.log(')
            if value == 9:
                self.storage1('math.pow(np.e','',0)
            self.change()

    def storage1(self,s,value,k):
        if self.state == 2:
           j = self.middle[self.replace + 1,-1]
           self.mid = self.section_calculate(j)
           self.state = 0
        if k == 0:
            if self.mid != '' and self.state == 0:
                if s == 'math.log10(' or s == 'math.log(':
                    try:
                        eval(self.mid)
                    except:
                        self.mid = self.mid
                    else:
                        if eval(self.mid) < 0:
                            self.invalid_input()
                            return
                if self.s == 1:
                    if self.mid == '+' or self.mid == '-':
                        self.display0_show()
                        i = eval(self.store)
                        self.middle.append(self.mid)
                        self.close = len(self.middle)
                        self.open.append(self.close)
                        self.middle.append(s)
                        self.middle.append(str(i))
                        self.state = 1
                        self.s = 0
                        self.mid = ')'
                        self.display0.setText(self.show_screen() + self.mid)
                    else:
                        i = self.recent_calculate(1)
                        self.middle.append(self.mid)
                        self.close = len(self.middle)
                        self.open.append(self.close)
                        self.middle.append(s)
                        self.middle.append(i)
                        self.state = 1
                        self.s = 0
                        self.mid = ')'
                        self.display0.setText(self.show_screen() + self.mid)
                elif self.mid == '(':
                    self.open.append(len(self.middle))
                    self.middle.append(self.mid)
                    self.close = len(self.middle)
                    self.open.append(self.close)
                    self.middle.append(s)
                    self.middle.append('0')
                    self.mid = ')'
                    self.state = 1
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.mid == ')':
                    self.mov_open(self.close)
                    self.insert_open(self.close)
                    self.middle.insert(self.close,s)
                    self.middle.append(self.mid)
                    self.open.pop()
                    self.state = 1
                    self.display0.setText(self.show_screen() + self.mid)
                else:
                    self.close = len(self.middle)
                    self.open.append(self.close)
                    self.middle.append(s)
                    self.middle.append(self.mid)
                    self.mid = ')'
                    self.state = 1
                    self.p = 0
                    self.display0.setText(self.show_screen() + self.mid)
            elif self.mid != '' and self.state == 1:
                if self.mid == ')':
                    self.mov_open(self.close)
                    self.insert_open(self.close)
                    self.middle.insert(self.close,s)
                    self.middle.append(self.mid)
                    self.open.pop()
                    self.display0.setText(self.show_screen() + self.mid)
                else:
                    self.close = len(self.middle)
                    self.open.append(self.close)
                    self.middle.append(s)
                    self.middle.append(self.mid)
                    self.mid = ')'
                    self.p = 0
                    self.display0.setText(self.show_screen() + self.mid)
            elif self.mid == '':
                if s == 'math.log10(' or s == 'math.log(':
                    self.invalid_input()
                    return
                self.close = len(self.middle)
                self.open.append(self.close)
                self.middle.append(s)
                self.middle.append('0')
                self.mid = ')'
                self.state = 1
                self.display0.setText(self.show_screen() + self.mid)
        if k == 2:
            if self.mid != '' and self.state == 0:
                if self.s == 1:
                    if self.mid == '+' or self.mid == '-':
                        self.display0_show()
                        i = eval(self.store)
                        self.middle.append(self.mid)
                        self.close = len(self.middle)
                        self.open.append(self.close)
                        self.middle.append(s)
                        self.middle.append(str(i))
                        self.middle.append(',')
                        self.middle.append(value)
                        self.state = 1
                        self.s = 0
                        self.mid = ')'
                        self.display0.setText(self.show_screen() + self.mid)
                    else:
                        i = self.recent_calculate(1)
                        self.middle.append(self.mid)
                        self.close = len(self.middle)
                        self.open.append(self.close)
                        self.middle.append(s)
                        self.middle.append(i)
                        self.middle.append(',')
                        self.middle.append(value)
                        self.state = 1
                        self.s = 0
                        self.mid = ')'
                        self.display0.setText(self.show_screen() + self.mid)
                elif self.mid == '(':
                    self.open.append(len(self.middle))
                    self.middle.append(self.mid)
                    self.close = len(self.middle)
                    self.open.append(self.close)
                    self.middle.append(s)
                    self.middle.append('0,')
                    self.middle.append(value)
                    self.mid = ')'
                    self.state = 1
                    self.display0.setText(self.show_screen() + self.mid)
                elif self.mid == ')':
                    self.mov_open(self.close)
                    self.middle.insert(self.close,s)
                    self.insert_open(self.close)
                    self.middle.append(self.mid)
                    self.open.pop()
                    self.middle.append(',')
                    self.middle.append(value)
                    self.state = 1
                    self.display0.setText(self.show_screen() + self.mid)
                else:
                    self.close = len(self.middle)
                    self.open.append(self.close)
                    self.middle.append(s)
                    self.middle.append(self.mid)
                    self.middle.append(',' + value)
                    self.mid = ')'
                    self.state = 1
                    self.display0.setText(self.show_screen() + self.mid)
            elif self.mid != '' and self.state == 1:
                if self.mid == ')':
                    self.middle.insert(self.close,s)
                    self.mov_open(self.close)
                    self.insert_open(self.close)
                    self.middle.append(self.mid)
                    self.open.pop()
                    self.middle.append(',' + value)
                    self.display0.setText(self.show_screen() + self.mid)
                else:
                    self.close = len(self.middle)
                    self.open.append(self.close)
                    self.middle.append(s)
                    self.middle.append(self.mid)
                    self.middle.append(',' + value)
                    self.mid = ')'
                    self.display0.setText(self.show_screen() + self.mid)
            elif self.mid == '':
                self.close = len(self.middle)
                self.open.append(self.close)
                self.middle.append(s)
                self.middle.append('0')
                self.middle.append(',' + value)
                self.mid = ')'
                self.state = 1
                self.display0.setText(self.show_screen() + self.mid)
        self.display.setText(self.section_calculate(self.middle[self.close:]))

    def storage2(self,value):
        if self.mid == '':
            self.replace = len(self.middle)
            self.open.append(self.replace)
            self.middle.append(value)
            self.middle.append('0,')
            self.state = 2
            self.display0.setText(self.show_screen())
        if self.mid != '' and self.state == 0:
            if self.s == 1:
                if self.mid == '+' or self.mid == '-':
                    self.replace = 0
                    self.middle.insert(0,value)
                    self.append(',')
                    self.state = 2
                    self.mov_open(0)
                    self.open.insert(0,0)
                    self.mid = ''
                    self.display0.setText(self.show_screen())
                else:
                    i = self.recent_calculate(0)
                    self.mov_open(i)
                    self.insert_open(i)
                    self.replace = i
                    self.middle.insert(i,value)
                    self.insert_open(i)
                    self.middle.append(',')
                    self.state = 2
                    self.mid = ''
                    self.display0.setText(self.show_screen())
            elif self.mid == '(':
                self.open.append(len(self.middle))
                self.middle.append(self.mid)
                self.replace = len(self.middle)
                self.middle.append(value)
                self.middle.append('0')
                self.middle.append(',')
                self.mid = ''
                self.state = 2
                self.display0.setText(self.show_screen())
            elif self.mid == ')':
                self.mov_open(self.close)
                self.insert_open(self.close)
                self.replace = self.close
                self.middle.insert(self.close,value)
                self.middle.append(self.mid)
                self.open.pop()
                self.middle.append(',')
                self.mid = ''
                self.close = self.close + 1
                self.state = 2
                self.display0.setText(self.show_screen())
            else:
                self.replace = len(self.middle)
                self.open.append(self.replace)
                self.middle.append(value)
                self.middle.append(self.mid)
                self.middle.append(',')
                self.mid = ''
                self.state = 2
                self.p = 0
                print(self.middle)
                self.display0.setText(self.show_screen())
        if self.mid != '' and self.state == 1:
            if self.mid == ')':
                self.replace = self.close
                self.mov_open(self.replace)
                self.insert_open(self.replace)
                self.middle.insert(self.close,value)
                self.middle.append(self.mid)
                self.open.pop()
                self.middle.append(',')
                self.close = -1
                self.mid = ''
                self.state = 2
                self.display0.setText(self.show_screen())
            else:
                self.replace = len(self.middle)
                self.open.append(self.replace)
                self.middle.append(value)
                self.middle.append(self.mid)
                self.middle.append(',')
                self.mid = ''
                self.state = 2
                self.p = 0
                self.display0.setText(self.show_screen())
        if self.state == 2:
            self.middle[self.replace] = value
            self.display0.setText(self.show_screen())

    def calculation(self):
        ss = self.show_screen()
        self.display0_show()
        if len(self.store) == 0:
            self.displayclear()
            return
        if self.s == 0:
            if len(self.mid) > 0 and self.mid != '-':
                self.store = self.store + self.mid
                ss = ss + self.mid
                if self.mid == ')':
                    self.open.pop()
            else:
                self.store = self.store[0:-1]
                ss = ss[0:-1]
        if len(self.open) > 0:
            for i in range(len(self.open)):
                self.store = self.store + ')'
                ss = ss + ')'
        screen_value=self.store
        self.displayclear()
        self.display0_screen(ss + "=")
        screen_value=str(screen_value)
        print(screen_value)
        try:
            final_value=eval(screen_value)
        except ZeroDivisionError:
            self.display_error("Math Error : Division by Zero")
        except ValueError:
            self.display_error("Math Error :No negatives in sqrt/log ,cos-1 & sin-1 b/w -1 & 1 ")
        except SyntaxError:
            self.display_error("Improper equation entered")
        except AttributeError:
            self.display_error("Input Error : Please enter proper input")
        else:
            final_value=str(final_value)
            self.mid = final_value
            self.state = 1
            self.display_screen(final_value)

    def display_screen(self,value):
        self.display.setText(value)

    def display0_screen(self,value):
        self.display0.setText(value)

    def display_error(self,value):
        self.display.setText(value)

    def display0_show(self):
        self.store = ""
        for i in self.middle:
            self.store = self.store + i
        return self.store

    def show_screen(self):
        self.store = ""
        for i in self.middle:
            if (len(i) > 1 and i[-1] == '(') or i == 'np.e' or i == 'np.pi':
                if i[0] == 'n':
                    self.store = self.store + i[3:]
                elif i[0] == 'm':
                    self.store = self.store + i[5:]
            else:
                self.store = self.store + i
        return self.store

    def displayclear(self):
        self.display0.clear()
        self.display.setText('0')
        self.middle.clear()
        self.mid = ""
        self.p = 0
        self.s = 0
        self.left = 0
        self.symbel.clear()
        self.store = ""
        self.close = -1
        self.state = 0
        self.open.clear()
        self.replace = 0
        self.calcul = 0
        self.memory = 0

    def invalid_input(self):
        s = self.store
        self.displayclear()
        self.display_screen('无效输入')
        self.display0_screen(s)

    def recent_calculate(self,k):
        le = len(self.middle)
        ri = 0
        j = 0
        for i in range(le - 1,-1,-1):
            j = i
            if (self.middle[i] == '+' or self.middle[i] == '-') and ri == 0:
                break
            if self.middle[i] == ')':
                ri += 1
                continue
            if self.middle[i][-1] == '(':
                if ri == 0:
                    ri = -1
                    break
                ri -= 1
                continue
        if j > 0 or ri == -1:
            m = self.middle[j+1:]
        else:
            m = self.middle
        if k == 0:
            if j > 0:
                return j + 1
            return j
        print(m)
        print(self.middle)
        return self.section_calculate(m)

    def section_calculate(self,value):
        s = ''
        for i in value:
            s = s + i
        if self.mid == ')' and self.state == 1:
            s = s + ')'
        return str(eval(s))

    def mov_open(self,k):
        for i in self.open:
            if i >= k:
                i += 1

    def dmov_open(self,k):
        for i in self.open:
            if i >= k:
                i -= 1

    def insert_open(self,k):
        j = 0
        for i in self.open:
            if i < k:
                j = i
            else:
                self.open.insert(j,k)
                return
        if len(self.open) == 0:
            self.open.append(k)

    def clear_enter(self):
        if self.s == 1 or self.mid == '(' or self.mid == ')':
            return
        self.mid = ""
        if self.state == 1:
            self.state = 0
        if self.p == 1:
            self.p = 0
        self.display_screen(self.mid)
        self.display0_screen(self.store)
    def clear_back(self):
        if self.store == "" and self.display.text() != "":
            self.displayclear()
            return
        if self.state == 1:
            return
        if len(self.mid) > 0:
            if self.mid[-1] == '.':
                self.p = 0
            if self.s == 1:
                self.s = 0
            self.mid = self.mid[0:-1]
        self.display_screen(self.mid)
        self.display0_screen(self.store + self.mid)

    def m_clear(self):
        self.memory = 0
        self.m.setStyleSheet("QPushButton{color:rgb(200,200,200);}")

    def m_read(self):
        self.storage('m')

    def m_add(self):
        try:
            eval(self.display.text())
        except:
            self.display.setText("content error")
        else:
            self.memory += eval(self.display.text())
            self.m.setStyleSheet("QPushButton{color:rgb(0,0,0);}")
            self.state = 1

    def m_sub(self):
        try:
            eval(self.display.text())
        except:
            self.display.setText("content error")
        else:
            self.memory += np.negative(eval(self.display.text()))
            self.m.setStyleSheet("QPushButton{color:rgb(0,0,0);}")
            self.state = 1

    def m_save(self):
        try:
            eval(self.display.text())
        except:
            self.display.setText("content error")
        else:
            self.memory = eval(self.display.text())
            self.m.setStyleSheet("QPushButton{color:rgb(0,0,0);}")
            self.state = 1
