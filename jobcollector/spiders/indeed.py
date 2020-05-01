import scrapy
import datetime
class QuotesSpider(scrapy.Spider):
    name = "indeed"
    def start_requests(self):
        urls = ['https://www.indeed.com/jobs?q='#penetration%20testing&l=Houston%20TX'
        ]
        self.numberOfPages=int(getattr(self,'pages',None))
        job=getattr(self,'job',None)
        location=getattr(self, 'location', None)
        for url in urls: #scrapy crawl indeed -o indeed.csv -a job="" -a location="" -a pages=2
            url+="+".join(job.split(" "))+"&l="
            if location is not None:
                url+="+".join(location.split(" "))

            yield scrapy.Request(url=url, callback=self.parse)
    pass
    def parse(self, response):
        # with open("page"+str(self.currentPage)+".html","wb") as f:
        #     f.write(response.body)
        #yield {"time":datetime.datetime.now()}
        for pieceOfPage in response.xpath('//div[@data-tn-component="organicJob"]'):
            yield {
                "Job Title":list(map(lambda a: a.replace("\n",""),(pieceOfPage.xpath("h2/a/text()|h2/a/*/text()").getall())))[0],
                "Company":list(map(lambda a: a.replace("\n",""),(pieceOfPage.xpath("div/div/span[@class='company']/text()|div/div/span[@class='company']/*/text()").getall())))[0],
                "Location":list(map(lambda a: a.replace("\n",""),(pieceOfPage.xpath("div[@class='sjcl']/span/text()|div[@class='sjcl']/span/*/text()").getall())))[0],
                "Salary":str(pieceOfPage.xpath('div/span/span[@class="salaryText"]/text()').get()).replace("\n",""),
                "Job Description":pieceOfPage.xpath("div[@class='summary']/*/*/text()|div[@class='summary']/*/*/*/text()").getall(),
                "Post Time":pieceOfPage.xpath("div/div/div/div/span[@class='date ']/text()").get(),
                "href":"https://www.indeed.com"+str(pieceOfPage.xpath("h2/a/@href").get())
            }
        pass
        nextPage=response.css('a[data-pp]:last-child::attr(href)').get()#response.xpath('//base/@href').get()
        #yield {"next page":nextPage}
        if nextPage is not None and self.numberOfPages>=int(str(nextPage)[-2:])/10:
            yield response.follow(nextPage, callback=self.parse)
