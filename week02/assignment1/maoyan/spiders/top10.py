# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.selector import Selector
from maoyan.items import MaoyanTop10Item


class Top10Spider(scrapy.Spider):
    name = 'top10'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'http://127.0.0.1:5000/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movie_infos = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie_info in movie_infos[0:10]:
            item = MaoyanTop10Item()
            movie_link = 'https://maoyan.com' + movie_info\
                .xpath('./a/@href').extract_first().strip()
            yield scrapy.Request(url=movie_link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        movie_info = Selector(response=response).xpath('//div[@class="movie-brief-container"]')

        name = movie_info.xpath('./h1/text()').extract_first().strip()

        movie_detail = movie_info.xpath('./ul/li/text()').extract()
        released_time = movie_detail[-1].strip()

        movie_types = ''
        for movie_type in movie_info.xpath('./ul/li/a/text()').extract():
            movie_types += " " + movie_type
        movie_types = movie_types.strip()

        item['name'] = name
        item['released_time'] = released_time
        item['movie_types'] = movie_types

        yield item