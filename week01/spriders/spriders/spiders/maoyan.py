# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spriders.items import SpridersItem

# 1. 根据 scrapy 框架提供的 start_requests 方法，初始化并生成 Request 对象，并发送给 Engine，以供 Schedule 使用
# 2. 根据 scrapy 框架提供的 parse 方法，将爬取到的数据做处理，得到想要的数据
#   若按深度不断访问网页中的链接，则需再次调用 scrapy.Request 方法去爬取下一层页面内容
#   定义处理函数，对再次获取到的信息进行处理


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        print(response.url)
        print(response.text)

        i = 0
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]').getall()
        items = []
        item = SpridersItem()
        for movie in movies:
            if i < 10:
                movie_hover = Selector(text=movie).xpath('//div')
                movie_name = movie_hover[1].xpath('./span/text()').get()
                movie_type = movie_hover[2].xpath('./span/text()').get() + " " + movie_hover[2].xpath('./text()')[1].get().strip()
                movie_time = movie_hover[4].xpath('./span/text()').get() + " " + movie_hover[4].xpath('./text()')[1].get().strip()
                item['moive_name'] = movie_name
                item['moive_type'] = movie_type
                item['moive_time'] = movie_time
                items.append(item)
                # print(movie_name)
                # print(movie_type)
                # print(movie_time)
                # print('--------------------------------------')
            i = i + 1
        return items
