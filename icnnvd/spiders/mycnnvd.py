# -*- coding: utf-8 -*-
import scrapy
from icnnvd.items import IcnnvdItem


class MycnnvdSpider(scrapy.Spider):
    name = 'mycnnvd'
    allowed_domains = ['www.cnnvd.org.cn']
    baseURL = "http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?pageno="
    offset = 0
    start_urls = [baseURL+str(offset)]

    def parse(self, response):
        node_list = response.xpath("//div[@class='list_list']/ul/li")

        for node in node_list:
            # 创建item字段对象来存信息
            item = IcnnvdItem()
            # .extract()是把xpath对象转化为uncoide字符串,并且转化为UTF-8的编码
            # item['name'] = node.xpath("./div[1]/a/text()").extract()[0].strip()
            # item['h'] = node.xpath("./div[1]/a/@href").extract()[0]
            # item['data'] = node.xpath("./div[@style]/text()").extract()[0].strip()
            item['url'] = "http://www.cnnvd.org.cn" + node.xpath("./div[1]/a/@href").extract()[0]
            item['CNNVD'] = node.xpath("./div[1]/p/a/text()").extract()[0]
            # print(name[0])
            # print(data[0])
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.detail_parse)
            # 返回每个item的值给管道，同时继续执行后面的代码
            # yield item

        if self.offset < 3:
            self.offset += 1
            url = self.baseURL + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)

    def detail_parse(self, response):
        # 接受上一级的爬去数据
        item = response.meta['item']

        # 详细页面数据提取
        item['title'] = response.xpath("//div[@class='detail_xq w770']/h2/text()").extract()[0]
        item['CVE'] = response.xpath("//ul/li[3]/a[@rel]/text()").extract()[0].strip()
        item['grade'] = response.xpath("//ul/li[2]/a[@style='color:#4095cc;cursor:pointer;']/text()").extract()[0].strip()
        item['loophole_type'] = response.xpath("//ul/li[4]/a[@style]/text()").extract()[0].strip()
        item['threat_type'] = response.xpath("//ul/li[6]/a[@style]/text()").extract()[0].strip()
        item['release_time'] = response.xpath("//ul/li[5]/a[@style]/text()").extract()[0].strip()
        item['update_time'] = response.xpath("//ul/li[7]/a[@style]/text()").extract()[0].strip()
        # item['loophole_info'] = response.xpath("//div[@class='d_ldjj']/p[1]/text()").extract()[0].strip() + response.xpath("//div[@class='d_ldjj']/p[2]/text()").extract()[0].strip()
        item['loophole_info'] = response.xpath("//div[@class='d_ldjj']/p/text()").extract()[0].strip()
        item['loophole_bulletin'] =response.xpath("//div[@class='fl w770']/div[4]/p[1]/text()").extract()[0].strip() + response.xpath("//div[@class='fl w770']/div[4]/p[2]/text()").extract()[0].strip()
        item['reference_website'] = response.xpath("//div[@class='d_ldjj m_t_20']/p[@class='ckwz']/text()").extract()[0].strip()

        yield item

