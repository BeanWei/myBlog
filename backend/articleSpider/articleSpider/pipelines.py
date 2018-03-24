# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from articleSpider.models import Juejin

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        try:
            articleUrl = Juejin.objects.get(articleUrl = item['originalUrl'])
            print("This article already exist")
            return item
        except Juejin.DoesNotExist:
            pass

        juejin = Juejin
        juejin.articleUrl = item['articleUrl']
        juejin.title = item['title']
        juejin.author = item['author']
        juejin.publishtime = item['publishtime']
        juejin.category = item['category']
        juejin.tag = item['tag']
        juejin.content = item['content']
        juejin.save()
        return item