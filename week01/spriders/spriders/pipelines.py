# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class SpridersPipeline:

    def process_item(self, item, spider):
        moive_name = item['movie_name']
        moive_type = item['movie_type']
        moive_time = item['movie_time']

        ll = [[moive_name, moive_type, moive_time]]
        movies = pd.DataFrame(data=ll)
        movies.to_csv('movie2.csv', mode='a', index=False, header=False, encoding='utf8')
        print(item)
        return item
