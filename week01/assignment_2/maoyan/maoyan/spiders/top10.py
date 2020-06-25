# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanTop10Item

class Top10Spider(scrapy.Spider):
    name = 'top10'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def start_requests(self):
        url = 'https://maoyan.com/board/4'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="board-item-content"]')

        for movie in movies:
            item = MaoyanTop10Item()
            name = movie.xpath(
                './div[@class="movie-item-info"]/p/a/text()').extract_first()
            released_time = movie.xpath(
                './div/p[@class="releasetime"]/text()').extract_first()
            
            score_integer = movie.xpath(
                './div[@class="movie-item-number score-num"]/p/i[@class="integer"]/text()').extract_first() 
            score_fraction = movie.xpath(
                './div[@class="movie-item-number score-num"]/p/i[@class="fraction"]/text()').extract_first()
            score = float(score_integer + score_fraction)

            item['name'] = name
            item['released_time'] = released_time
            item['score'] = score
            
            yield item