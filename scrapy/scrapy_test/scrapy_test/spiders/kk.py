# -*- coding: utf-8 -*-
import scrapy


class KkSpider(scrapy.Spider):
    name = 'kk'
    allowed_domains = ['www.bladeblue.top']
    start_urls = ['http://www.bladeblue.top/']

    def parse(self, response):
        print(response.body);
        print("-------------------");
        print(dir(response));
        print(response.headers);
        pass
