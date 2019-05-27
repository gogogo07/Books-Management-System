from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from userWindow import Ui_userWindow
from myRecord import Ui_myRecord
import resource
import classes
import connect
import time
import sys
import os



class myRecord(QtWidgets.QWidget, Ui_myRecord):
    ret = pyqtSignal()
    def __init__(self):
        super(myRecord, self).__init__()
        self.account = None
        self.setupUi(self)
        self.recordTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)    # 设置不可编辑
        self.user = classes.User()
        self.load()
        self.tableShow()
        bg = QtGui.QPalette()
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("myRecordWindow.jpg")))  # 设置背景图片
        self.setPalette(bg)

    def tableShow(self):
        """表格初始化"""
        if self.account !=None:
            num1 = self.user.lending
            num2 = self.user.history
            numTotal = len(num1) // 2 + len(num2) // 3
            self.recordTableWidget.setRowCount(numTotal)  # 设置表格行数
            row = 0
            list = 0
            for i in range(len(num1)):
                result = num1[i]
                newItem2(self, result, row, list)
                list += 1
                if i%2 == 1:
                    newItem2(self, '----', row, list)
                    row += 1
                    list = 0

            list = 0
            for i in range(len(num2)):
                result = num2[i]
                newItem2(self, result, row, list)
                list += 1
                if i%3 == 2:
                    row += 1
                    list = 0

    def load(self):
        """加载数据库信息"""
        if self.account != None:
            user = self.account
            con, cursor = connect.connection()
            sql = 'SELECT * FROM users WHERE user_account = "%s"' % (user)
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            con.close()
            if len(results)!=0:
                lending = eval(results[0][4])
                history = eval(results[0][5])
                self.user.setdata(results[0][1], results[0][2], results[0][3], lending, history)
            # self.user.show()
            self.setWindowTitle(str(self.account)+"的记录")
            self.setWindowIcon(QIcon('main.jpg'))                                       # 设置窗体标题图标


    def userReturn(self):
        """归还图书"""
        if self.account != None:
            con, cursor = connect.connection()                                          # 连接数据库
            curRow = self.recordTableWidget.currentRow()                                # 获取光标所点击的行数
            cellItem1 = self.recordTableWidget.item(curRow, 0)
            if cellItem1 != None: # 获取是否归还信息
                bookName = cellItem1.text()                                                 # 获取选中图书的信息
            else:
                QMessageBox.warning(self, "警告","请选择你要归还的图书！", QMessageBox.Yes)
                return
            """if curRow < 0 :
                QMessageBox.warning(self, "警告", "请选择你要归还的图书！", QMessageBox.Yes)"""
            cellItem2 = self.recordTableWidget.item(curRow, 2)                          # 获取是否归还信息
            str2 = cellItem2.text()
            if  str2 != "----":
                QMessageBox().information(self, "错误", "您已归还该图书", QMessageBox.Ok)
            else :
                reply = QMessageBox().warning(self, "归还图书", "您确定要归还"+bookName+"图书吗？",QMessageBox.Yes|QMessageBox.No)
                if reply == QMessageBox.Yes :
                    returnTime = time.strftime("%Y-%m-%d", time.localtime())            # 获取归还图书的时间
                    n = self.user.lending.index(bookName)
                    lentTime = self.user.lending[n+1]
                    self.user.lending.remove(bookName)                                  # 移除
                    self.user.lending.remove(lentTime)
                    self.user.history.append(bookName)                                  # 添加至history
                    self.user.history.append(lentTime)
                    self.user.history.append(returnTime)
                    lending = str(self.user.lending)
                    history = str(self.user.history)
                    try:                                                                # 还书--数据库信息更新
                        """Tode 用户名"""
                        cursor.execute("UPDATE users SET user_lendingnum = user_lendingnum-1 ,user_lending = %s,"
                                       " user_history = %s WHERE user_account = %s", (lending, history,self.account))
                        cursor.execute("UPDATE books SET book_left = book_left + 1 ,book_lending = book_lending - 1 WHERE book_name = %s",
                                       (bookName))
                        con.commit()

                    except Exception as e:
                        print(e)
                        con.rollback()
                    """finally:
                        cursor.close()
                        con.close()"""

                    """将记录保存到数据库中"""
                    try:
                        cursor.execute("INSERT INTO records(user_name, operator, book_name, time) VALUES(%s, %s, %s, %s)",
                                       (self.user.account, '归还了', bookName, returnTime))
                        con.commit()
                    except Exception as e:
                        con.rollback()
                        print (e)
                    finally:
                        con.close()
                        cursor.close()

                    QMessageBox().information (self, "成功", "成功归换"+bookName+"图书，欢迎您继续借阅图书", QMessageBox.Ok)
                    self.tableShow()
                    self.load()
                    self.ret.emit()

