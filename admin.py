from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
        self.messageUpdata()
        self.chillBookManWin = adminBookManage()
        self.chillPutawayWin = adminPutaway()
        self.setWindowIcon(QIcon('main.jpg'))                       # 设置标题图片
        bg = QtGui.QPalette()  # 初始化界面
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("adminBookBg.jpg")))  # 设置背景图片
        self.setPalette(bg)
        self.setWindowTitle("图书管理")
        self.chillPutawayWin.putBook.connect(self.messageUpdata)
        self.chillBookManWin.signalDelete.connect(self.messageUpdata)

    def adminBookBack(self):
        self.hide()


    def adminBookManage(self):
        self.chillBookManWin.show()

    def adminBookPutaway(self):
        self.chillPutawayWin.show()

    def messageShow(self):
        records = getRecords()
        self.adminBookLab1.setText(records[0][1] + '于' + records[0][4] + records[0][2] + '一本《' + records[0][3] + '》。')
        self.adminBookLab2.setText(records[1][1] + '于' + records[1][4] + records[1][2] + '一本《' + records[1][3] + '》。')
        self.adminBookLab3.setText(records[2][1] + '于' + records[2][4] + records[2][2] + '一本《' + records[2][3] + '》。')
        self.adminBookLab4.setText(records[3][1] + '于' + records[3][4] + records[3][2] + '一本《' + records[3][3] + '》。')
        self.adminBookLab5.setText(records[4][1] + '于' + records[4][4] + records[4][2] + '一本《' + records[4][3] + '》。')
        self.adminBookLab1.setFont(QFont("Roman times", 12, QFont.Bold))
        self.adminBookLab2.setFont(QFont("Roman times", 12, QFont.Bold))
        self.adminBookLab3.setFont(QFont("Roman times", 12, QFont.Bold))
        self.adminBookLab4.setFont(QFont("Roman times", 12, QFont.Bold))
        self.adminBookLab5.setFont(QFont("Roman times", 12, QFont.Bold))


    def messageUpdata(self):
        self.adminBookSumLab.setText("当前图书馆的藏书为： " + str(getBookSum()))


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
    putBook = pyqtSignal()
    def __init__(self):
        super(adminPutaway,self).__init__()
        self.setupUi(self)
        self.adminPutawayNameEdit.setFocus()
        self.setWindowIcon(QIcon('main.jpg'))
        self.setWindowTitle("上架")
        bg = QtGui.QPalette()
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("putawayBg.jpg")))  # 设置背景图片
        self.setPalette(bg)


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
            res = get_books(tempno)
            if res == 0:
                try:
                    cursor.execute("INSERT INTO books(\
                                    book_name,book_author, book_kind, book_number, book_left, book_lending) \
                                    VALUES(%s, %s, %s, %s, %s, %s)", (tempname, tempauthor, tempkind, tempno, tempnum, 0))
                    con.commit()
                    reply = QMessageBox.question(self, '信息', '上架成功，是否继续？',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        self.adminPutawayNameEdit.clear()
                        self.adminPutawayKindEdit.clear()
                        self.adminPutawayNumEdit.clear()
                        self.adminPutawayNoEdit.clear()
                        self.adminPutawayAuthor.clear()
                        return
                    else:
                        self.adminPutawayBack()
                    self.putBook.emit()
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
                    QMessageBox.warning(self, "", "此书籍已经存在于书库，改数数目增加", QMessageBox.Ok)
                except Exception as e:
                    con.rollback()
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
    signalDelete = pyqtSignal()
    def __init__(self):
        super(adminBookManage,self).__init__()
        self.setupUi(self)
        self.results = None
        self.adminBookTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.adminBookTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.adminBookTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setWindowIcon(QIcon('main.jpg'))
        self.adminBookFindBtn.setStyleSheet("QPushButton{border-image: url(Find.jpg)}")
        self.setWindowTitle("图书管理")
        bg = QtGui.QPalette()
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("adminBookManageBg.jpg")))  # 设置背景图片
        self.setPalette(bg)
        self.adminBookTableWidget.horizontalHeader().sectionClicked.connect(self.HorSectionClicked)  # 表头单击信号
        self.lending = 0
        self.left = 0


    def HorSectionClicked(self, index):
        if index == 1 or index == 2 or index == 3:
            return
        elif index == 0:
            pass
        elif index == 4:
            if self.lending == 0:
                qsortIncrease(0, len(self.results) - 1, self.results, index)
                self.lending = 1
                self.left = 0
            else:
                qsortDecrease(0, len(self.results) - 1, self.results, index)
                self.lending = 0
                self.left = 0
            self.tableAdd()
        elif index == 5:
            if self.left == 0:
                qsortIncrease(0, len(self.results) - 1, self.results, index)
                self.left = 1
                self.lending = 0
            else:
                qsortDecrease(0, len(self.results) - 1, self.results, index)
                self.left = 0
                self.lending = 0
            self.tableAdd()


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
            self.signalDelete.emit()
            self.results = list(self.bookFine())
            self.tableAdd()
        else:
            return


    def adminBookFind(self):
        res = self.bookFine()
        if res == 0:
            QMessageBox.warning(self, "警告", "未找到符合书籍", QMessageBox.Ok)
            self.adminBookFindEdit.clear()
        else:
            self.results = list(res)
            self.tableAdd()


    def bookFine(self):
        bookkind = self.comboBox.currentText()
        bookdata = self.adminBookFindEdit.text()
        results = adminFindFunction(bookdata, bookkind)
        if len(results) == 0:
            return 0
        else:
            return results


    def tableAdd(self):
        self.adminBookTableWidget.setRowCount(len(self.results))
        for i in range(len(self.results)):
            self.adminBookTableWidget.setItem(i, 0, QTableWidgetItem(self.results[i][1]))  # 设置单元格内容
            self.adminBookTableWidget.setItem(i, 1, QTableWidgetItem(self.results[i][2]))
            self.adminBookTableWidget.setItem(i, 2, QTableWidgetItem(self.results[i][3]))
            self.adminBookTableWidget.setItem(i, 3, QTableWidgetItem(self.results[i][4]))
            self.adminBookTableWidget.setItem(i, 4, QTableWidgetItem(str(self.results[i][5])))
            self.adminBookTableWidget.setItem(i, 5, QTableWidgetItem(str(self.results[i][6])))





    def adminBookManageBack(self, results):
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
        bg = QtGui.QPalette()                                            # 初始化界面
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("adminWindowBg.jpg")))        # 设置背景图片
        self.setPalette(bg)
        self.setWindowIcon(QIcon('main.jpg'))
        self.setWindowTitle("管理界面")


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
        self.adminUserTable2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.adminUserLineEdit2.setFocus()
        self.setWindowIcon(QIcon('main.jpg'))
        self.adminUserFindBtn.setStyleSheet("QPushButton{border-image: url(Find.jpg)}")
        bg = QtGui.QPalette()  # 初始化界面
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("adminUserBg.jpg")))  # 设置背景图片
        self.setPalette(bg)
        self.setWindowTitle("用户管理")



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
        sql = 'SELECT * FROM BOOKS'
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
    except Exception as e:
        con.rollback()
        print (e)
    finally:
        cursor.close()
        con.close()


