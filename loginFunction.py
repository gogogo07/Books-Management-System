from login import Ui_loginWidgrt
from register import Ui_registerWidget
from userWindow import Ui_userWindow
from myRecord import Ui_myRecord
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import sys
import connect
import userMain
from admin import *


class Login(QtWidgets.QMainWindow, Ui_loginWidgrt):
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)         # 设置密码黑点遮挡
        self.lineEdit.setFocus()                        # 设置焦点
        self.setWindowTitle("登陆")
        self.setWindowIcon(QIcon('main.jpg'))
        bg = QtGui.QPalette()
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("loginBg.jpg")))  # 设置背景图片
        self.setPalette(bg)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.login()


    def login(self):
        tempAccount=self.lineEdit.text()
        tempPassword=self.lineEdit_2.text()
        res = get_user(tempAccount)
        if tempAccount == 'admin' and tempPassword == 'admin123':
            adminWindowT.show()
            self.close()
        elif tempAccount == '':
            QMessageBox.warning(self, "错误", "请输入账号", QMessageBox.Yes)
            return
        elif tempPassword == '':
            QMessageBox.warning(self, "错误", "请输入密码", QMessageBox.Yes)
            return
        elif len(res) != 0:
            if tempPassword == res[0][2]:
                userWindow.account = tempAccount
                userWindow.load()
                userWindow.show()
                self.close()
            else:
                QMessageBox.warning(self, "错误", "密码错误，请重新输入", QMessageBox.Yes)
                self.lineEdit_2.clear()


    def register123(self):
        self.hide()
        res.show()


class Register(QtWidgets.QMainWindow, Ui_registerWidget):
    def __init__(self):
        super(Register,self).__init__()
        self.setupUi(self)
        self.lineEdit.setPlaceholderText("请输入账号")
        self.lineEdit_2.setPlaceholderText("密码由6-12位字母与数字组成")
        self.lineEdit_3.setPlaceholderText("请重新输入密码")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit.setFocus()
        self.setWindowTitle("注册")
        self.setWindowIcon(QIcon('main.jpg'))
        bg = QtGui.QPalette()
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("registerBg.jpg")))  # 设置背景图片
        self.setPalette(bg)

    def registerDue(self):
        tempAccout = self.lineEdit.text()
        tempPassword = self.lineEdit_2.text()
        tempPassword2 = self.lineEdit_3.text()

        if len(get_user(tempAccout)) != 0:
            QMessageBox.warning(self, "错误", "账号已注册", QMessageBox.Ok)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        elif len(tempAccout) > 12:
            QMessageBox.warning(self, "错误", "账号长度太长", QMessageBox.Ok)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        #elif len(tempAccout) < 6:
        #    QMessageBox.warning(self, "错误", "账号长度太短", QMessageBox.Ok)
        #    self.lineEdit.clear()
        #    self.lineEdit_2.clear()
        #   self.lineEdit_3.clear()
        elif len(tempPassword) >12:
            QMessageBox.warning(self, "错误", "密码长度太长", QMessageBox.Ok)
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        elif len(tempPassword) < 6:
            QMessageBox.warning(self, "错误", "账号长度太短", QMessageBox.Ok)
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        elif tempPassword != tempPassword2:
            QMessageBox.warning(self, "错误", "两次输入的密码不匹配", QMessageBox.Ok)
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        else:
            print("注册成功")
            QMessageBox.warning(self, "恭喜", "注册成功", QMessageBox.Ok)
            add_account(tempAccout, tempPassword)
            self.hide()
            log.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.registerDue()

    def registerBack(self):
        self.hide()
        log.show()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()



def get_user(name):
    con, cursor = connect.connection()
    sql = 'SELECT * FROM users WHERE user_account = "%s"' % (name)
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    con.close()
    return res


def add_account(*mes):
    con, cursor = connect.connection()
    try:
        cursor.execute("INSERT INTO users(\
                            user_account, user_password, user_lendingnum, user_lending, user_history) \
                            VALUES(%s, %s, %s, %s, %s)", (mes[0], mes[1], 0, '[]', '[]'))
        con.commit()
        print ('添加成功')
    except Exception as e:
        con.rollback()
    finally:
        cursor.close()
        con.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    log = Login()
    res = Register()
    userWindow = userMain.userWindow()
    adminWindowT = adminWindow()
    myRecord = userMain.myRecord()
    log.show()

    exit(app.exec())
