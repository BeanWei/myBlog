# -*- coding: utf-8 -*-
import scrapy
import json
from articleSpider.items import JuejinItem

class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['juejin.im']
    start_urls = ['https://timeline-merger-ms.juejin.im/v1/get_tag_entry?src=web&tagId=559a7227e4b08a686d25744f&page=1&pageSize=10&sort=createdAt']

    def __init__(self):
        self.item = JuejinItem()

    def parse(self, response):
        results = json.loads(response.body)
        for article in results['d']['entrylist']:
            self.item['articleUrl'] = article['originalUrl']
            self.item['title'] = article['title']
            if 'username' in ((article['user']['community'].get(article['user']['community'].keys()[0])).keys()):
                authorKey = 'username'
            else:
                authorKey = 'nickname'
            self.item['author'] = article['user']['community'].get(article['user']['community'].keys()[0]).get(authorKey)
            self.item['publishtime'] = article['updatedAt']
            self.item['category'] = article['category']['name']
            tags_list = []
            for t in article['tags']:
                tags_list.append(t['title'])
            self.item['tag'] = ','.join(tags_list)
            yield scrapy.Request(article['originalUrl'],callback=self.parse_detail)

    def parse_detail(self,response):
        content = response.css('.article-content').extract_first()
        self.item['content'] = content
        yield self.item
