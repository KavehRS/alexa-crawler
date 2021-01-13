from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import pandas as pd
import numpy as np
from bs2json import bs2json
import re
import itertools
import requests

    df1 = pd.read_excel('/home/i/Documents/alexsa/alexsa_site.xlsx')
    url_list=list(itertools.chain(*df1.iloc[:,[0]].values.tolist()))

    country_rank_list=[]
    global_rank_list=[]
    Daily_Pageviews_per_Visitor_list=[]
    Daily_Time_on_Site_list=[]
    Bounce_rate_list=[]
    for i in range (len(url_list)):

    alexsa_site_info_url='https://www.alexa.com/siteinfo/'
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    try:
        time.sleep(2)
        driver.get(alexsa_site_info_url+str(url_list[i]))
        try:
            flw=WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#CountryRank > div > div.CountryRank.minTablet')))
            html=driver.execute_script("return arguments[0].outerHTML;", flw)
            html_soup=b(html,'html.parser')
            country_rank_class_find=html_soup.findAll('span',{'class':"num"})
            converter = bs2json()
            json_country_rank_class = converter.convertAll(country_rank_class_find)
            country_rank=json_country_rank_class[0]['text']
            country_rank_list.append(country_rank)
            print('country_rank='+country_rank)
        except:
            country_rank_list.append('')

        try:
            flw=WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#card_rank > section.rank > div.rank-global')))
            html=driver.execute_script("return arguments[0].outerHTML;", flw)
            html_soup=b(html,'html.parser')
            global_rank_class_find=html_soup.findAll('p',{'class':"big data"})
            converter = bs2json()
            json_global_rank_class = converter.convertAll(global_rank_class_find)
            global_rank=json_global_rank_class[0]['text']
            global_rank_list.append(global_rank)
            print('global rank='+global_rank)
        except:
            global_rank_list.append('')
        try:
            flw=WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#card_metrics > section.engagement')))
            html=driver.execute_script("return arguments[0].outerHTML;", flw)
            html_soup=b(html,'html.parser')
            site_metrics=html_soup.findAll('p',{'class':"small data"})
            converter = bs2json()
            json_site_metrics = converter.convertAll(site_metrics)
            Daily_Pageviews_per_Visitor=json_site_metrics[0]['text']
            Daily_Pageviews_per_Visitor_list.append(Daily_Pageviews_per_Visitor)
            print('Daily Pageviews per Visitor='+Daily_Pageviews_per_Visitor)
            Daily_Time_on_Site=json_site_metrics[1]['text']
            Daily_Time_on_Site_list.append(Daily_Time_on_Site)
            print('Daily Time on Site='+ Daily_Time_on_Site)
            Bounce_rate=json_site_metrics[2]['text']
            Bounce_rate_list.append(Bounce_rate)
            print('Bounce_rate='+Bounce_rate)
        except:
            Daily_Pageviews_per_Visitor_list.append('')
            Daily_Time_on_Site_list.append('')
            Bounce_rate_list.append('')

        driver.close()
    except:
        print('please check your address')
        country_rank_list.append('please check your address')
        global_rank_list.append('please check your address')
        Daily_Pageviews_per_Visitor_list.append('please check your address')
        Daily_Time_on_Site_list.append('please check your address')
        Bounce_rate_list.append('please check your address')
dic={'نام سایت':url_list,'Bounce rate':Bounce_rate_list,'Daily Pageviews per Visitor list':Daily_Pageviews_per_Visitor_list,
'Daily Time on Site':Daily_Time_on_Site_list,'global rank':global_rank_list,'country rank':country_rank_list}

output = pd.DataFrame(dic)
output.to_excel('~/Documents/alexsa_output.xlsx',index=False)
