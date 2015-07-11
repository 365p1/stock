from Crawler import Crawler
from BeautifulSoup import BeautifulSoup


class PageParser:
    def __init__(self, page):
        self.page = page


if __name__ == "__main__":
    url = 'http://bbs.10jqka.com.cn/codelist.html'
    page = Crawler.getPage(url, "gbk")
    pp = PageParser(page)
    print page