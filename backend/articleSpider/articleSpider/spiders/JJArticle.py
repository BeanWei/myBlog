import scrapy

class JJArticleSpider(scrapy.Spider):
    name = 'jjarticle'
    allowed_domains = ['juejin.im']
    start_urls = ['https://juejin.im/post/5ab1d2f46fb9a028d566fbb2']

    def parse(self, response):
        content = response.css('.article-content').extract_first()
        print(content)