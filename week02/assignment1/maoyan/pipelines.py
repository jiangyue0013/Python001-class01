# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'spider_test_db_admin',
    'password' : 'test@1234',
    'db' : 'spider_test_db',
}

class MaoyanPipeline:
    def process_item(self, item, spider):
        return item


class MaoyanTop10Pipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            database = dbInfo['db']
            )

        name = item['name']
        released_time = item['released_time']
        movie_type = item['movie_type']

        sql = f'insert into maoyan_movies ( name, types, released_time) values ({name}, {movie_type}, {released_time});'

        cursor = conn.cursor()
        result = cursor.execute(sql)
        return item
