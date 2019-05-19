from login import Ui_loginWidgrt
from register import Ui_registerWidget
from userWindow import Ui_userWindow
from myRecord import Ui_myRecord
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import sys
import connect
import userMain


class Login(QtWidgets.QMainWindow, Ui_loginWidgrt):
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)


    def login(self):
        tempAccount=self.lineEdit.text()
        tempPassword=self.lineEdit_2.text()
        res = get_user(tempAccount)
        if tempPassword == res[0][2]:
            userWindow.account = tempAccount
            userWindow.load()
            userWindow.show()
            self.close()
        else:
            QMessageBox.warning(self, "错误", "密码错误，请重新输入", QMessageBox.Ok)
            self.lineEdit_2.clear()






    def register123(self):
        self.hide()
        res.show()


class Register(QtWidgets.QMainWindow, Ui_registerWidget):
    def __init__(self):
        super(Register,self).__init__()
        self.setupUi(self)
        self.lineEdit.setPlaceholderText("账号由8-12位数字与字母组成")
        self.lineEdit_2.setPlaceholderText("密码由8-12位字母与数字组成")
        self.lineEdit_3.setPlaceholderText("请重新输入密码")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

    def registerDue(self):
        tempAccout = self.lineEdit.text()
        tempPassword = self.lineEdit_2.text()
        tempPassword2 = self.lineEdit_3.text()

        if len(get_user(tempAccout)) != 0:
            QMessageBox.warning(self, "错误", "账号已注册", QMessageBox.Ok)
            self.lineEdit.clear()
        elif len(tempAccout) > 12:
            QMessageBox.warning(self, "错误", "账号长度太长", QMessageBox.Ok)
            self.lineEdit.clear()
        elif len(tempAccout) < 8:
            QMessageBox.warning(self, "错误", "账号长度太短", QMessageBox.Ok)
            self.lineEdit.clear()
        elif len(tempPassword) >12:
            QMessageBox.warning(self, "错误", "密码长度太长", QMessageBox.Ok)
            self.lineEdit_2.clear()
        elif len(tempPassword) < 8:
            QMessageBox.warning(self, "错误", "账号长度太短", QMessageBox.Ok)
            self.lineEdit_2.clear()
        elif tempPassword != tempPassword2:
            QMessageBox.warning(self, "错误", "两次输入的密码不匹配", QMessageBox.Ok)
        else:
            print("注册成功")
            QMessageBox.warning(self, "恭喜", "注册成功", QMessageBox.Ok)
            add_account(tempAccout, tempPassword)
            self.hide()
            log.show()



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
        print (e)
    finally:
        cursor.close()
        con.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    log = Login()
    res = Register()
    userWindow = userMain.userWindow()
    myRecord = userMain.myRecord()
    log.show()

    exit(app.exec())
