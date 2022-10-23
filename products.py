from lib2to3.pgen2 import driver
from urllib import response
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

indica_url="https://www.leafly.com/products/collections/indica?page={}"
sativa_url="https://www.leafly.com/products/collections/sativa?page={}"

indica_page_num=534  #534
indica_page_per_take=18  #18

sativa_page_num=411 #411
sativa_page_per_take=18

productList_slug=[]

# get product list slug
for x in range(indica_page_num):
    url=indica_url.format(x+1)
    driver.get(url)
    for y in range(indica_page_per_take):
        # print(y)
        try:
            if(y<8): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+1)).get_attribute("href"))
            elif(y>=8 and y<12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+2)).get_attribute("href"))
            elif(y>=12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+3)).get_attribute("href"))
        except:
            continue
for x in range(sativa_page_num):
    url=sativa_url.format(x+1)
    driver.get(url)
    for y in range(sativa_page_per_take):
        # print(y)
        try:
            if(y<8): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+1)).get_attribute("href"))
            elif(y>=8 and y<12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+2)).get_attribute("href"))
            elif(y>=12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+3)).get_attribute("href"))
        except:
            continue
# print(productList_slug)
productList_name=[]
productList_url=[]
productList_strain_name=[]
productList_kind=[]
productList_thc=[]
productList_cbd=[]
productList_rating=[]
productList_strain_rating=[]
productList_desc=[]
productList_strain_desc=[]
productList_feelings=[]
productList_negatives=[]
productList_helpwith=[]
productList_brand_name=[]
productList_brand_url=[]
productList_brand_desc=[]

for pi in productList_slug:
    driver.get(pi)
    try:
        productList_name.append(driver.find_element(By.XPATH, "/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/h1").text)
    except:
        productList_name.append('')
    try:
        productList_url.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/ul/li[1]/div/div/picture/source[1]').get_attribute('srcset'))
    except:
        productList_url.append('')
    try:
        productList_strain_name.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[4]/div/div[1]/div[1]/div/div[2]/a').text)
    except:
        productList_strain_name.append('')   
    try:
        productList_kind.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[1]').text)
    except:
        productList_kind.append('')
    try:
        productList_thc.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[2]').text)
    except:
        productList_thc.append('')
    try:
        productList_cbd.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[3]').text)
    except:
        productList_cbd.append('')
    try:
        productList_rating.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/span/span/span[1]').text)
    except:
        productList_rating.append('')
    try:
        productList_strain_rating.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/div[4]/a/span/span/span[1]').text)
    except:
        productList_strain_rating.append('')
    try:
        productList_desc.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[3]/div/div/div/div/div/div').text)
    except:
        productList_desc.append('')
    try:
        productList_strain_desc.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[4]/div/div[1]/div[2]/div/div/div/div/p').text)
    except:
        productList_strain_desc.append('')
    try: 
        productList_feelings.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[4]/div/section/div[3]/div/div/div[1]').text)
    except:
        productList_feelings.append('')
    try:    
        productList_negatives.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[4]/div/section/div[3]/div/div/div[2]').text)
    except:
        productList_negatives.append('')
    try: 
        productList_helpwith.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[4]/div/section/div[3]/div/div/div[3]').text)
    except:
        productList_helpwith.append('')
    try:    
        productList_brand_desc.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[6]/div/div/div/div[2]/div').text)
    except:
        productList_brand_desc.append('')
    try:
        productList_brand_name.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[6]/div/div/div/div[1]/div[2]/div[1]').text)
    except:
        productList_brand_name.append('')
    try:    
        productList_brand_url.append(driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[6]/div/div/div/div[1]/div[1]/div/img').get_attribute('data-srcset'))
    except:
        productList_brand_url.append('')
    # finally:
    #     continue
# print(productList_brand_url)
df = pd.DataFrame({
        'name':productList_name,
        'url':productList_url,
        'strain name':productList_strain_name,
        'kind':productList_kind,
        'thc':productList_thc,
        'cbd':productList_cbd,
        'rating':productList_rating,
        'strain rating':productList_strain_rating,
        'description':productList_desc,
        'strain description':productList_strain_desc,
        'feelings':productList_feelings,
        'negatives':productList_negatives,
        'help with':productList_helpwith,
        'brand name':productList_brand_name,
        'brand url':productList_brand_url,
        'brand description':productList_brand_desc
    })
df.to_excel('products.xlsx', index=False, encoding='utf-8')