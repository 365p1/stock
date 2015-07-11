import urllib


class Crawler:
    def __init__(self):
        pass

    @staticmethod
    def getPage(url, encode):
        wp = urllib.urlopen(url)
        content = wp.read()
        page = unicode(content, encode).encode("utf8")
        wp.close()
        return page

    @staticmethod
    def getPage2(url):
        wp = urllib.urlopen(url)
        content = wp.read()
        wp.close()
        return content

if __name__ == "__main__":
    print Crawler.getPage('http://bbs.10jqka.com.cn/codelist.html', "gbk")