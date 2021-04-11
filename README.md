# Remote Job Market Analytics

This project is developed by job analytics team at Evros, a non-profit which helps refugees with remote job skills and contracts (evrosglobal.org)

This project is deployed to https://job-collector.herokuapp.com/

Contact Burak for questions

Setup

    pip3 install scrapy 

Run (locally):

    scrapy crawl indeed -o indeed.csv -a job="software engineer" -a location="redwood city" -a pages=1

Show output:

    cat indeed.csv #<- this shows the csv file that is the result of the scraping


How it scrapes is in the following file:

    cat jobcollector/spiders/indeed.py

