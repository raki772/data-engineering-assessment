import scrapy

class ProductItem(scrapy.Item):
    product_name = scrapy.Field()
    price_range = scrapy.Field()
    supplier_city = scrapy.Field()
    supplier_name = scrapy.Field()
    description = scrapy.Field()
