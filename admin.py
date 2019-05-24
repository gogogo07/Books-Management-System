from PyQt5.QtWidgets import *
from adminUserManage import Ui_adminUserManageWidget
from adminWindow import Ui_adminWindow
from adminPutaway import Ui_adminPutaway
from adminBook import Ui_adminBook
from adminBookManage import Ui_adminBookManage
from PyQt5 import QtWidgets,QtCore,QtGui
import connect
import time
import sys
import os


class adminBook(QtWidgets.QMainWindow, Ui_adminBook):
    def __init__(self):
        super(adminBook,self).__init__()
        self.setupUi(self)
        self.messageShow()
        self.chillBookManWin = adminBookManage()
        self.chillPutawayWin = adminPutaway()

    def adminBookBack(self):
        self.hide()


    def adminBookManage(self):
        self.chillBookManWin.show()

    def adminBookPutaway(self):
        self.chillPutawayWin.show()

    def messageShow(self):
        self.adminBookSumLab.setText("当前图书馆的藏书为： " + str(getBookSum()))
        records = getRecords()
        self.adminBookLab1.setText(records[0][1] + '于' + records[0][4] + records[0][2] + '一本《' + records[0][3] + '》。')
        self.adminBookLab2.setText(records[1][1] + '于' + records[1][4] + records[1][2] + '一本《' + records[1][3] + '》。')
        self.adminBookLab3.setText(records[2][1] + '于' + records[2][4] + records[2][2] + '一本《' + records[2][3] + '》。')
        self.adminBookLab4.setText(records[3][1] + '于' + records[3][4] + records[3][2] + '一本《' + records[3][3] + '》。')
        self.adminBookLab5.setText(records[4][1] + '于' + records[4][4] + records[4][2] + '一本《' + records[4][3] + '》。')


def getBookSum():
    con, cursor = connect.connection()
    sql = "SELECT COUNT(1) FROM books"
    cursor.execute(sql)
    sum = cursor.fetchone()
    cursor.close()
    con.close()
    return sum[0]


def getRecords():
    con, cursor = connect.connection()
    sql = "SELECT * FROM records ORDER BY id DESC"
    cursor.execute(sql)
    results = list()
    for _ in range(5):
        res = cursor.fetchone()
        res = list(res)
        results.append(res)
    cursor.close()
    con.close()
    return results


class adminPutaway(QtWidgets.QMainWindow,Ui_adminPutaway):

    def __init__(self):
        super(adminPutaway,self).__init__()
        self.setupUi(self)
        self.adminPutawayNameEdit.setFocus()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.adminPutawayDue()

    def adminPutawayDue(self):
        tempname=self.adminPutawayNameEdit.text()
        tempkind=self.adminPutawayKindEdit.text()
        tempauthor=self.adminPutawayAuthor.text()
        tempnum=self.adminPutawayNumEdit.text()
        tempno=self.adminPutawayNoEdit.text()
        if tempname == '':
            QMessageBox.warning(self,"警告","书籍名不能为空",QMessageBox.Ok)
            return
        elif tempkind == '':
            QMessageBox.warning(self, "警告""种类不能为空", QMessageBox.Ok)
            return
        elif tempauthor == '':
            QMessageBox.warning(self, "警告","作者不能为空", QMessageBox.Ok)
            return
        elif tempnum == '':
            QMessageBox.warning(self, "警告","数量不能为空", QMessageBox.Ok)
            return
        elif tempno == '':
            QMessageBox.warning(self,"警告","序列号不能为空",QMessageBox.Ok)

        else:
            con, cursor = connect.connection()
            res = get_books(tempnum)
            if res == 0:
                try:
                    cursor.execute("INSERT INTO books(\
                                    book_name,book_author, book_kind, book_number, book_left, book_lending) \
                                    VALUES(%s, %s, %s, %s, %s, %s)", (tempname, tempauthor, tempkind, tempno, tempnum, 0))
                    con.commit()
                    QMessageBox.Warning(self, "", "书籍上架成功", QMessageBox.Ok)
                except Exception as e:
                    con.rollback()
                    print (e)
                finally:
                    cursor.close()
                    con.close()

            else:
                sql = "UPDATE books SET book_left = book_left + 1 WHERE book_number = '%s'" % (tempnum)
                try:
                    cursor.execute(sql)
                    con.commit()
                    print("更新成功")
                    QMessageBox.warning(self, "", "书籍上架成功", QMessageBox.Ok)
                except Exception as e:
                    con.rollback()
                    print(e)
                finally:
                    cursor.close()
                    con.close()


    def adminPutawayBack(self):
        self.hide()
        self.adminPutawayNameEdit.clear()
        self.adminPutawayKindEdit.clear()
        self.adminPutawayNumEdit.clear()
        self.adminPutawayNoEdit.clear()
        self.adminPutawayAuthor.clear()



