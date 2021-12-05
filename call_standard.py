# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from standard import Ui_standard
from PyQt5.QtCore import pyqtSignal,Qt
import math

class StandardPageWindow(QWidget,Ui_standard):
 #定义点击信号
    chooseSignal = pyqtSignal(str)
    def __init__(self,parent=None):
        super(StandardPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.m.setStyleSheet("QPushButton{color:rgb(200,200,200);}")
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
        self.add.clicked.connect(lambda:self.storage(' + '))
        self.sub.clicked.connect(lambda:self.storage(' - '))
        self.ant.clicked.connect(lambda:self.storage('-'))
        self.mul.clicked.connect(lambda:self.storage(' * '))
        self.divide.clicked.connect(lambda:self.storage(' / '))
        self.sqrt.clicked.connect(lambda:self.storage('^'))
        self.extract.clicked.connect(lambda:self.storage('s'))
        self.back.clicked.connect(lambda:self.storage('b'))
        self.c.clicked.connect(lambda:self.displayclear())
        self.ce.clicked.connect(lambda:self.clear_enter())
        self.dele.clicked.connect(lambda:self.clear_back())
        self.rest.clicked.connect(lambda:self.storage('%'))
        self.equ.clicked.connect(self.calculation)
        self.display.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:black;")
        self.display0.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:black;font-size:19px;font-weight:bold;font-family:Roman times;")
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display0.setReadOnly(True)
        self.display0.setAlignment(QtCore.Qt.AlignRight)
        self.selectwindow.currentIndexChanged.connect(self.showDialog)
        self.mc.clicked.connect(lambda:self.m_clear())
        self.mr.clicked.connect(lambda:self.m_read())
        self.m1.clicked.connect(lambda:self.m_add())
        self.m2.clicked.connect(lambda:self.m_sub())
        self.ms.clicked.connect(lambda:self.m_save())

    def showDialog(self):#实现页面切换
        ss = self.selectwindow.currentText()
        if ss == 'time':   #发射点击信号
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
    middle = []
    mid = ""
    prev_disp = ""
    stack = []
    stack_disp = []
    temp = []
    flag = 0
    p = 0  #point
    c = 0  #calculate
    s = 0  #symbel
    n = 0  #middle last is number
    memory = 0

    def displayclear(self):
        self.display0.clear()
        self.display.setText('0')
        self.flag = 0
        self.stack=[]
        self.stack_disp=[]
        self.store=""
        self.middle = []
        self.p = 0
        self.n = 0
        self.s = 0
        self.c = 0
        self.mid = ""
        memory = 0
    def clear_enter(self):
        self.mid = ""
        if self.s == 1:
            return
        if self.c == 1:
            self.c = 0
        if self.p == 1:
            self.p = 0
        self.display_screen(self.mid)
        self.display0_screen(self.store)
    def clear_back(self):
        if self.store == "" and self.display.text() != "":
            self.displayclear()
            return
        if self.c == 1:
            return
        if self.s == 1:
            return
        if len(self.mid) > 0:
            if self.mid[-1] == '.':
                self.p = 0
            self.mid = self.mid[0:-1]
        self.display_screen(self.mid)
        self.display0_screen(self.store + self.mid)
    def storage1(self,value):
        try:
            self.stack.pop()
        except IndexError:
            self.store = ""
        else:
            self.temp = self.stack
            self.store = ''.join(self.temp)
    def display0_show(self):
        self.store = ""
        for i in self.middle:
            self.store = self.store + i
        return self.store
    def storage(self,value):
        if value > '0' and value <= '9':
            if self.c == 1:
                self.n = 0
                self.c = 0
                self.mid = ""
            if self.s == 1:
                self.middle.append(self.mid)
                self.display0.setText(self.display0_show())
                self.mid = ""
                self.s = 0
            if len(self.mid) > 0 and eval(self.mid) == 0 and self.p == 0:
                self.mid = value
            else:
                self.mid = self.mid + value
            self.display0_screen(self.store + self.mid)
            self.display_screen(self.mid)
        if value == ' - ' or value == ' + ' or value == ' * ' or value == ' / ':
            self.p = 0
            if len(self.mid) > 0 and self.s == 0:
                if self.c == 1:
                    self.c = 0
                self.middle.append(self.mid)
                self.store = self.display0_show()
            if len(self.middle) > 0:
                if self.s == 0:
                    self.mid = value[1]
                    self.s = 1
                elif self.s == 1:
                    self.mid = value[1]
            self.display0_screen(self.store + self.mid)
        if value == '-':
            if self.s == 0 and eval(self.mid) != 0:
                a = 0 - eval(self.mid)
                self.mid = str(a)
            self.display_screen(self.mid)
            self.display0_screen(self.store + self.mid)
        if value == '.':
            if self.p == 0:
                if len(self.mid) == 0 or self.c == 1:
                    self.mid = "0"
                    self.c = 0
                self.mid = self.mid + value
                self.p = 1
            self.display_screen(self.mid)
            self.display0_screen(self.store + self.mid)
        if value == 'b' or value == 's' or  value == '^' or value == '%':
            if value == 'b':
                if len(self.mid) == 0 or self.s == 1:
                    return
                if eval(self.mid) != 0:
                    a = 1/eval(self.mid)
                    self.mid = str(a)
                    self.c = 1
                else:
                    self.displayclear()
                    self.display_error("分母不能为零")
                    return
            elif value == '^':
                if len(self.mid) == 0 or self.s == 1:
                    return
                a = pow(eval(self.mid),2)
                self.mid = str(a)
                self.c = 1
            elif value == 's':
                if len(self.mid) == 0 or self.s == 1:
                    return
                if eval(self.mid) >= 0:
                    a = math.sqrt(eval(self.mid))
                    self.mid = str(a)
                    self.c = 1
                else:
                    self.displayclear()
                    self.display_error("被开方数应大于等于零")
                    return
            elif value == '%':
                if len(self.mid) == 0 or self.s == 1 or eval(self.mid) == 0:
                    return
                a = eval(self.mid)/100
                self.mid = str(a)
                self.c = 1
            self.display0_screen(self.store + self.mid)
            self.display_screen(self.mid)
        if value == '0':
            if self.c == 1:
                self.n = 0
                self.c = 0
                self.mid = ""
            if self.s == 1:
                self.middle.append(self.mid)
                self.display0.setText(self.display0_show())
                self.mid = ""
                self.s = 0
            if len(self.mid) == 0:
                self.mid = self.mid + value
            elif len(self.mid) != 0 and eval(self.mid) > 0 and self.p == 0:
                self.mid = self.mid + value
            elif len(self.mid) != 0 and self.p == 1:
                self.mid = self.mid + value
            self.display_screen(self.mid)
            self.display0_screen(self.store + self.mid)
        self.stack.append(value)

    def display_screen(self,value):
        self.display.setText(value)
        self.stack_disp.append(value)

    def display0_screen(self,value):
        self.display0.setText(value)
        self.stack_disp.append(value)

    def display_error(self,value):
        self.display.setText(value)
        self.stack_disp.append(value)

    def disp_res(self,value):
        self.display.setText(value)
        self.stack_disp.append(value)

    def calculation(self):
        if len(self.store) == 0:
            self.displayclear()
            return
        if self.s == 0:
            if len(self.mid) > 0 and self.mid != '-':
                self.store = self.store + self.mid
            else:
                self.store = self.store[0:-1]
        screen_value=self.store
        self.displayclear()
        self.display0_screen(screen_value + "=")
        screen_value=str(screen_value)
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
            self.c = 1
            self.stack.append(final_value)
            self.disp_res(final_value)

    def m_clear(self):
        self.memory = 0
        self.m.setStyleSheet("QPushButton{color:rgb(200,200,200);}")

    def m_read(self):
        if self.s == 1:
            self.middle.append(self.mid)
        self.c = 1
        self.s = 0
        self.mid = str(self.memory)
        self.display.setText(self.mid)

    def m_add(self):
        try:
            eval(self.display.text())
        except:
            self.display.setText("content error")
        else:
            self.memory += eval(self.display.text())
            self.m.setStyleSheet("QPushButton{color:rgb(0,0,0);}")
            self.c = 1

    def m_sub(self):
        try:
            eval(self.display.text())
        except:
            self.display.setText("content error")
        else:
            self.memory += np.negative(eval(self.display.text()))
            self.m.setStyleSheet("QPushButton{color:rgb(0,0,0);}")
            self.c = 1

    def m_save(self):
        try:
            eval(self.display.text())
        except:
            self.display.setText("content error")
        else:
            self.memory = eval(self.display.text())
            self.m.setStyleSheet("QPushButton{color:rgb(0,0,0);}")
            self.c = 1

