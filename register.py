# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerWidget(object):
    def setupUi(self, registerWidget):
        registerWidget.setObjectName("registerWidget")
        registerWidget.resize(400, 300)
        self.label = QtWidgets.QLabel(registerWidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(registerWidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(registerWidget)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(registerWidget)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 81, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(registerWidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 50, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(registerWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 90, 131, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(registerWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 130, 131, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(registerWidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 170, 131, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(registerWidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 252, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.codeLabel = QtWidgets.QLabel(registerWidget)
        self.codeLabel.setGeometry(QtCore.QRect(50, 170, 100, 25))
        self.codeLabel.setText("")
        self.codeLabel.setObjectName("codeLabel")

        self.retranslateUi(registerWidget)
        self.pushButton.clicked.connect(registerWidget.registerDue)
        QtCore.QMetaObject.connectSlotsByName(registerWidget)

    def retranslateUi(self, registerWidget):
        _translate = QtCore.QCoreApplication.translate
        registerWidget.setWindowTitle(_translate("registerWidget", "Form"))
        self.label.setText(_translate("registerWidget", "请输入账号"))
        self.label_2.setText(_translate("registerWidget", "请输入密码"))
        self.label_3.setText(_translate("registerWidget", "请再次输入密码"))
        self.label_4.setText(_translate("registerWidget", "请输入验证码"))
        self.pushButton.setText(_translate("registerWidget", "注册"))

