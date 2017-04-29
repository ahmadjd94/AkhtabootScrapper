import scrapy
import bs4
import  json
from scrapy.selector import Selector , HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
# import requests
class AkhtabootSpider(scrapy.Spider):
    name = 'Akhtaboot'
    start_urls = ['https://akhtaboot.com/jobs']
    allowed_domains = ["www.akhtaboot.com"]


    # the following function will scrap the contents of the jobs
    def traverse_job(self,response):
        print ("traversing jobs")
        try:

            soup = bs4.BeautifulSoup(response.body)

            job = (soup.find("div", {'class': 'job-title'}))
            print (job.get_text())
            description = (soup.find("div", {'class': 'description_div'}))
            print (description.get_text())
            yield ({'job-title':job.get_text(),"job-description":description.get_text()})
        except Exception as a:
            print ("failure"+ str(a))

    # the following function will travers the pages of the jobs index
    def parse(self, response):
        soup =bs4.BeautifulSoup(response.body)
        try:
            jobs=(soup.find_all("a",{'class':'job-link'}))   # grab link with the class job-link
            targets = []

            for job in jobs:
                # print ("#########printing job########")
                targets.append(job.get('href'))
            next=soup.find("a",{'class':'next_page'})
            print (next.get('href'))
            print ("length pof targert ="+str(len (targets)))
            next_page=response.urljoin(next.get("href"))  # generate the link for the next index page


            for target in targets:  #
                full_url = response.urljoin(target)
                print(full_url)
                try:
                    yield scrapy.Request(full_url, callback=self.traverse_job)
                except Exception as e:
                    print (str(e))
        except:
            pass
        try:
            yield scrapy.Request(next_page, callback=self.parse)


        except:
            pass
    def extract_job(self,response,next_page):
        pass



