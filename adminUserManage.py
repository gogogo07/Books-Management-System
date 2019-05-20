# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_user_manage.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminUserManageWidget(object):
    def setupUi(self, adminUserManageWidget):
        adminUserManageWidget.setObjectName("adminUserManageWidget")
        adminUserManageWidget.resize(621, 448)
        self.adminUserBackBtn = QtWidgets.QPushButton(adminUserManageWidget)
        self.adminUserBackBtn.setGeometry(QtCore.QRect(500, 370, 101, 61))
        self.adminUserBackBtn.setObjectName("adminUserBackBtn")
        self.adminUserTable2 = QtWidgets.QTableWidget(adminUserManageWidget)
        self.adminUserTable2.setGeometry(QtCore.QRect(40, 160, 341, 271))
        self.adminUserTable2.setObjectName("adminUserTable2")
        self.adminUserTable2.setColumnCount(3)
        self.adminUserTable2.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setHorizontalHeaderItem(2, item)
        self.adminUserLineEdit2 = QtWidgets.QLineEdit(adminUserManageWidget)
        self.adminUserLineEdit2.setGeometry(QtCore.QRect(40, 50, 311, 41))
        self.adminUserLineEdit2.setText("")
        self.adminUserLineEdit2.setObjectName("adminUserLineEdit2")
        self.adminUserPutawayBtn = QtWidgets.QPushButton(adminUserManageWidget)
        self.adminUserPutawayBtn.setGeometry(QtCore.QRect(500, 160, 101, 61))
        self.adminUserPutawayBtn.setObjectName("adminUserPutawayBtn")
        self.adminUserFindBtn = QtWidgets.QPushButton(adminUserManageWidget)
        self.adminUserFindBtn.setGeometry(QtCore.QRect(370, 30, 75, 71))
        self.adminUserFindBtn.setObjectName("adminUserFindBtn")
        self.adminUserLab = QtWidgets.QLabel(adminUserManageWidget)
        self.adminUserLab.setGeometry(QtCore.QRect(210, 110, 171, 41))
        self.adminUserLab.setObjectName("adminUserLab")

        self.retranslateUi(adminUserManageWidget)
        self.adminUserPutawayBtn.clicked.connect(adminUserManageWidget.adminReturn)
        self.adminUserBackBtn.clicked.connect(adminUserManageWidget.adminUserBack)
        self.adminUserFindBtn.clicked.connect(adminUserManageWidget.adminUserFind)
        QtCore.QMetaObject.connectSlotsByName(adminUserManageWidget)

    def retranslateUi(self, adminUserManageWidget):
        _translate = QtCore.QCoreApplication.translate
        adminUserManageWidget.setWindowTitle(_translate("adminUserManageWidget", "Form"))
        self.adminUserBackBtn.setText(_translate("adminUserManageWidget", "返回"))
        item = self.adminUserTable2.verticalHeaderItem(0)
        item.setText(_translate("adminUserManageWidget", "记录1"))
        item = self.adminUserTable2.verticalHeaderItem(1)
        item.setText(_translate("adminUserManageWidget", "记录2"))
        item = self.adminUserTable2.verticalHeaderItem(2)
        item.setText(_translate("adminUserManageWidget", "记录3"))
        item = self.adminUserTable2.verticalHeaderItem(3)
        item.setText(_translate("adminUserManageWidget", "记录4"))
        item = self.adminUserTable2.verticalHeaderItem(4)
        item.setText(_translate("adminUserManageWidget", "记录5"))
        item = self.adminUserTable2.verticalHeaderItem(5)
        item.setText(_translate("adminUserManageWidget", "记录6"))
        item = self.adminUserTable2.verticalHeaderItem(6)
        item.setText(_translate("adminUserManageWidget", "记录7"))
        item = self.adminUserTable2.verticalHeaderItem(7)
        item.setText(_translate("adminUserManageWidget", "记录8"))
        item = self.adminUserTable2.horizontalHeaderItem(0)
        item.setText(_translate("adminUserManageWidget", "书籍"))
        item = self.adminUserTable2.horizontalHeaderItem(1)
        item.setText(_translate("adminUserManageWidget", "借出日期"))
        item = self.adminUserTable2.horizontalHeaderItem(2)
        item.setText(_translate("adminUserManageWidget", "归还日期"))
        self.adminUserPutawayBtn.setText(_translate("adminUserManageWidget", "还书"))
        self.adminUserFindBtn.setText(_translate("adminUserManageWidget", "查找"))
        self.adminUserLab.setText(_translate("adminUserManageWidget", "<html><head/><body><p><span style=\" font-size:14pt;\">用户名</span></p></body></html>"))


