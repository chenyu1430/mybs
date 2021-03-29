# from lxml import html
import requests
import time
import re
from bs4 import BeautifulSoup


class spider_:
    def __init__(self,url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }

    def info_spider(self) -> dict:
        dict={'标题：':None ,'成果完成人：':None ,'第一完成单位：':None,
              '关键词：':None,'中图分类号：':None,'学科分类号：':None,
              '成果简介：':None,'成果类别：':None,'研究起止时间：':None,
              '评价形式：':None,'成果入库时间：':None ,'url':None}
        response = requests.get(url = self.url , headers = self.headers , verify=False)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        # print(soup.prettify())
        title = soup.h1.string
        dict['标题：'] = title
        dict['url'] = self.url
        for p in soup.find_all(class_='row'):
            key = p.find_all(class_ = 'rowtit')
            key = key[0].string
            data = p.find_all(class_='funds')
            data = data[0].string.replace(' ','')
            data = data.replace('\r\n','')
            dict[key] = data
        return dict




if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    url ='https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=SNAD&dbname=SNAD&filename=SNAD000000006385'
    a = spider_(url)
    print(a.info_spider())