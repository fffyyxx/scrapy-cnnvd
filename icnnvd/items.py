# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class IcnnvdItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class IcnnvdItem(scrapy.Item):
    # define the fields for your item here like:
    # 漏洞名称
    # name = scrapy.Field()
    url = scrapy.Field()
    CNNVD = scrapy.Field()
    title = scrapy.Field()
    CVE = scrapy.Field()
    grade = scrapy.Field()
    loophole_type = scrapy.Field()
    threat_type = scrapy.Field()
    release_time = scrapy.Field()
    update_time = scrapy.Field()
    loophole_info = scrapy.Field()
    loophole_bulletin = scrapy.Field()
    reference_website = scrapy.Field()

    pass
