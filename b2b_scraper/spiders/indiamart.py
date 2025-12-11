import scrapy
from b2b_scraper.items import ProductItem

class IndiaMartSpider(scrapy.Spider):
    name = 'indiamart'
    start_urls = ['https://dir.indiamart.com/search.mp?ss=industrial+machinery']

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
    }

    def parse(self, response):
        for product in response.css('div#prodList li'):
            item = ProductItem()
            item['product_name'] = product.css('.nm-t::text').get()
            item['price_range'] = product.css('.prc::text').get()
            item['supplier_city'] = product.css('.city::text').get()
            item['supplier_name'] = product.css('.cmpny::text').get()
            item['description'] = product.css('.pdscp::text').get()
            yield item
