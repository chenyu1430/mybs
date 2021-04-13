# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MybsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #标题
    authors = scrapy.Field() #作者
    company = scrapy.Field() #单位
    key_word = scrapy.Field() #关键词
    zt_class = scrapy.Field() #中图分类号
    xk_class = scrapy.Field() #学科分类号
    synopsis = scrapy.Field() #简介
    cg_class = scrapy.Field() #成果类别
    time = scrapy.Field() #起止时间
    form = scrapy.Field() #评价形式
    save_time = scrapy.Field() #入库时间
