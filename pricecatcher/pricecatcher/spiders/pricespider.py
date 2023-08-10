# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from pricecatcher.items import PricecatcherItem

class PricespiderSpider(scrapy.Spider):
    name = 'pricespider'
    allowed_domains = ['open.dosm.gov.my']
    start_urls = ['https://open.dosm.gov.my/data-catalogue']

    def parse(self, response):
        price_selected = response.xpath('//h4[text()="Economy: PriceCatcher"]/ancestor::section[1]')
        price_urls = price_selected.xpath('.//ul[1]//li/a[contains(@href, "dosm-public-pricecatcher_pricecatcher")]/@href').getall()

        for url in price_urls:
            yield response.follow(url, callback=self.parse_parquet_link)
    
    def parse_parquet_link(self, response):
        parquet_links = response.xpath('//div[h5[text()="URLs to dataset"]]/ul/li/a[contains(@href, ".parquet")]/@href').getall()

        item = PricecatcherItem(parquet_files=parquet_links)  
        yield item