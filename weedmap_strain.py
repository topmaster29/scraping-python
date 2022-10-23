# from lib2to3.pgen2 import driver
# from urllib import response
import pandas as pd
import requests
import json
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path='./chromedriver.exe')


# Grab content from URL
strain_origin_url = "https://api-g.weedmaps.com/wm/v1/strains?"
strain_page_per_take = 100  # 18
strain_page_num = 15
# strains list to excel

strainList_slug = []
strainList_name = []
strainList_url = []
strainList_category = []
strainList_thc = []
strainList_cbd = []
# strainList_rating = []

# detailed
# strainList_flavor_aroms = []
strainList_effects = []
strainList_desc = []

# strainList_feelings = []
# strainList_negatives = []
strainList_flavors = []
# strainList_helpwith = []
ua = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': 'PostmanRuntime/7.26.8', 'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive'}


def scrapStrains():

    for x in range(strain_page_num):
        strain_get_url = (
            strain_origin_url + "&page={}&page_size={}").format(x+1, strain_page_per_take)
        # print(strain_get_url)
        response = requests.get(strain_get_url, headers=headers)
        # print(response.text)
        strains = json.loads(response.text)['data']
        for y in strains:
            strainList_slug.append(y['attributes']['slug'])
            strainList_name.append(y['attributes']['name'])
            strainList_url.append(y['attributes']['hero_image_url'])
            strainList_category.append(y['attributes']['species'])
            strainList_thc.append(y['attributes']['thc_max'])
            strainList_cbd.append(y['attributes']['cbd_max'])
            strainList_desc.append(y['attributes']['description'])

            _ef = ''
            for z in y['attributes']['effects']:
                _ef += z['name'] + ','
            strainList_effects.append(_ef)
            _fl = ''
            for z in y['attributes']['flavors']:
                _fl += z['name'] + ','
            strainList_flavors.append(_fl)

            # strainList_rating.append(strains[y]['averageRating'])
scrapStrains()
df = pd.DataFrame({
    'name': strainList_name,
    'url': strainList_url,
    'category': strainList_category,
    'thc': strainList_thc,
    'cbd': strainList_cbd,

    'Top effect': strainList_effects,
    'description': strainList_desc,
    'flavors': strainList_flavors,

})
df.to_excel('weedstrains.xlsx', index=False, encoding='utf-8')
