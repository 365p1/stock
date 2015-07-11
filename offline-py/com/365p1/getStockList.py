__author__ = 'chen'
from Crawler import Crawler
from BeautifulSoup import BeautifulSoup
from DbConn import DbConn


class StockList:
    def __init__(self, url):
        self.url = url
        self.db = DbConn()

    def close(self):
        self.db.close()

    def getIndexPage(self):
        return Crawler.getPage(self.url, "gbk")

    def getResult(self, res):
        arr = []
        for item in res:
            tmp = item.text
            l = len(tmp)
            name = tmp[:l - 8].replace(' ', '')
            code = tmp[l - 7:l - 1].replace(' ', '')
            arr.append((name, code))
        return arr


    def getCompany(self):
        page = self.getIndexPage()
        sql = """insert into company(code,name,type) values('%s','%s','%s')"""
        soup = BeautifulSoup(page)
        liangshi = soup.findAll('div', attrs={'class': 'result'})
        hushi = liangshi[0].find('ul').findAll('li')
        shenshi = liangshi[1].find('ul').findAll('li')
        chuangye = liangshi[2].find('ul').findAll('li')
        arr = self.getResult(hushi)
        for i in arr:
            cmd = sql % (i[1], i[0], 'sh')
            self.db.execute(cmd)

        arr = self.getResult(shenshi)
        for i in arr:
            cmd = sql % (i[1], i[0], 'sz')
            self.db.execute(cmd)

        arr = self.getResult(chuangye)
        for i in arr:
            cmd = sql % (i[1], i[0], 'cz')
            self.db.execute(cmd)


if __name__ == "__main__":
    indexUrl = 'http://www.bestopview.com/stocklist.html'
    stockList = StockList(indexUrl)
    stockList.getCompany()
    stockList.close()
