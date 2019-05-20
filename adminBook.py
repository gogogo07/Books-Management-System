# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminbookmanag.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminBook(object):
    def setupUi(self, adminBook):
        adminBook.setObjectName("adminBook")
        adminBook.resize(518, 394)
        self.adminBookPutawBtn = QtWidgets.QPushButton(adminBook)
        self.adminBookPutawBtn.setGeometry(QtCore.QRect(360, 190, 75, 51))
        self.adminBookPutawBtn.setObjectName("adminBookPutawBtn")
        self.adminBookManageBtn = QtWidgets.QPushButton(adminBook)
        self.adminBookManageBtn.setGeometry(QtCore.QRect(360, 82, 75, 51))
        self.adminBookManageBtn.setObjectName("adminBookManageBtn")
        self.pushButton_3 = QtWidgets.QPushButton(adminBook)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 292, 75, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.adminBookLab4 = QtWidgets.QLabel(adminBook)
        self.adminBookLab4.setGeometry(QtCore.QRect(60, 270, 241, 31))
        self.adminBookLab4.setObjectName("adminBookLab4")
        self.adminBookLab3 = QtWidgets.QLabel(adminBook)
        self.adminBookLab3.setGeometry(QtCore.QRect(60, 210, 241, 31))
        self.adminBookLab3.setObjectName("adminBookLab3")
        self.adminBookLab2 = QtWidgets.QLabel(adminBook)
        self.adminBookLab2.setGeometry(QtCore.QRect(60, 150, 241, 31))
        self.adminBookLab2.setObjectName("adminBookLab2")
        self.adminBookLab1 = QtWidgets.QLabel(adminBook)
        self.adminBookLab1.setGeometry(QtCore.QRect(60, 90, 241, 31))
        self.adminBookLab1.setObjectName("adminBookLab1")
        self.adminBookSumLab = QtWidgets.QLabel(adminBook)
        self.adminBookSumLab.setGeometry(QtCore.QRect(20, 20, 241, 31))
        self.adminBookSumLab.setObjectName("adminBookSumLab")
        self.adminBookLab5 = QtWidgets.QLabel(adminBook)
        self.adminBookLab5.setGeometry(QtCore.QRect(60, 330, 241, 31))
        self.adminBookLab5.setObjectName("adminBookLab5")

        self.retranslateUi(adminBook)
        self.adminBookManageBtn.clicked.connect(adminBook.adminBookManage)
        self.adminBookPutawBtn.clicked.connect(adminBook.adminBookPutaway)
        self.pushButton_3.clicked.connect(adminBook.adminBookBack)
        QtCore.QMetaObject.connectSlotsByName(adminBook)

    def retranslateUi(self, adminBook):
        _translate = QtCore.QCoreApplication.translate
        adminBook.setWindowTitle(_translate("adminBook", "Form"))
        self.adminBookPutawBtn.setText(_translate("adminBook", "图书上架"))
        self.adminBookManageBtn.setText(_translate("adminBook", "图书查询"))
        self.pushButton_3.setText(_translate("adminBook", "返回"))
        self.adminBookLab4.setText(_translate("adminBook", "信息"))
        self.adminBookLab3.setText(_translate("adminBook", "信息"))
        self.adminBookLab2.setText(_translate("adminBook", "信息"))
        self.adminBookLab1.setText(_translate("adminBook", "信息"))
        self.adminBookSumLab.setText(_translate("adminBook", "书籍总量"))
        self.adminBookLab5.setText(_translate("adminBook", "信息"))


