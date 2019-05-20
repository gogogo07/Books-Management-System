# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminWindow(object):
    def setupUi(self, adminWindow):
        adminWindow.setObjectName("adminWindow")
        adminWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(adminWindow)
        self.centralWidget.setMouseTracking(False)
        self.centralWidget.setObjectName("centralWidget")
        self.adminUserManageBtn = QtWidgets.QPushButton(self.centralWidget)
        self.adminUserManageBtn.setGeometry(QtCore.QRect(40, 110, 81, 61))
        self.adminUserManageBtn.setObjectName("adminUserManageBtn")
        self.admin = QtWidgets.QPushButton(self.centralWidget)
        self.admin.setGeometry(QtCore.QRect(160, 110, 81, 61))
        self.admin.setObjectName("admin")
        self.adminQuitBtn = QtWidgets.QPushButton(self.centralWidget)
        self.adminQuitBtn.setGeometry(QtCore.QRect(270, 110, 81, 61))
        self.adminQuitBtn.setObjectName("adminQuitBtn")
        adminWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(adminWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menuBar.setObjectName("menuBar")
        adminWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(adminWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        adminWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(adminWindow)
        self.statusBar.setObjectName("statusBar")
        adminWindow.setStatusBar(self.statusBar)

        self.retranslateUi(adminWindow)
        self.adminUserManageBtn.clicked.connect(adminWindow.adminUserManage)
        self.admin.clicked.connect(adminWindow.adminBookManage)
        self.adminQuitBtn.clicked.connect(adminWindow.adminQuit)
        QtCore.QMetaObject.connectSlotsByName(adminWindow)

    def retranslateUi(self, adminWindow):
        _translate = QtCore.QCoreApplication.translate
        adminWindow.setWindowTitle(_translate("adminWindow", "MainWindow"))
        self.adminUserManageBtn.setText(_translate("adminWindow", "用户管理"))
        self.admin.setText(_translate("adminWindow", "图书管理"))
        self.adminQuitBtn.setText(_translate("adminWindow", "退出"))


