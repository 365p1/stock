# -*- coding: utf8 -*-
from Crawler import Crawler
from BeautifulSoup import BeautifulSoup


class CompanyFinancial:
    def __init__(self):
        self.url = 'http://www.538538.com/Stock_Code_Total---%s---548.html?StockCode=600446&stock_name=&f10=007'
        self.fenhong = 'http://m.538538.com/mstock_Code_Total---600000---548.html?StockCode=%s&stock_name=&f10=010'

if __name__ == "__main__":
    cf = CompanyFinancial()
    url = cf.url % ('000750')
    print url
    page = Crawler.getPage2(url)
    soup = BeautifulSoup(page)
    res = soup.findAll('div', attrs={'id': 'maincontent'})
    for i in res[0].text.split(u'│'):
        tmp = i.encode("utf8")
        print tmp.replace('&nbsp', '').replace(';', '')