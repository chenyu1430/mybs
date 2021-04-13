import scrapy
from ..items import MybsItem
from bs4 import BeautifulSoup


class SpiderSpider(scrapy.Spider):
    name = 'spider_'
    allowed_domains = ['www.cnki.net']
    url = 'https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=SNAD&dbname=SNAD&filename=SNAD{}'
    def start_requests(self):
        for i in range(287303, 2000000):
            i = str(i)
            print(i)
            s = '0' * (12 - len(i)) + i
            url = self.url.format(s)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )


    def parse(self, response):
        items = MybsItem()
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        dict_ = {'标题：':'title','成果完成人：':'authors' ,'第一完成单位：':'company',
          '关键词：':'key_word','中图分类号：':'zt_class','学科分类号：':'xk_class',
          '成果简介：':'synopsis','成果类别：':'cg_class','研究起止时间：':'time',
          '评价形式：':'form','成果入库时间：':'save_time'}
        try:
            title = soup.h1.string
            items['title'] = title
            for p in soup.find_all(class_='row'):
                key = p.find_all(class_='rowtit')
                key = key[0].string
                data = p.find_all(class_='funds')
                data = data[0].string.replace(' ', '')
                data = data.replace('\r\n', '')
                items[dict_[key]] = data
            yield items
        except:
            pass


