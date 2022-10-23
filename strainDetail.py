from lib2to3.pgen2 import driver
from urllib import response
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Grab content from URL
strain_origin_url = "https://consumer-api.leafly.com/api/strain_playlists/v2?"
strain_page_per_take = 18  # 18
strain_page_num = 342
# strains list to excel

strainList_slug = []
strainList_name = []
strainList_url = []
strainList_category = []
strainList_thc = []
strainList_cbd = []
strainList_rating = []

# detailed
strainList_flavor_aroms = []
strainList_topeffect = []
strainList_desc = []

strainList_feelings = []
strainList_negatives = []
strainList_flavors = []
strainList_helpwith = []


# webdriver setting
option = Options()
option.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver.exe')


def scrapStrains():

    for x in range(strain_page_num):
        strain_get_url = strain_origin_url + "&skip={}&take={}"
        response = requests.get(strain_get_url.format(x+1, strain_page_per_take))
        strains = json.loads(response.text)['hits']['strain']
        for y in strains:
            strainList_slug.append(y['slug'])
            strainList_name.append(y['name'])
            strainList_url.append(y['nugImage'])
            strainList_category.append(y['category'])
            strainList_thc.append(
                y['cannabinoids']['thc']['percentile50'])
            strainList_cbd.append(
                y['cannabinoids']['cbd']['percentile50'])
            strainList_rating.append(y['averageRating'])


def scrapStrainDetail(url):
    driver.get(url)
    try:
        strainList_flavor_aroms.append(driver.find_element(
            By.XPATH, "//section[1]/div/div[2]/div/div[4]/div/a/div/span[2]").text)
    except:
        strainList_flavor_aroms.append('')
    try:
        strainList_topeffect.append(driver.find_element(
            By.XPATH, "//section[1]/div/div[2]/div/div[4]/div[2]/a/div/span[2]").text)
    except:
        strainList_topeffect.append('')
    try:
        strainList_desc.append(driver.find_element(
            By.XPATH, "//section[1]/div/div[2]/div[2]/div/div").text)
    except:
        strainList_desc.append('')
    try:
        strainList_feelings.append(
            driver.find_element(By.XPATH, "//section[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/a/p").text+"," +
            driver.find_element(By.XPATH, "//section[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/a/p").text+"," +
            driver.find_element(
                By.XPATH, "//section[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[3]/a/p").text
            )
    except:
        strainList_feelings.append('')
    try:
        strainList_negatives.append(
            driver.find_element(By.XPATH, "//section[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[1]/a/p").text+"," +
            driver.find_element(By.XPATH, "//section[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[2]/a/p").text+"," +
            driver.find_element(
                By.XPATH, "//section[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[3]/a/p").text
            )
    except:
        strainList_negatives.append('')
    try:
        strainList_flavors.append(
            driver.find_element(By.XPATH, "//section[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/a/p").text+"," +
            driver.find_element(By.XPATH, "//section[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/a/p").text+"," +
            driver.find_element(
                By.XPATH, "//section[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/a/p").text
            )
    except:
        strainList_flavors.append('')
    try:
        strainList_helpwith.append(driver.find_element(
            By.XPATH, "//section[2]/div[2]/div/div[2]/div[2]/ul").text)
    except:
        strainList_helpwith.append('')

# get strains list
scrapStrains()

# request per strain
for si in strainList_slug:
    st_url = "https://www.leafly.com/strains/" + si
    scrapStrainDetail(st_url)

# print(strainList_flavor_aroms)
# print(strainList_topeffect)
# print(strainList_desc)
# print(strainList_feelings)
# print(strainList_negatives)
# print(strainList_flavors)
# print(strainList_helpwith)

df = pd.DataFrame({
        'name' : strainList_name,
        'url':strainList_url,
        'category':strainList_category,
        'thc':strainList_thc,
        'cbd':strainList_cbd,
        'rating':strainList_rating,
        'flavor&aroms':strainList_flavor_aroms,
        'Top effect':strainList_topeffect,
        'description':strainList_desc,
        'feelings':strainList_feelings,
        'negatives':strainList_negatives,
        'flavors':strainList_flavors,
        'help with':strainList_helpwith
    })
df.to_excel('strains.xlsx', index=False, encoding='utf-8')
