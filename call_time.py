# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from timess import Ui_Time
from PyQt5.Qt import *
from PyQt5.QtCore import pyqtSignal,Qt
import datetime
import calendar




class TimePageWindow(QWidget,Ui_Time):
 #定义点击信号
    chooseSignal = pyqtSignal(str)
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    select_time0y = current_year
    select_time0m = current_month
    select_time0d = current_day
    select_time1y = current_year
    select_time1m = current_month
    select_time1d = current_day
    starttimes = 0
    def __init__(self,parent=None):
        super(TimePageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.border.hide()
        self.select.hide()
        self.result.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:black;")
        self.border.setStyleSheet("background:transparent;border:none;")
        self.init_add()
        self.selectwindow.currentIndexChanged.connect(self.showDialog)
        self.selectmodel.currentIndexChanged.connect(self.show_model)
        self.year.currentIndexChanged.connect(self.result_add)
        self.month.currentIndexChanged.connect(self.result_add)
        self.day.currentIndexChanged.connect(self.result_add)
        self.starttime.clicked.connect(lambda:self.init_select(1))
        self.endtime.clicked.connect(lambda:self.init_select(2))
        self.border.clicked.connect(lambda:self.dispper_select())
        self.add.clicked.connect(lambda:self.result_add())
        self.sub.clicked.connect(lambda:self.result_add())
        self.select.clicked.connect(lambda:self.day_click())



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

    def show_model(self):
        ss = self.selectmodel.currentText()
        if ss == 'The val between dates':
            self.init_between()
        elif ss == 'Add or subtract the number of days':
            self.init_add()

    def init_add(self):
        self.endtime.hide()
        self.endlabel.hide()
        self.rday.hide()
        self.add.show()
        self.sub.show()
        self.year.show()
        self.month.show()
        self.day.show()
        self.yearlabel.show()
        self.monthlabel.show()
        self.daylabel.show()
        self.add.setChecked(True)
        self.sub.setChecked(False)
        self.selectmodel.setCurrentIndex(1)
        self.resultlabel.setText("date")
        self.starttime.setText(self.appear_day(self.select_time0y,self.select_time0m,self.select_time0d))
        self.result_add()

    def init_between(self):
        self.endtime.show()
        self.endlabel.show()
        self.rday.show()
        self.add.hide()
        self.sub.hide()
        self.year.hide()
        self.month.hide()
        self.day.hide()
        self.yearlabel.hide()
        self.monthlabel.hide()
        self.daylabel.hide()
        self.selectmodel.setCurrentIndex(0)
        self.resultlabel.setText("interval")
        self.rday.setText("")
        self.starttime.setText(self.appear_day(self.select_time0y,self.select_time0m,self.select_time0d))
        self.endtime.setText(self.appear_day(self.select_time1y,self.select_time1m,self.select_time1d))
        self.result_between()

    def dispper_select(self):
        self.border.hide()
        self.select.hide()
        if self.starttimes == 1:
            self.starttime.setFocus()
            self.starttime.setText(self.appear_day(self.select_time0y,self.select_time0m,self.select_time0d))
        elif self.starttimes == 2:
            self.endtime.setFocus()
            self.endtime.setText(self.appear_day(self.select_time1y,self.select_time1m,self.select_time1d))
        self.starttimes = 0

    def init_select(self,m):
        if m == 1:
            self.starttimes = 1
            self.init_month(self.select_time0y,self.select_time0m,self.select_time0d)
        if m == 2:
            self.starttimes = 2
            self.init_month(self.select_time1y,self.select_time1m,self.select_time1d)
        self.border.show()
        self.select.show()
    def init_month(self,y,m,d):
        self.select.setSelectedDate(QDate(y,m,d))

    def appear_week(self,y,m,w,d):
        s = ""
        if y != 0:
            s = str(y)
            s = s + '年'
            s = s + ','
        if m != 0:
            s = s + str(m)
            s = s + '月'
            s = s + ','
        if w != 0:
            s = s + str(w)
            s = s + '周'
            s = s + ','
        if d != 0:
            s = s + str(d)
            s = s + '天'
        if len(s) > 0 and s[-1] == ',':
            s = s[0:-1]
        return s

    def appear_day(self,y,m,d):
        s = str(y)
        s = s + '年'
        s = s + str(m)
        s = s + '月'
        s = s + str(d)
        s = s + '日'
        return s

    def day_click(self):
        if self.starttimes == 1:
            self.select_time0y = self.select.yearShown()
            self.select_time0m = self.select.monthShown()
            self.select_time0d = self.select.selectedDate().day()
        elif self.starttimes == 2:
            self.select_time1y = self.select.yearShown()
            self.select_time1m = self.select.monthShown()
            self.select_time1d = self.select.selectedDate().day()
        self.dispper_select()
        ss = self.selectmodel.currentText()
        if ss == 'The val between dates':
            self.result_between()
        elif ss == 'Add or subtract the number of days':
            self.result_add()

    def result_add(self):
        y = int(eval(self.year.currentText()))
        m = int(eval(self.month.currentText()))
        d = int(eval(self.day.currentText()))
        if self.add.isChecked() == True:
            m = m + self.select_time0m
            f = int(m % 12)
            if f == 0:
                f = 12
            i = int((m - 1) / 12)
            y = y + i
            year =self.select_time0y + y
            month = f
            d1 = datetime.datetime(year,month,self.select_time0d)
            delt = datetime.timedelta(days=d)
            delta = d1 + delt
            y = delta.year
            m = delta.month
            d = delta.day

        elif self.sub.isChecked() == True:
            f = int(m % 12)
            i = int((m - 1) / 12)
            if self.select_time0m - f <= 0:
                f = self.select_time0m - f + 12
                i += 1
            else:
                f = self.select_time0m - f
            y = y + i
            year =self.select_time0y - y
            month = f
            d1 = datetime.datetime(year,month,self.select_time0d)
            delt = datetime.timedelta(days=d)
            delta = d1 - delt
            y = delta.year
            m = delta.month
            d = delta.day
        self.result.setText(self.appear_day(y,m,d))

    def result_between(self):
        d1 = datetime.datetime(self.select_time0y,self.select_time0m,self.select_time0d)
        d2 = datetime.datetime(self.select_time1y,self.select_time1m,self.select_time1d)
        delt = d1 - d2
        delta = delt.days
        if delta > 0:
            y = self.select_time0y - self.select_time1y
            m = self.select_time0m - self.select_time1m
            d = self.select_time0d - self.select_time1d
            if m < 0:
                y -= 1
                m += 12
                if d < 0:
                    m -= 1
                    year = self.select_time1y + y
                    month = self.select_time1m + m
                    if month > 12:
                        year += 1
                    month = int(month % 12)
                    if month == 0:
                        month = 12
                    b1 = datetime.datetime(year,month,self.select_time1d)
                    d = (d1 - b1).days
            elif m == 0:
                if y > 0:
                    if d < 0:
                        y -= 1
                        m += 11
                        year = self.select_time1y + y
                        month = self.select_time1m + m
                        if month > 12:
                            year += 1
                        month = int(month % 12)
                        if month == 0:
                            month = 12
                        b1 = datetime.datetime(year,month,self.select_time1d)
                        d = (d1 - b1).days
                elif y == 0:
                    d = delta
            elif m > 0:
                if d < 0:
                    m -= 1
                    year = self.select_time1y + y
                    month = self.select_time1m + m
                    month = int(month % 12)
                    if month == 0:
                        month = 12
                    b1 = datetime.datetime(year,month,self.select_time1d)
                    d = (d1 - b1).days
            w = int(d / 7)
            d = d % 7
            self.result.setText(self.appear_week(y,m,w,d))
            if y == 0 and m == 0 and w == 0:
                self.rday.setText("")
            else:
                self.rday.setText(str(abs(delta)) + '天')
        elif delta < 0:
            y = self.select_time1y - self.select_time0y
            m = self.select_time1m - self.select_time0m
            d = self.select_time1d - self.select_time0d
            if m < 0:
                y -= 1
                m += 12
                if d < 0:
                    m -= 1
                    year = self.select_time0y + y
                    month = self.select_time0m + m
                    if month > 12:
                        year += 1
                    month = int(month % 12)
                    if month == 0:
                        month = 12
                    b1 = datetime.datetime(year,month,self.select_time0d)
                    d = (d2 - b1).days
            elif m == 0:
                if y > 0:
                    if d < 0:
                        y -= 1
                        m += 11
                        year = self.select_time0y + y
                        month = self.select_time0m + m
                        if month > 12:
                            year += 1
                        month = int(month % 12)
                        if month == 0:
                            month = 12
                        b1 = datetime.datetime(year,month,self.select_time0d)
                        d = (d2 - b1).days
                elif y == 0:
                    d = abs(delta)
            elif m > 0:
                if d < 0:
                    m -= 1
                    year = self.select_time0y + y
                    month = self.select_time0m + m
                    month = int(month % 12)
                    if month == 0:
                        month = 12
                    b1 = datetime.datetime(year,month,self.select_time0d)
                    d = (d2 - b1).days
            w = int(d / 7)
            d = d % 7
            self.result.setText(self.appear_week(y,m,w,d))
            if y == 0 and m == 0 and w == 0:
                self.rday.setText("")
            else:
                self.rday.setText(str(abs(delta)) + '天')
        elif delta == 0:
            self.result.setText("相同日期")
            self.rday.setText("")





