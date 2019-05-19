class Book(object):
    """书本的类"""
    def __init__(self, id, name, author, kind, number, left, lending):
        self.id = id
        self.name = name
        self.author = author
        self.kind = kind
        self.number = number
        self.left = left
        self.lending = lending


class User(object):
    """用户的类"""
    def __init__(self, account = None, password = None, lendingnum = None, lending = None, history = None):
        self.account = account
        self.password = password
        self.lendingnum = lendingnum
        self.lending = lending
        self.history = history

    def setdata(self, account, password, lendingnum, lending, history):
        self.account = account
        self.password = password
        self.lendingnum = lendingnum
        self.lending = lending
        self.history = history

    def show(self):
        print (self.account, self.password, self.lendingnum, self.lending, self.history)


