# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class MaoyanPipeline:
    def process_item(self, item, spider):
        return item

class MaoyanTop10Pipeline:
    def process_item(self, item, spider):
        name = item['name']
        released_time = item['released_time']
        score = item['score']
        
        movie = [name, released_time, score]
        movies = pd.DataFrame(data=[movie])
        movies.to_csv('./maoyaotop10.csv', 
                      encoding='gbk', 
                      header=False, 
                      mode='a',
                      index=False)
        return item
