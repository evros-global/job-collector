import requests
from bs4 import BeautifulSoup as bs
import csv

url="https://www.indeed.com/q-Web-Developer-l-San-Francisco,-CA-jobs.html"
r = requests.get(url)
soup = bs(r.text,"html.parser")


def extract_job_title_from_result(soup): 
    jobs = []
    comName=[]
    desc=[]
    loca=[]
    date=[]
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
    print(jobs)
    print(comName)
    print(desc)
    print(date)
    
    with open ("c:/users/admin/desktop/newcsv.csv", "w", newline="") as f:
        writer =csv.writer(f)
        writer.writerows(jobs)
        writer.writerows(comName)
        writer.writerows(desc)
    return(jobs)
extract_job_title_from_result(soup)