def red(self, bookTotal):
    """将剩余量为0的标红"""
    for curRow in range(bookTotal):
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
    sql = 'SELECT * FROM books WHERE book_number = "%s"' % (number)
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


def qsortIncrease(l, r, res, index):
    if l >= r:
        return
    left, right = l, r
    base = res[l]
    while l < r:
        while l < r and res[r][index + 1] >= base[index + 1]:
            r -= 1
        if l < r:
            res[l] = res[r]
        while l < r and res[l][index+ 1] <= base[index+ 1]:
            l += 1
        if l < r:
            res[r] = res[l]
    res[l] = base
    qsortIncrease(left, l - 1, res, index)
    qsortIncrease(l + 1, right, res, index)


def qsortDecrease(l, r, res, index):
    if l >= r:
        return
    left, right = l, r
    base = res[l]
    while l < r:
        while l < r and res[r][index + 1] <= base[index + 1]:
            r -= 1
        if l < r:
            res[l] = res[r]
        while l < r and res[l][index+ 1] >= base[index+ 1]:
            l += 1
        if l < r:
            res[r] = res[l]
    res[l] = base
    qsortDecrease(left, l - 1, res, index)
    qsortDecrease(l + 1, right, res, index)


if __name__ ==  '__main__':
    app=QtWidgets.QApplication(sys.argv)
    adminWindowT = adminWindow()
    adminWindowT.show()
    adminBookT=adminBook()

    sys.exit(app.exec())
