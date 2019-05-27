# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myRecord.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_myRecord(object):
    def setupUi(self, myRecord):
        myRecord.setObjectName("myRecord")
        myRecord.resize(590, 381)
        myRecord.setStyleSheet("QWidget#customWidget {\n"
"        background: rgb(173, 202, 232);\n"
"}\n"
"\n"
"/**********子界面中央背景**********/\n"
"QWidget#centerWidget {\n"
"        background: rgb(232, 241, 252);\n"
"}\n"
"\n"
"/**********主界面样式**********/\n"
"QWidget#mainWindow {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(232, 241, 252);\n"
"}\n"
"\n"
"QWidget#messageWidget {\n"
"        background: rgba(173, 202, 232, 50%);\n"
"}\n"
"\n"
"QWidget#loadingWidget {\n"
"        border: none;\n"
"        border-radius: 5px;\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"QWidget#remoteWidget {\n"
"        border-top-right-radius: 10px;\n"
"        border-bottom-right-radius: 10px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-left: none;\n"
"        background: transparent;\n"
"}\n"
"\n"
"StyledWidget {\n"
"        qproperty-normalColor: rgb(65, 65, 65);\n"
"        qproperty-disableColor: rgb(180, 180, 180);\n"
"        qproperty-highlightColor: rgb(0, 160, 230);\n"
"        qproperty-errorColor: red;\n"
"}\n"
"\n"
"QProgressIndicator {\n"
"        qproperty-color: rgb(2, 65, 132);\n"
"}\n"
"\n"
"/**********提示**********/\n"
"QToolTip{\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"/**********状态栏**********/\n"
"QStatusBar {\n"
"        background: rgb(187, 212, 238);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-left: none;\n"
"        border-right: none;\n"
"        border-bottom: none;\n"
"}\n"
"QStatusBar::item {\n"
"    border: none;\n"
"    border-right: 1px solid rgb(111, 156, 207);\n"
"}\n"
"\n"
"\n"
"/**********表头**********/\n"
"QHeaderView{\n"
"        border: none;\n"
"        border-bottom: 3px solid rgb(0, 78, 161);\n"
"        background: transparent;\n"
"        min-height: 30px;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding-left: 5px;\n"
"}\n"
"QHeaderView::section:horizontal:hover {\n"
"        color: white;\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"QHeaderView::section:horizontal:pressed {\n"
"        color: white;\n"
"        background: rgb(6, 94, 187);\n"
"}\n"
"QHeaderView::up-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        image: url(:/White/topArrow);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
"        image: url(:/White/topArrowHover);\n"
"}\n"
"QHeaderView::down-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        image: url(:/White/bottomArrow);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
"        image: url(:/White/bottomArrowHover);\n"
"}\n"
"\n"
"/**********表格**********/\n"
"QTableView {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(224, 238, 255);\n"
"        gridline-color: rgb(111, 156, 207);\n"
"}\n"
"QTableView::item {\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        border: none;\n"
"        background: white;\n"
"        border-right: 1px solid rgb(111, 156, 207);\n"
"        border-bottom: 1px solid rgb(111, 156, 207);\n"
"}\n"
"QTableView::item:selected{\n"
"        background-color:rgb(160, 255, 182);\n"
"        \n"
"}\n"
"/*QTableView::item:selected:!active {\n"
"        color: rgb(65, 65, 65);*/\n"
"QTableView::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"\n"
"/**********滚动条-水平**********/\n"
"QScrollBar:horizontal {\n"
"        height: 20px;\n"
"        background: transparent;\n"
"        margin-top: 3px;\n"
"        margin-bottom: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"        height: 20px;\n"
"        min-width: 30px;\n"
"        background: rgb(170, 200, 230);\n"
"        margin-left: 15px;\n"
"        margin-right: 15px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"        background: rgb(165, 195, 225);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"        width: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/arrowLeft);\n"
"        subcontrol-position: left;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"        width: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/arrowRight);\n"
"        subcontrol-position: right;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/**********滚动条-垂直**********/\n"
"QScrollBar:vertical {\n"
"        width: 20px;\n"
"        background: transparent;\n"
"        margin-left: 3px;\n"
"        margin-right: 3px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"        width: 20px;\n"
"        min-height: 30px;\n"
"        background: rgb(170, 200, 230);\n"
"        margin-top: 15px;\n"
"        margin-bottom: 15px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"        background: rgb(165, 195, 225);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"        height: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/topArrow);\n"
"        subcontrol-position: top;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"        height: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/bottomArrow);\n"
"        subcontrol-position: bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"        background: transparent;\n"
"}\n"
"\n"
"QScrollBar#verticalScrollBar:vertical {\n"
"        margin-top: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"/**********文本编辑框**********/\n"
"QTextEdit {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        color: rgb(70, 71, 73);\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********滚动区域**********/\n"
"QScrollArea {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********滚动区域**********/\n"
"QWidget#transparentWidget {\n"
"        background: transparent;\n"
"}\n"
"\n"
"\n"
"/**********按钮**********/\n"
"QToolButton#nsccButton {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding: 10px;\n"
"        qproperty-icon: url(:/White/nscc);\n"
"        qproperty-iconSize: 32px 32px;\n"
"        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
"}\n"
"QToolButton#nsccButton:hover {\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"QToolButton#transferButton {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding: 10px;\n"
"        qproperty-icon: url(:/White/transfer);\n"
"        qproperty-iconSize: 32px 32px;\n"
"        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
"}\n"
"QToolButton#transferButton:hover {\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********按钮**********/\n"
"QPushButton{\n"
"        border-radius: 4px;\n"
"        border: none;\n"
"        width: 75px;\n"
"        height: 25px;\n"
"}\n"
"QPushButton:enabled {\n"
"        background: rgb(120, 170, 220);\n"
"        color: white;\n"
"}\n"
"QPushButton:!enabled {\n"
"        background: rgb(180, 180, 180);\n"
"        color: white;\n"
"}\n"
"QPushButton:enabled:hover{\n"
"        background: rgb(100, 160, 220);\n"
"}\n"
"QPushButton:enabled:pressed{\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"\n"
"QPushButton#blueButton {\n"
"        color: white;\n"
"}\n"
"QPushButton#blueButton:enabled {\n"
"        background: rgb(0, 78, 161);\n"
"        color: white;\n"
"}\n"
"QPushButton:!enabled {\n"
"        background: rgb(180, 180, 180);\n"
"        color: white;\n"
"}\n"
"QPushButton#blueButton:enabled:hover {\n"
"        background: rgb(2, 65, 132);\n"
"}\n"
"QPushButton#blueButton:enabled:pressed {\n"
"        background: rgb(6, 94, 187);\n"
"}\n"
"\n"
"QPushButton#selectButton {\n"
"        border: none;\n"
"        border-radius: none;\n"
"        border-left: 1px solid rgb(111, 156, 207);\n"
"        background: transparent;\n"
"        image: url(:/White/scan);\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QPushButton#selectButton:enabled:hover{\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"QPushButton#selectButton:enabled:pressed{\n"
"        background: rgb(120, 170, 220);\n"
"}\n"
"\n"
"QPushButton#linkButton {\n"
"        background: transparent;\n"
"        color: rgb(0, 160, 230);\n"
"        text-align:left;\n"
"}\n"
"QPushButton#linkButton:hover {\n"
"        color: rgb(20, 185, 255);\n"
"        text-decoration: underline;\n"
"}\n"
"QPushButton#linkButton:pressed {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QPushButton#transparentButton {\n"
"        background: transparent;\n"
"}\n"
"\n"
"")
        self.recordTableWidget = QtWidgets.QTableWidget(myRecord)
        self.recordTableWidget.setGeometry(QtCore.QRect(30, 70, 411, 271))
        self.recordTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.recordTableWidget.setObjectName("recordTableWidget")
        self.recordTableWidget.setColumnCount(3)
        self.recordTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.recordTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordTableWidget.setHorizontalHeaderItem(2, item)
        self.userReturnBtn = QtWidgets.QPushButton(myRecord)
        self.userReturnBtn.setGeometry(QtCore.QRect(470, 80, 93, 51))
        self.userReturnBtn.setObjectName("userReturnBtn")
        self.userRecordExitBtn = QtWidgets.QPushButton(myRecord)
        self.userRecordExitBtn.setGeometry(QtCore.QRect(470, 280, 93, 51))
        self.userRecordExitBtn.setObjectName("userRecordExitBtn")
        self.textEdit = QtWidgets.QTextEdit(myRecord)
        self.textEdit.setGeometry(QtCore.QRect(170, 30, 151, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(myRecord)
        self.userRecordExitBtn.clicked.connect(myRecord.close)
        self.userReturnBtn.clicked.connect(myRecord.userReturn)
        QtCore.QMetaObject.connectSlotsByName(myRecord)

    def retranslateUi(self, myRecord):
        _translate = QtCore.QCoreApplication.translate
        myRecord.setWindowTitle(_translate("myRecord", "我的记录"))
        item = self.recordTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("myRecord", "图书"))
        item = self.recordTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("myRecord", "借阅时间"))
        item = self.recordTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("myRecord", "归还时间"))
        self.userReturnBtn.setText(_translate("myRecord", "归还图书"))
        self.userRecordExitBtn.setText(_translate("myRecord", "退出"))
        self.textEdit.setHtml(_translate("myRecord", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">我的借阅记录</span></p></body></html>"))


