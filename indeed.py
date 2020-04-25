import requests
from bs4 import BeautifulSoup as bs
import csv

# outputs to csv file called newcsv.csv
def scrape_indeed(url, num_pages):

    #url="https://www.indeed.com/jobs?q=social+media&l=United+States&explvl=entry_level&remotejob=1"
    #num_pages=2
    urls = [url+"&start=" + str(p*10) for p in range(num_pages)]

    jobs = ["Job Title"]
    comName=["Company Name"]
    desc=["Description"]
    loca=["Location"]
    date=["Post Date"]

    for x in urls:

        r = requests.get(x)
        soup = bs(r.text,"html.parser")

        def extract_job_title_from_result(soup): 
            for div in soup.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard unifiedRow row result"}):
                for span in div.find_all(name="span", attrs={"class":"company"}):
                    a=span.get_text()
                    comName.append(a)
                for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
                    jobs.append(a["title"])
                for div in div.find_all(name="div", attrs={"class":"summary"}):
                    a=div.get_text()
                    desc.append(a)
                for span in div.find_all(name="span", attrs={"class":"date"}):
                    a=span.get_text()
                    loca.append(a)
                for div in div.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard-footer"}):
                    a=div.get_text()
                    date.append(a)
            return()
        extract_job_title_from_result(soup)


    #deleting \n and - I'll use - as delimiter
    def orderlist(liste):
        a=0
        for x in liste:
            liste[a]=liste[a].replace("\n","")
            liste[a]=liste[a].replace("-"," ")
            a=a+1
    orderlist(comName)
    orderlist(desc)

    #creating csv
    with open ("./newcsv.csv", "w", newline="") as f:
        writer =csv.writer(f, delimiter="-")
        writer.writerow(["Job Title","Company Name","Description"])
        for i in range(len(jobs)):
            writer.writerow([jobs[i],comName[i],desc[i]])