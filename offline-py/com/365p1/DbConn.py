import MySQLdb


class DbConn:
    def __init__(self):
        self.conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="chen", db="company", charset="utf8")
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute(self, cmd):
        self.cursor.execute(cmd)
        self.conn.commit()

    def getRes(self):
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = DbConn()
    cmd = "select * from company"
    db.execute(cmd)
    res = db.getRes()
    for i in res:
        print i
