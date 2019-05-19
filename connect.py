import pymysql


def connection():
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '563070147dotA',
        database = 'testdb',
        charset = 'utf8',
        # cursorclass = pymysql.cursors.DictCursor
    )
    cursor = con.cursor()
    return con, cursor


if __name__ == '__main__':
    pass
