# -*- coding: utf-8 -*-
import scrapy

class BlablacarSpider(scrapy.Spider):
    name = 'blablacar'
    # allowed_domains = ['www.blablacar.in/']
    start_urls = ['https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/#?fn=new+delhi/']

    def parse(self, response):
        # yield {
        #     'link' : response.css('.relative a::attr(href)').extract()
        # }
        homepage = "https://www.blablacar.in"
        urls = response.css('.relative a::attr(href)').extract()
        for url in urls:
            myurl = homepage + url
            yield scrapy.Request(url=myurl, callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'location' : response.css('.RideName-location--arrowAfter::text').extract_first(),
            'node' : response.css('.Footer-footnotes .u-marginNone::text').extract(),
        }

# response.css('.RideName-location--arrowAfter::text').extract_first()
# response.css('.Footer-footnotes .u-marginNone::text').extract()
