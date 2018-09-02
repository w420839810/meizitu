# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MzituItem

class MeizituSpider(CrawlSpider):
    name = 'meizitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'^http://www.mzitu.com/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MzituItem()
        i['file_urls'] = response.xpath('.//img[contains(@src,"http")]/@src').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