class userWindow(QtWidgets.QWidget, Ui_userWindow):
    def __init__(self):
        super(userWindow, self).__init__()
        self.account = None
        self.setupUi(self)
        self.userTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)          # 设置不可编辑
        self.child = myRecord()                                                         # 子窗口实例化
        self.user = classes.User()
        self.load()
        bg = QtGui.QPalette()
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("userWindow.jpg")))  # 设置背景图片
        self.setPalette(bg)


    def load(self):
        """加载数据库信息"""
        if self.account!=None:
            user = self.account
            con, cursor = connect.connection()
            sql = 'SELECT * FROM users WHERE user_account = "%s"' % (user)
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            con.close()
            lending = eval(results[0][4])
            history = eval(results[0][5])
            self.user.setdata(results[0][1], results[0][2], results[0][3], lending, history)
            # self.user.show()
            timee = int(time.strftime("%H", time.localtime()))
            if timee < 5 or timee > 18:
                hellostr = "晚上好！"
            elif timee >5 and timee <12:
                hellostr = "上午好！"
            else:
                hellostr = "下午好！"
            self.userLabel.setText("尊敬的 " + str(self.account) + " 用户，"+hellostr)
            self.setWindowIcon(QIcon('main.jpg'))                                       # 设置窗体标题图标

    def userMyRecord(self):
        """我的记录"""
        self.child.setWindowModality(Qt.ApplicationModal)                               # 堵塞父窗口
        self.child.account = self.account
        self.child.load()
        self.child.tableShow()
        self.child.ret.connect(self.load)
        self.child.ret.connect(self.userFind)
        self.child.show()


    def userFind(self):
        """查找"""
        if self.account != None:
            bookFind = self.bookNameEdit.text()                                         # 所查找的图书名称
            d = {}
            if bookFind != '':
                d['book_name'] = bookFind
                d['book_author'] = bookFind
            kind = self.kindofBooksBox.currentIndex()                                   # 所查找的图书种类
            bookKinds = [0, 'all', 1, '自传', 2, '医学', 3, '文学', 4, '计算机']
            for i in range(len(bookKinds)):
                if bookKinds[i] == kind:
                    d['book_kind'] = bookKinds[i+1]
            results = search(**d)
            if len(results) == 0:
                QMessageBox.warning(self, "警告", "抱歉，没有找到与‘"+bookFind+"’相关的书籍，建议适当减少筛选条件",
                                    QMessageBox.Ok)
            self.userTableWidget.setRowCount(len(results))
            row = 0
            list = 0
            for result in results:
                for l in range(1, 7):
                    newItem(self, result[l], row, list)
                    list += 1
                row += 1
                list = 0
            red(self, len(results))


    def userExit(self):
        """退出"""
        reply = QMessageBox.warning(self, "退出", "您确定要退出吗？", QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes :
            self.close()


    def userBorrow(self):
        """借阅图书"""
        if self.account != None:
            con, cursor = connect.connection()                                          # 连接数据库
            curRow = self.userTableWidget.currentRow()                                  # 获取光标所点击的行数
            if curRow < 0 :
                QMessageBox.warning(self, "警告", "请选择你要借阅的图书！", QMessageBox.Ok)
                return
            cellItem1 = self.userTableWidget.item(curRow, 0)                            # 获取图书名称
            bookName = cellItem1.text()
            if bookName in self.user.lending:
                QMessageBox.warning(self, "警告", "这本书你已经借了，而且还没有归还，不可重复再借同一本书。", QMessageBox.Yes)
            else:
                cellItem2 = self.userTableWidget.item(curRow, 4)                            # 获取图书剩余量
                str1 = cellItem2.text()
                bookNumber = int(str1)
                if bookNumber <= 0:
                    QMessageBox.warning(self, "警告", "‘"+bookName+"’已经没有剩余量了！", QMessageBox.Ok)
                else :
                    """Todo 借阅图书（记录+图书，剩余量-1）"""
                    lendTime = time.strftime("%Y-%m-%d", time.localtime())  # 获取借阅图书的时间

                    self.user.lending.append(bookName)
                    self.user.lending.append(lendTime)
                    lending = str(self.user.lending)
                    try: #借书-用户添加信息
                        cursor.execute("UPDATE users SET user_lendingnum = user_lendingnum+1, user_lending = %s WHERE user_account = %s",
                                       (lending, self.account))
                        cursor.execute("UPDATE books SET book_left = book_left - 1 ,book_lending = book_lending + 1 WHERE book_name = %s",
                            (bookName))
                        con.commit()
                    except Exception as e:
                        con.rollback()
                        print(e)

                    """保存借阅记录"""
                    try:
                        cursor.execute(
                            "INSERT INTO records(user_name, operator, book_name, time) VALUES(%s, %s, %s, %s)",
                            (self.user.account, '借阅了', bookName, lendTime))
                        con.commit()
                    except Exception as e:
                        con.rollback()
                        print(e)
                    finally:
                        con.close()
                        cursor.close()

                    QMessageBox.information(self, "恭喜您", "您已成功借阅‘"+bookName+"’图书", QMessageBox.Ok)
                    self.load()
                    self.userFind()

    def userBookRecommend(self):
        """推荐图书"""
        if self.account != None:
            self.userTableWidget.clearContents()                                        # 清空表格
            self.userTableWidget.setRowCount(10)                                        # 设置10行（即推荐10本书）
            QMessageBox.information(self, "推荐", "根据您的查找记录向您推荐以下10本书", QMessageBox.Ok)
            """Todo(根据用户的查找记录，按一定权重推荐10本书)"""


    def userHotBooks(self):
        """当前热门"""
        if self.account != None:
            self.userTableWidget.clearContents()                                        # 清空表格
            self.userTableWidget.setRowCount(10)                                        # 设置10行（即10本书）
            QMessageBox.information(self, "当前热门", "根据当前的热门向您推荐以下10本书", QMessageBox.Ok)
            """Todo(根据图书的借阅次数，显示10本书)"""

def search(book_name = None, book_author = None, book_kind = None):
    """在数据库里查找"""
    con, cursor = connect.connection()
    sql = ''
    if book_name is not None and book_kind !='all':
        sql = 'SELECT * FROM books WHERE (book_author REGEXP "%s" OR book_name REGEXP "%s")AND book_kind REGEXP "%s"'\
              % (book_name,book_name,book_kind)
    elif book_name is not None and book_kind == 'all':
        sql = 'SELECT * FROM books WHERE book_author REGEXP "%s" OR book_name REGEXP "%s"'\
              % (book_name,book_name)
    elif book_name is None and book_kind !='all':
        sql = 'SELECT * FROM books WHERE  book_kind REGEXP "%s"'% (book_kind)
    elif book_name is None and book_kind == 'all':
        sql = 'SELECT * FROM books '
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return results
    except:
        cursor.close()
        con.close()
        return None


def newItem(self, s, row, list):
    """创建单元格"""
    if list ==5 or list == 4:
        s = str(s)
    newItem = QTableWidgetItem(s)                                                       # 将图书信息添加至表格中
    newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)                         # 单元格文本居中
    self.userTableWidget.setItem(row, list, newItem)


def newItem2(self, s, row, list):
    """创建单元格"""
    newItem = QTableWidgetItem(s)                                                       # 将图书信息添加至表格中
    newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)                         # 单元格文本居中
    self.recordTableWidget.setItem(row, list, newItem)


def red(self,bookTotal):
    """将剩余量为0的标红"""
    for curRow in range(bookTotal):
        cellItem = self.userTableWidget.item(curRow, 4)
        str = cellItem.text()
        bookNumber = int(str)
        if bookNumber == 0:
            cellItem.setForeground(QBrush(QColor(255, 0, 0)))                           # 红色

