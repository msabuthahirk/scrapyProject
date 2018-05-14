# -*- coding: utf-8 -*-
import scrapy


class BlablacarSpider(scrapy.Spider):
    name = 'blablacar'
    allowed_domains = ['www.blablacar.in/ride-sharing/new-delhi/chandigarh/#?fn=new+delhi']
    start_urls = ['https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/#?fn=new+delhi/']

    def parse(self, response):
        print(response.text)
