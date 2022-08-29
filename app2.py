from wsgiref.headers import Headers 
from bs4 import BeautifulSoup
import time
import csv 

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
stars_data = []

browser = webdriver.Chrome("helloo-main\chromedriver.exe")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers=["Name","Distance","Mass","Radius"]
    
    for i in range (0,300):
        
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr",attrs={"class","exoplanet"}):
            td_tags = tr_tag.find_all("td")
            temp_list=[]
            for index,td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                            temp_list.append("")
            stars_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("final.csv","w")as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
scrape()