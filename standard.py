# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_standard(object):
    def setupUi(self, standard):
        standard.setObjectName("standard")
        standard.resize(470, 630)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(standard.sizePolicy().hasHeightForWidth())
        standard.setSizePolicy(sizePolicy)
        standard.setMinimumSize(QtCore.QSize(470, 630))
        standard.setMaximumSize(QtCore.QSize(470, 630))
        self.selectwindow = QtWidgets.QComboBox(standard)
        self.selectwindow.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.selectwindow.setObjectName("selectwindow")
        self.selectwindow.addItem("")
        self.selectwindow.addItem("")
        self.selectwindow.addItem("")
        self.selectwindow.addItem("")
        self.model = QtWidgets.QLabel(standard)
        self.model.setGeometry(QtCore.QRect(140, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.model.setFont(font)
        self.model.setAlignment(QtCore.Qt.AlignCenter)
        self.model.setObjectName("model")
        self.display0 = QtWidgets.QLineEdit(standard)
        self.display0.setEnabled(False)
        self.display0.setGeometry(QtCore.QRect(10, 80, 451, 53))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display0.setFont(font)
        self.display0.setObjectName("display0")
        self.display = QtWidgets.QLineEdit(standard)
        self.display.setEnabled(False)
        self.display.setGeometry(QtCore.QRect(10, 130, 451, 50))
        self.display.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display.setFont(font)
        self.display.setObjectName("display")
        self.layoutWidget = QtWidgets.QWidget(standard)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 250, 451, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rest = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rest.sizePolicy().hasHeightForWidth())
        self.rest.setSizePolicy(sizePolicy)
        self.rest.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rest.setFont(font)
        self.rest.setObjectName("rest")
        self.horizontalLayout_2.addWidget(self.rest)
        self.ce = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ce.sizePolicy().hasHeightForWidth())
        self.ce.setSizePolicy(sizePolicy)
        self.ce.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ce.setFont(font)
        self.ce.setObjectName("ce")
        self.horizontalLayout_2.addWidget(self.ce)
        self.c = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c.sizePolicy().hasHeightForWidth())
        self.c.setSizePolicy(sizePolicy)
        self.c.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c.setFont(font)
        self.c.setObjectName("c")
        self.horizontalLayout_2.addWidget(self.c)
        self.dele = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dele.sizePolicy().hasHeightForWidth())
        self.dele.setSizePolicy(sizePolicy)
        self.dele.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dele.setFont(font)
        self.dele.setObjectName("dele")
        self.horizontalLayout_2.addWidget(self.dele)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.back = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.horizontalLayout_7.addWidget(self.back)
        self.sqrt = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqrt.sizePolicy().hasHeightForWidth())
        self.sqrt.setSizePolicy(sizePolicy)
        self.sqrt.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sqrt.setFont(font)
        self.sqrt.setObjectName("sqrt")
        self.horizontalLayout_7.addWidget(self.sqrt)
        self.extract = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extract.sizePolicy().hasHeightForWidth())
        self.extract.setSizePolicy(sizePolicy)
        self.extract.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.extract.setFont(font)
        self.extract.setObjectName("extract")
        self.horizontalLayout_7.addWidget(self.extract)
        self.divide = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divide.sizePolicy().hasHeightForWidth())
        self.divide.setSizePolicy(sizePolicy)
        self.divide.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.divide.setFont(font)
        self.divide.setObjectName("divide")
        self.horizontalLayout_7.addWidget(self.divide)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.d7 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d7.sizePolicy().hasHeightForWidth())
        self.d7.setSizePolicy(sizePolicy)
        self.d7.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d7.setFont(font)
        self.d7.setAutoDefault(False)
        self.d7.setObjectName("d7")
        self.horizontalLayout_8.addWidget(self.d7)
        self.d8 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d8.sizePolicy().hasHeightForWidth())
        self.d8.setSizePolicy(sizePolicy)
        self.d8.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d8.setFont(font)
        self.d8.setAutoDefault(False)
        self.d8.setObjectName("d8")
        self.horizontalLayout_8.addWidget(self.d8)
        self.d9 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d9.sizePolicy().hasHeightForWidth())
        self.d9.setSizePolicy(sizePolicy)
        self.d9.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d9.setFont(font)
        self.d9.setAutoDefault(False)
        self.d9.setObjectName("d9")
        self.horizontalLayout_8.addWidget(self.d9)
        self.mul = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mul.sizePolicy().hasHeightForWidth())
        self.mul.setSizePolicy(sizePolicy)
        self.mul.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mul.setFont(font)
        self.mul.setObjectName("mul")
        self.horizontalLayout_8.addWidget(self.mul)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.d4 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d4.sizePolicy().hasHeightForWidth())
        self.d4.setSizePolicy(sizePolicy)
        self.d4.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d4.setFont(font)
        self.d4.setAutoDefault(False)
        self.d4.setObjectName("d4")
        self.horizontalLayout_9.addWidget(self.d4)
        self.d5 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d5.sizePolicy().hasHeightForWidth())
        self.d5.setSizePolicy(sizePolicy)
        self.d5.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d5.setFont(font)
        self.d5.setAutoDefault(False)
        self.d5.setObjectName("d5")
        self.horizontalLayout_9.addWidget(self.d5)
        self.d6 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d6.sizePolicy().hasHeightForWidth())
        self.d6.setSizePolicy(sizePolicy)
        self.d6.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d6.setFont(font)
        self.d6.setAutoDefault(False)
        self.d6.setObjectName("d6")
        self.horizontalLayout_9.addWidget(self.d6)
        self.sub = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sub.sizePolicy().hasHeightForWidth())
        self.sub.setSizePolicy(sizePolicy)
        self.sub.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sub.setFont(font)
        self.sub.setObjectName("sub")
        self.horizontalLayout_9.addWidget(self.sub)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.d1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d1.sizePolicy().hasHeightForWidth())
        self.d1.setSizePolicy(sizePolicy)
        self.d1.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d1.setFont(font)
        self.d1.setAutoDefault(False)
        self.d1.setObjectName("d1")
        self.horizontalLayout_10.addWidget(self.d1)
        self.d2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d2.sizePolicy().hasHeightForWidth())
        self.d2.setSizePolicy(sizePolicy)
        self.d2.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d2.setFont(font)
        self.d2.setAutoDefault(False)
        self.d2.setObjectName("d2")
        self.horizontalLayout_10.addWidget(self.d2)
        self.d3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d3.sizePolicy().hasHeightForWidth())
        self.d3.setSizePolicy(sizePolicy)
        self.d3.setMaximumSize(QtCore.QSize(16777215, 65))
        self.d3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d3.setFont(font)
        self.d3.setAutoDefault(False)
        self.d3.setObjectName("d3")
        self.horizontalLayout_10.addWidget(self.d3)
        self.add = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.horizontalLayout_10.addWidget(self.add)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ant = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ant.sizePolicy().hasHeightForWidth())
        self.ant.setSizePolicy(sizePolicy)
        self.ant.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ant.setFont(font)
        self.ant.setAutoDefault(False)
        self.ant.setObjectName("ant")
        self.horizontalLayout_11.addWidget(self.ant)
        self.d0 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d0.sizePolicy().hasHeightForWidth())
        self.d0.setSizePolicy(sizePolicy)
        self.d0.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.d0.setFont(font)
        self.d0.setAutoDefault(False)
        self.d0.setObjectName("d0")
        self.horizontalLayout_11.addWidget(self.d0)
        self.point = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point.sizePolicy().hasHeightForWidth())
        self.point.setSizePolicy(sizePolicy)
        self.point.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.point.setFont(font)
        self.point.setAutoDefault(False)
        self.point.setObjectName("point")
        self.horizontalLayout_11.addWidget(self.point)
        self.equ = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equ.sizePolicy().hasHeightForWidth())
        self.equ.setSizePolicy(sizePolicy)
        self.equ.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.equ.setFont(font)
        self.equ.setObjectName("equ")
        self.horizontalLayout_11.addWidget(self.equ)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.layoutWidget_2 = QtWidgets.QWidget(standard)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 190, 451, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mc = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mc.sizePolicy().hasHeightForWidth())
        self.mc.setSizePolicy(sizePolicy)
        self.mc.setObjectName("mc")
        self.horizontalLayout.addWidget(self.mc)
        self.mr = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mr.sizePolicy().hasHeightForWidth())
        self.mr.setSizePolicy(sizePolicy)
        self.mr.setObjectName("mr")
        self.horizontalLayout.addWidget(self.mr)
        self.m1 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m1.sizePolicy().hasHeightForWidth())
        self.m1.setSizePolicy(sizePolicy)
        self.m1.setObjectName("m1")
        self.horizontalLayout.addWidget(self.m1)
        self.m2 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m2.sizePolicy().hasHeightForWidth())
        self.m2.setSizePolicy(sizePolicy)
        self.m2.setObjectName("m2")
        self.horizontalLayout.addWidget(self.m2)
        self.ms = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ms.sizePolicy().hasHeightForWidth())
        self.ms.setSizePolicy(sizePolicy)
        self.ms.setObjectName("ms")
        self.horizontalLayout.addWidget(self.ms)
        self.m = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m.sizePolicy().hasHeightForWidth())
        self.m.setSizePolicy(sizePolicy)
        self.m.setObjectName("m")
        self.horizontalLayout.addWidget(self.m)

        self.retranslateUi(standard)
        QtCore.QMetaObject.connectSlotsByName(standard)

    def retranslateUi(self, standard):
        _translate = QtCore.QCoreApplication.translate
        standard.setWindowTitle(_translate("standard", "Form"))
        self.selectwindow.setItemText(0, _translate("standard", "standard"))
        self.selectwindow.setItemText(1, _translate("standard", "scientific"))
        self.selectwindow.setItemText(2, _translate("standard", "graph"))
        self.selectwindow.setItemText(3, _translate("standard", "time"))
        self.model.setText(_translate("standard", "standard"))
        self.rest.setText(_translate("standard", "%"))
        self.ce.setText(_translate("standard", "CE"))
        self.c.setText(_translate("standard", "C"))
        self.dele.setText(_translate("standard", "<-"))
        self.back.setText(_translate("standard", "1/x"))
        self.sqrt.setText(_translate("standard", "x^2"))
        self.extract.setText(_translate("standard", "√x"))
        self.divide.setText(_translate("standard", "÷"))
        self.d7.setText(_translate("standard", "7"))
        self.d8.setText(_translate("standard", "8"))
        self.d9.setText(_translate("standard", "9"))
        self.mul.setText(_translate("standard", "×"))
        self.d4.setText(_translate("standard", "4"))
        self.d5.setText(_translate("standard", "5"))
        self.d6.setText(_translate("standard", "6"))
        self.sub.setText(_translate("standard", "-"))
        self.d1.setText(_translate("standard", "1"))
        self.d2.setText(_translate("standard", "2"))
        self.d3.setText(_translate("standard", "3"))
        self.add.setText(_translate("standard", "+"))
        self.ant.setText(_translate("standard", "±"))
        self.d0.setText(_translate("standard", "0"))
        self.point.setText(_translate("standard", "."))
        self.equ.setText(_translate("standard", "="))
        self.mc.setText(_translate("standard", "MC"))
        self.mr.setText(_translate("standard", "MR"))
        self.m1.setText(_translate("standard", "M+"))
        self.m2.setText(_translate("standard", "M-"))
        self.ms.setText(_translate("standard", "MS"))
        self.m.setText(_translate("standard", "M"))