class adminBookManage(QtWidgets.QMainWindow,Ui_adminBookManage):
    def __init__(self):
        super(adminBookManage,self).__init__()
        self.setupUi(self)
        self.adminBookTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.adminBookTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.adminBookFind()

    def adminBookSold(self):
        cloum = self.adminBookTableWidget.currentRow()
        if cloum == -1:
            return
        tempname = self.adminBookTableWidget.item(cloum,0).text()
        tempno = self.adminBookTableWidget.item(cloum,3).text()
        reply = QMessageBox.question(self, '信息', '是否确认下架该书？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            deleteBooks(tempname)
        else:
            return


    def adminBookFind(self):
        bookkind = self.comboBox.currentText()
        bookdata = self.adminBookFindEdit.text()
        print(bookkind)
        print(bookdata)
        results=adminFindFunction(bookdata, bookkind)
        if len(results) == 0:
            # QMessageBox.Warning(self, "", "未找到符合的书籍", QMessageBox.Ok)                 # 结果为0查找失败返回
            QMessageBox.warning(self, "警告", "未找到符合书籍", QMessageBox.Ok)
            self.adminBookFindEdit.clear()
            return
        else:
            self.adminBookTableWidget.setRowCount(len(results))
            for i in range(len(results)):
                self.adminBookTableWidget.setItem(i, 0, QTableWidgetItem(results[i][1]))        #设置单元格内容
                self.adminBookTableWidget.setItem(i, 1, QTableWidgetItem(results[i][2]))
                self.adminBookTableWidget.setItem(i, 2, QTableWidgetItem(results[i][3]))
                self.adminBookTableWidget.setItem(i, 3, QTableWidgetItem(results[i][4]))
                self.adminBookTableWidget.setItem(i, 4, QTableWidgetItem(results[i][5]))
                self.adminBookTableWidget.setItem(i, 5, QTableWidgetItem(results[i][6]))
                self.adminBookTableWidget.setItem(i, 6, QTableWidgetItem(results[i][6]))                                #


    def adminBookManageBack(self):
        self.adminBookFindEdit.clear()
        self.adminBookTableWidget.clearContents()                                                                       # 清空信息，并将格式初始化
        self.adminBookTableWidget.setRowCount(0)
        self.close()



class adminWindow(QtWidgets.QMainWindow,Ui_adminWindow):
    def __init__(self):
        super(adminWindow,self).__init__()
        self.setupUi(self)
        self.childWinBook = adminBook()
        self.childWinUser = adminUserManage()
        self.app = QtWidgets.QApplication(sys.argv)
        # 初始化界面
        """需要初始加载数据"""

    def adminUserManage(self):
        self.childWinUser.show()  # 显示子页面


        """显示用户管理界面"""

    def adminBookManage(self):
        self.childWinBook.show()

    def adminQuit(self):
        reply = QMessageBox.question(self, '信息', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)          # 退出时确定弹窗
        if reply==QMessageBox.No:
           return
        else:
            sys.exit(self.app.exec())



class adminUserManage(QtWidgets.QMainWindow,Ui_adminUserManageWidget):
    def __init__(self):
        super(adminUserManage,self).__init__()
        self.setupUi(self)                # 初始化界面
        self.adminUserTable2.setEditTriggers(QAbstractItemView.NoEditTriggers)       # 设置tablewidget为只读
        self.adminUserTable2.setSelectionBehavior(QAbstractItemView.SelectRows)          # 设置tablewidge为单行选中
        self.adminUserLineEdit2.setFocus()



    def adminUserBack(self):
        self.adminUserTable2.clearContents()
        self.adminUserLineEdit2.clear()
        self.adminUserTable2.setRowCount(8)
        self.adminUserLab.setText("用户名")
        self.close()              # 隐藏子窗口


    def adminReturn(self):
        """
        获取选中所在行数，若状态为未还将其第3列数据改为已换，
        并将现在日期赋给第四列。
        """
        state=''
        if state=='N':
            state='Y'

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.adminUserFind()

    def adminUserFind(self):
        tempusername=self.adminUserLineEdit2.text()             # 获取用户xing
        results = adminUserFindFunction(tempusername)
        print (results)
        if len(results) != 0:
            lending = eval(results[0][4])
            history = eval(results[0][5])
            self.adminUserTable2.setRowCount((len(lending) / 2) + (len(history) / 3))
            for i in range(0,len(lending)//2):
                self.adminUserTable2.setItem(i, 0, QTableWidgetItem(lending[i*2]))
                self.adminUserTable2.setItem(i, 1, QTableWidgetItem(lending[(i*2)+1]))
                self.adminUserTable2.setItem(i, 2, QTableWidgetItem("----"))
            j = 0
            for i in range(len(lending)//2, len(history)//3 + len(lending) // 2):
                self.adminUserTable2.setItem(i, 0, QTableWidgetItem(history[j * 3]))
                self.adminUserTable2.setItem(i, 1, QTableWidgetItem(history[(j * 3) + 1]))
                self.adminUserTable2.setItem(i, 2, QTableWidgetItem(history[(j * 3) + 2]))
                j += 1
            self.adminUserLab.setText(results[0][1])
        else:
            QMessageBox.warning(self,"警告", '抱歉，没有找到与%s有关的书。'%(tempusername), QMessageBox.Ok)


def adminFindFunction(bookData=None, bookKind=None):
    con, cursor = connect.connection()
    sql = ''
    if bookKind == '书名':
        sql = 'SELECT * FROM books WHERE book_name REGEXP "%s"' % (bookData)  # 在数据库里查找相应信息
    elif bookKind == '作者':
        sql = 'SELECT * FROM books WHERE book_author REGEXP "%s"' % (bookData)
    elif bookKind == '序列号':
        sql = 'SELECT * FROM books WHERE book_no REGEXP "%s"' % (bookData)
    elif bookKind == '全部':
        pass
    elif bookKind == '种类':
        sql = 'SELECT * FROM books WHERE book_kind REGEXP "%s"' % (bookData)
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


def adminUserFindFunction(userData):
    # 用户查询
    con,cursor = connect.connection()
    sql = 'SELECT * FROM users WHERE user_account = "%s"' % (userData)
    getdata(sql)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return results
    except:
        print('获取失败')
        cursor.close()
        con.close()
        p = tuple()
        return p


def getdata(sql):
    con, cursor = connect.connection()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        con.close()
        print (results)
        return results
    except:
        print ('获取失败')
        cursor.close()
        con.close()
        return None


def getuser_inf(user):
    sql = 'SELECT * FROM users WHERE user_account = "%s"' % (user)
    return getdata(sql)


def deleteBooks(bookName):
    con, cursor = connect.connection()
    sql = "DELETE FROM books WHERE book_name = '%s'" % (bookName)
    try:
        cursor.execute(sql)
        con.commit()
        print ("删除成功")
    except Exception as e:
        con.rollback()
        print (e)
    finally:
        cursor.close()
        con.close()


def red(self, bookTotal):
    """将剩余量为0的标红"""
    print("red")
    for curRow in range(bookTotal):
        print(curRow)
        cellItem = self.userTableWidget.item(curRow, 4)
        str = cellItem.text()
        bookNumber = int(str)
        if bookNumber == 0:
            cellItem.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))  # 红色

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
        print ('获取失败')
        cursor.close()
        con.close()
        return None


def get_books(number):
    con, cursor = connect.connection()
    sql = 'SELECT * FROM books WHERE book_number REGEXP "%s"' % (number)
    res = cursor.execute(sql)
    cursor.close()
    con.close()
    return res


def newItem(self, s, row, list):
    """创建单元格"""
    if list ==5 or list == 4:
        s = str(s)
    newItem = QTableWidgetItem(s)                                                   # 将图书信息添加至表格中
    newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)                     # 单元格文本居中
    self.userTableWidget.setItem(row, list, newItem)



if __name__ ==  '__main__':
    app=QtWidgets.QApplication(sys.argv)
    adminWindowT = adminWindow()
    adminWindowT.show()
    adminBookT=adminBook()
    sys.exit(app.exec())
