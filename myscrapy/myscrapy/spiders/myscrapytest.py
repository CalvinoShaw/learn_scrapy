# -*- coding: utf-8 -*-
import scrapy


class MyscrapytestSpider(scrapy.Spider):
    # 爬虫文件名
    name = 'myscrapytest'
    # 允许爬取的范围
    allowed_domains = ['https://www.baidu.com']
    # 起始url
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print(response.body)
