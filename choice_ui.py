# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 170)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_player_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_player_btn.setGeometry(QtCore.QRect(237, 50, 219, 50))
        self.create_player_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_player_btn.setFont(font)
        self.create_player_btn.setObjectName("create_player_btn")
        self.authorization_btn = QtWidgets.QPushButton(self.centralwidget)
        self.authorization_btn.setGeometry(QtCore.QRect(10, 50, 220, 50))
        self.authorization_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.authorization_btn.setFont(font)
        self.authorization_btn.setObjectName("authorization_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_player_btn.setText(_translate("MainWindow", "Новый игрок"))
        self.authorization_btn.setText(_translate("MainWindow", "Авторизироваться"))
