from urllib import response
import pandas as pd
import requests
import json
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options

# Grab content from URL
strain_origin_url = "https://consumer-api.leafly.com/api/strain_playlists/v2?"
strain_page_per_take = 18
strain_page_num = 342
# strains list to excel

strainList_name=[]
strainList_url=[]
strainList_category=[]
strainList_thc=[]
strainList_cbd=[]
strainList_rating=[]


def scrapStrain():

    for x in range(strain_page_num):
        strain_get_url = strain_origin_url + "&skip={}&take={}"
        response = requests.get(strain_get_url.format(x, strain_page_per_take))
        strains = json.loads(response.text)['hits']['strain']
        for y in range(strain_page_per_take):
            strainList_name.append(strains[y]['name']) 
            strainList_url.append(strains[y]['nugImage'])
            strainList_category.append(strains[y]['category']) 
            strainList_thc.append(strains[y]['cannabinoids']['thc']['percentile50'])
            strainList_cbd.append(strains[y]['cannabinoids']['cbd']['percentile50'])
            strainList_rating.append(strains[y]['averageRating'])
    df = pd.DataFrame({
        'name' : strainList_name,
        'url':strainList_url,
        'category':strainList_category,
        'thc':strainList_thc,
        'cbd':strainList_cbd,
        'rating':strainList_rating
    })
    df.to_excel('names.xlsx', index=False, encoding='utf-8')


scrapStrain()
