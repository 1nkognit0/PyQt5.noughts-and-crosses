# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 235)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.error = QtWidgets.QLabel(Form)
        self.error.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.error.setFont(font)
        self.error.setText("")
        self.error.setObjectName("error")
        self.gridLayout.addWidget(self.error, 3, 0, 1, 2)
        self.confirm_new_name = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirm_new_name.setFont(font)
        self.confirm_new_name.setObjectName("confirm_new_name")
        self.gridLayout.addWidget(self.confirm_new_name, 1, 1, 1, 1)
        self.new_nickname = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_nickname.setFont(font)
        self.new_nickname.setObjectName("new_nickname")
        self.gridLayout.addWidget(self.new_nickname, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.accept_btn = QtWidgets.QPushButton(Form)
        self.accept_btn.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.accept_btn.setFont(font)
        self.accept_btn.setObjectName("accept_btn")
        self.gridLayout.addWidget(self.accept_btn, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Подтвердите имя:"))
        self.label.setText(_translate("Form", "Введите новое имя:"))
        self.accept_btn.setText(_translate("Form", "OK"))
