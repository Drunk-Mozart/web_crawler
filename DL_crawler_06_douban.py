from lxml import etree

import requests
from bs4 import BeautifulSoup

class DouBan:
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        self.starnum = []
        for start_num in range(0,251,25):
            self.starnum.append(start_num)
        self.header = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            }
    def get_top250(self):
        for start in self.starnum:
            start = str(start)
            html = requests.get(self.url,params={'start':start},headers = self.header)
            soup = BeautifulSoup(html.text, "html.parser")
            name = soup.select('#content>div>div.article>ol>li>div>div.info>div.hd>a>span:nth-child(1)')
            for name in name:
                print(name.get_text())


if __name__ == '__main__':
    cls = DouBan()
    cls.get_top250()