# AkhtabootScrapper
this is an excercise for scrapping akhtaboot jobs website 


before running the scrapper consider creating a new virtual env that cntain the libraries in the requriments.txt

pip3 install -r requirments.txt

after installing the required packages run the foloowing commnad

scrapy runspider main.py -o test.json

the previous command will traverse all the jobs in akhtaboot.com and return the titles and jobs descriptions to a json files 
