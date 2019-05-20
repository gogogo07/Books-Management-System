# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminputaway.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminPutaway(object):
    def setupUi(self, adminPutaway):
        adminPutaway.setObjectName("adminPutaway")
        adminPutaway.resize(550, 350)
        self.adminPutawayNameEdit = QtWidgets.QLineEdit(adminPutaway)
        self.adminPutawayNameEdit.setGeometry(QtCore.QRect(300, 60, 120, 25))
        self.adminPutawayNameEdit.setObjectName("adminPutawayNameEdit")
        self.adminPutawayKindEdit = QtWidgets.QLineEdit(adminPutaway)
        self.adminPutawayKindEdit.setGeometry(QtCore.QRect(300, 110, 120, 25))
        self.adminPutawayKindEdit.setObjectName("adminPutawayKindEdit")
        self.adminPutawayAuthor = QtWidgets.QLineEdit(adminPutaway)
        self.adminPutawayAuthor.setGeometry(QtCore.QRect(300, 160, 120, 25))
        self.adminPutawayAuthor.setObjectName("adminPutawayAuthor")
        self.adminPutawayNumEdit = QtWidgets.QLineEdit(adminPutaway)
        self.adminPutawayNumEdit.setGeometry(QtCore.QRect(300, 210, 120, 25))
        self.adminPutawayNumEdit.setObjectName("adminPutawayNumEdit")
        self.adminPutawayBackBtn = QtWidgets.QPushButton(adminPutaway)
        self.adminPutawayBackBtn.setGeometry(QtCore.QRect(440, 310, 75, 23))
        self.adminPutawayBackBtn.setObjectName("adminPutawayBackBtn")
        self.label = QtWidgets.QLabel(adminPutaway)
        self.label.setGeometry(QtCore.QRect(60, 120, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(adminPutaway)
        self.label_2.setGeometry(QtCore.QRect(60, 170, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(adminPutaway)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(adminPutaway)
        self.label_4.setGeometry(QtCore.QRect(50, 70, 61, 20))
        self.label_4.setObjectName("label_4")
        self.adminPutawayDueBtn = QtWidgets.QPushButton(adminPutaway)
        self.adminPutawayDueBtn.setGeometry(QtCore.QRect(40, 310, 75, 23))
        self.adminPutawayDueBtn.setObjectName("adminPutawayDueBtn")
        self.label_5 = QtWidgets.QLabel(adminPutaway)
        self.label_5.setGeometry(QtCore.QRect(160, 20, 221, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(adminPutaway)
        self.label_6.setGeometry(QtCore.QRect(60, 270, 54, 12))
        self.label_6.setObjectName("label_6")
        self.adminPutawayNoEdit = QtWidgets.QLineEdit(adminPutaway)
        self.adminPutawayNoEdit.setGeometry(QtCore.QRect(300, 260, 120, 25))
        self.adminPutawayNoEdit.setObjectName("adminPutawayNoEdit")

        self.retranslateUi(adminPutaway)
        self.adminPutawayDueBtn.clicked.connect(adminPutaway.adminPutawayDue)
        self.adminPutawayBackBtn.clicked.connect(adminPutaway.adminPutawayBack)
        QtCore.QMetaObject.connectSlotsByName(adminPutaway)

    def retranslateUi(self, adminPutaway):
        _translate = QtCore.QCoreApplication.translate
        adminPutaway.setWindowTitle(_translate("adminPutaway", "Form"))
        self.adminPutawayBackBtn.setText(_translate("adminPutaway", "返回"))
        self.label.setText(_translate("adminPutaway", "种类"))
        self.label_2.setText(_translate("adminPutaway", "作者"))
        self.label_3.setText(_translate("adminPutaway", "数量"))
        self.label_4.setText(_translate("adminPutaway", "书籍名称"))
        self.adminPutawayDueBtn.setText(_translate("adminPutaway", "确定"))
        self.label_5.setText(_translate("adminPutaway", "     请输入上架书籍的信息"))
        self.label_6.setText(_translate("adminPutaway", "序列号"))


