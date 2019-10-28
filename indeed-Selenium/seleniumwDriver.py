from selenium import webdriver
import csv

driver=webdriver.Chrome("C:/ChromeDriver/chromedriver.exe")

urls=("https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=10",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=20",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=30",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=40",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=50",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=60",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=70",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=80",
"https://www.indeed.com/jobs?q=wordpress&l=San+Francisco%2C+CA&start=90")

jobtitle=["Job Title"]
comp=["Company Name"]
desc=["Description"]
loc=["Location"]
date=["Job Date"]
def gettext(liste):
    a=0
    for x in liste:
        liste[a]=liste[a].text
        a+=1
def orderlist(liste):
    a=0
    for x in liste:
        liste[a]=liste[a].replace("-"," ")
        a=a+1
for url in urls:
    driver.get(url)
    titles=driver.find_elements_by_class_name("jobtitle")
    comNames=driver.find_elements_by_class_name("company")
    descrs=driver.find_elements_by_class_name("summary")
    locns=driver.find_elements_by_class_name("location")
    dates=driver.find_elements_by_class_name("date")

    gettext(titles)
    gettext(comNames)
    gettext(descrs)
    gettext(locns)
    gettext(dates)

    orderlist(titles)
    orderlist(comNames)
    orderlist(descrs)
    orderlist(locns)
    orderlist(dates)

    jobtitle=jobtitle+titles
    comp=comp+comNames
    desc=desc+descrs
    loc=loc+locns
    date=date+dates

with open ("c:/users/admin/desktop/indeedwordpres.csv", "w", newline="") as f:
    writer =csv.writer(f, delimiter="-")
    
    writer.writerow(jobtitle)
    writer.writerow(comp)
    writer.writerow(desc)
    writer.writerow(loc)
    writer.writerow(date)

"""print(jobtitle)
print(comp)
print(desc)
print(loc)
print(date)"""

