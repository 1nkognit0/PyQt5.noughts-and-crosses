# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(808, 487)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.confirm_password_label = QtWidgets.QLabel(Form)
        self.confirm_password_label.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.confirm_password_label.setFont(font)
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.gridLayout.addWidget(self.confirm_password_label, 8, 0, 1, 2)
        self.nickname_label = QtWidgets.QLabel(Form)
        self.nickname_label.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nickname_label.setFont(font)
        self.nickname_label.setObjectName("nickname_label")
        self.gridLayout.addWidget(self.nickname_label, 5, 0, 1, 2)
        self.error = QtWidgets.QLabel(Form)
        self.error.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setText("")
        self.error.setObjectName("error")
        self.gridLayout.addWidget(self.error, 9, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 3)
        self.confirm_password = QtWidgets.QLineEdit(Form)
        self.confirm_password.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirm_password.setFont(font)
        self.confirm_password.setText("")
        self.confirm_password.setObjectName("confirm_password")
        self.gridLayout.addWidget(self.confirm_password, 8, 2, 1, 1)
        self.password_label = QtWidgets.QLabel(Form)
        self.password_label.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 7, 0, 1, 2)
        self.previous_window = QtWidgets.QPushButton(Form)
        self.previous_window.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.previous_window.setFont(font)
        self.previous_window.setObjectName("previous_window")
        self.gridLayout.addWidget(self.previous_window, 11, 0, 1, 3)
        self.nickname = QtWidgets.QLineEdit(Form)
        self.nickname.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nickname.setFont(font)
        self.nickname.setObjectName("nickname")
        self.gridLayout.addWidget(self.nickname, 5, 2, 1, 1)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 7, 2, 1, 1)
        self.create_btn = QtWidgets.QPushButton(Form)
        self.create_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.create_btn.setFont(font)
        self.create_btn.setObjectName("create_btn")
        self.gridLayout.addWidget(self.create_btn, 10, 0, 1, 3)
        self.requirements = QtWidgets.QPushButton(Form)
        self.requirements.setMaximumSize(QtCore.QSize(25, 16777215))
        self.requirements.setObjectName("requirements")
        self.gridLayout.addWidget(self.requirements, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.confirm_password_label.setText(_translate("Form", "Подтвердите пароль: "))
        self.nickname_label.setText(_translate("Form", "Введите имя: "))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">Создание нового игрока</p></body></html>"))
        self.password_label.setText(_translate("Form", "Введите пароль: "))
        self.previous_window.setText(_translate("Form", "Вернуться на начальное окно"))
        self.create_btn.setText(_translate("Form", "Создать"))
        self.requirements.setText(_translate("Form", "См."))
        self.label.setText(_translate("Form", "См. требования к паролю и имени -->"))
