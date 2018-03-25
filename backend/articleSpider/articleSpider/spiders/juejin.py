# -*- coding: utf-8 -*-
import scrapy
import json
import time
from articleSpider.items import JuejinItem

class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['juejin.im']
    start_urls = ['https://timeline-merger-ms.juejin.im/v1/get_tag_entry?src=web&tagId=559a7227e4b08a686d25744f&page=1&pageSize=10&sort=createdAt']

    def parse(self, response):
        items = []
        results = json.loads(response.body)
        if results['s'] == 1 :
            for article in results['d']['entrylist']:
                item = JuejinItem()
                item['title'] = article['title']
                communityDic = article['user']['community']
                if communityDic == None :
                    item['author'] = "匿名"
                else:
                    commType = list(communityDic.keys())[0]
                    commTypeKeys = communityDic[commType].keys()
                    if 'username' in commTypeKeys:
                        authorKey = 'username'
                    else:
                        authorKey = 'nickname'
                    item['author'] = communityDic[commType][authorKey]
                item['publishtime'] = article['updatedAt']
                item['category'] = article['category']['name']
                tags_list = []
                for t in article['tags']:
                    tags_list.append(t['title'])
                item['tag'] = ','.join(tags_list)
                if 'post' in article['originalUrl']:
                    detailUrl = article['originalUrl']
                else:
                    detailUrl = "https://juejin.im/entry/" + article['objectId']
                item['articleUrl'] = detailUrl
                items.append(item)
            for item in items:
                yield scrapy.Request(url=item['articleUrl'],meta={"item_1":item},callback=self.parse_detail)

        else:
            time.sleep(3)
            self.parse()

    def parse_detail(self,response):
        item = response.meta["item_1"]
        content = response.css('.article-content').extract_first()
        item['content'] = content
        yield item