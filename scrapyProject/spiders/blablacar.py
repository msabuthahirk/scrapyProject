# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import scrapy


class BlablacarSpider(scrapy.Spider):
    name = 'blablacar'
    allowed_domains = ['www.blablacar.in/']
    start_urls = ['https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/#?fn=new+delhi/']

    def parse(self, response):
        # link = response.css('.relative a::attr(href)').extract()
        yield {
            'link' : response.css('.relative a::attr(href)').extract()
        }
