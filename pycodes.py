from selenium import webdriver
import csv
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:/ChromeDriver/chromedriver.exe")

url=("https://www.indeed.com/q-USA-jobs.html")
search_term=input("Enter Search Term: ")
search_location=input("Enter Locations: ")
job_title=["Job Title"]
company_names=["Company Name"]
descriptions=["Description"]
locations=["Location"]
dates_of_post=["Job Date"]
datailed_descriptions=["Detailed Descriptions"]

def gettext(liste):
    for a in range(0,len(liste)):
        liste[a]=liste[a].text

def orderlist(liste):
    for a in range(0,len(liste)):
        liste[a]=liste[a].replace("-"," ")
driver.maximize_window()
#getting search page
driver.get(url)
#select search term area
driver.find_element_by_xpath("//input[@id='what']").clear()
driver.find_element_by_xpath("//input[@id='what']").send_keys(search_term)

driver.find_element_by_xpath("//input[@id='where']").send_keys(search_location)
driver.find_element_by_xpath("//input[@id='what']").send_keys(Keys.ENTER)
#input("Waiting for pop-up...-press ENTER")
time.sleep(13)
try:
    driver.find_element_by_id("popover-close-link").click()
except:
    pass
titles=driver.find_elements_by_class_name("jobtitle")
comNames=driver.find_elements_by_class_name("company")
descrs=driver.find_elements_by_class_name("summary")
locns=driver.find_elements_by_class_name("location")
dates=driver.find_elements_by_class_name("date")

for a in range(0,10):
    titles[a].click()
    time.sleep(4)
    details=driver.find_element_by_xpath("//div[@id='vjs-desc']").text
    datailed_descriptions.append(details)

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
orderlist(datailed_descriptions)

job_title=job_title+titles
company_names=company_names+comNames
descriptions=descriptions+descrs
locations=locations+locns
dates_of_post=dates_of_post+dates

with open ("c:/users/admin/desktop/indeedresults.csv", "w", newline="") as f:
    writer =csv.writer(f, delimiter="-")
    writer.writerow(job_title)
    writer.writerow(company_names)
    writer.writerow(locations)
    writer.writerow(descriptions)
    writer.writerow(dates_of_post)
    writer.writerow(datailed_descriptions)
driver.close()
"""print(jobtitle)
print(comp)
print(desc)
print(loc)
print(date)"""

