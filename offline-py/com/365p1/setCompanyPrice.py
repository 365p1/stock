from Crawler import Crawler
from DbConn import DbConn
import random
import time



class CompanyPrice:
    def __init__(self):
        self.sinaApi = 'http://hq.sinajs.cn/list=%s'
        self.db = DbConn()

    def getPriceInfo(self, code):
        r = random.uniform(0, 3)
        time.sleep(r)
        url = self.sinaApi % (code)
        page = Crawler.getPage(url, "gbk")
        tmp = page.split('"')
        return tmp[1].split(',')

    def getCompanyList(self):
        sql = "select code,type from company;"
        sqlIn = """insert into price(companyid,price,createtime) values('%s','%s','%s')"""
        self.db.execute(sql)
        res = self.db.getRes()
        for i in res:
            if 'sh' == i[1]:
                post = 'sh' + i[0]
            else:
                post = 'sz' + i[0]
            priceInfo = self.getPriceInfo(post)
            if len(priceInfo) < 31:
                print i[0] + " failed!"
                continue
            currentPrice = priceInfo[3]
            currentTime = priceInfo[30]
            cmd = sqlIn % (i[0],currentPrice,currentTime)
            self.db.execute(cmd)
            print i[0], currentPrice, currentTime



if __name__ == "__main__":
    cp = CompanyPrice()
    #print cp.getPriceInfo("s_sz000021")
    cp.getCompanyList()