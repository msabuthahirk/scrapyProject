# -*- coding: utf-8 -*-
import scrapy

class BlablacarSpider(scrapy.Spider):
    name = 'blablacar'
    # allowed_domains = ['www.blablacar.in/']
    start_urls = ['https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/#?fn=new+delhi/']

    def parse(self, response):
        homepage = "https://www.blablacar.in"
        urls = response.css('.relative a::attr(href)').extract()
        for url in urls:
            myurl = homepage + url
            yield scrapy.Request(url=myurl, callback=self.parse_details)
        nextpage = response.css("li.next > a::attr(href)").extract_first()
        nexturl = homepage + nextpage
        yield scrapy.Request(url=nexturl, callback=self.parse)

    def parse_details(self, response):
        yield {
            # 'location' : response.css('.RideName-location--arrowAfter::text').extract_first(),
            # 'node' : response.css('.Footer-footnotes .u-marginNone::text').extract(),
            'source' : response.css(".RideName-location--arrowAfter::text").extract_first(),
            'destination' : response.css(".RideName-mainTrip span+span::text").extract_first(),
            'departure_point' : response.css(".RideDetails div span+span span::text").extract_first(),
            'drop_off_point' : response.css(".RideDetails div+.RideDetails-info span+span span::text").extract_first(),
            'departure_date' : response.css(".RideDetails div+.RideDetails-info+.RideDetails-info span+strong span::text").extract_first(),
            'options' : response.css(".RideDetails div+.RideDetails-info+.RideDetails-info+.RideDetails-info span+span div span span::text").extract_first(),
            'price' : response.css(".Booking-price::text").extract_first(),
            'seats_left' : response.css(".Booking-seats b::text").extract_first(),
            'car_owner_image' : response.css(".PhotoWrapper img::attr(src)").extract_first(),
            'car_owner_name' : response.css(".ProfileCard-info a::text").extract_first(),
            'car_owner_age' : response.css(".ProfileCard-info + .ProfileCard-info::text").extract_first(),
            'car_model' : response.css(".Profile-carDetails::text").extract_first(),
        }
