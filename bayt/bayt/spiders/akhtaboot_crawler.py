# -*- coding: utf-8 -*-
import scrapy,scrapy.http
import urlparse
from bayt.items import BaytItem
import codecs
import bs4

class AkhtabootCrawlerSpider(scrapy.Spider):
    name = "akhtaboot_crawler"
    allowed_domains = ["akhtaboot.com"]
    start_urls = ('http://www.akhtaboot.com/jobs',)

    def job_details(self,response):
        item = BaytItem()
        soup =bs4.BeautifulSoup(str(response.body))
        item['job_title']= codecs.decode(soup.find('div',{'class':'job-title'}).get_text())
        item['job_description'] = soup.find('div',{'class':'description_div'}).get_text()
        yield item


    def parse(self, response):

        jobs = response.selector.xpath("//a[@class='job-link']//@href").extract()

        for job in jobs:
            yield scrapy.http.Request(urlparse.urljoin(str(response.url), job),callback=self.job_details)

        try:
            next_page= str(response.selector.xpath("//a[@class='next_page']//@href").extract()[0])
            yield scrapy.http.Request(urlparse.urljoin(response.url,next_page),callback=self.parse)
        except Exception as exc :
            print (exc)

