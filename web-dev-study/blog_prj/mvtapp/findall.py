from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests
import re
import pandas as pd
import numpy as np
import os
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By


def text_get(search_item):
    ua = UserAgent(user_cache_server=False) #
    ua = UserAgent(verify_ssl=False) #https 도 들어갈 수 있도록
    userAgent = ua.random
    # options.add_argument(f'user-agent={userAgent}')
    chromediver_path = 'D:/대학원/웹개발특론/vscode_prj/crawling/driver/chromedriver.exe'
    driver = webdriver.Chrome(chromediver_path ) # options=options
    li=[ '제품명', '평점', '5점 개수', '4점 개수', '3점 개수', '2점 개수', '1점 개수', '최저가', '최고가', '등록일' ]
    df = pd.DataFrame(columns=li)
    
    # 데이터를 추출할 url을 리스트로 묶어줌
    
    naver= "https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=%ED%81%AC%EB%A6%AC%EC%8A%A4%EB%A7%88%EC%8A%A4+%EC%84%A0%EB%AC%BC"
    daum ="https://shoppinghow.kakao.com/top"
    google = "https://shopping.google.com/?nord=1"

    # name=['크리스마스 선물']
    category=['별점']


    driver.get(naver)
    print(driver.title)
    print(driver.current_url)    

    elem = driver.find_element(By.NAME,'query')
    elem.clear()

    elem.send_keys(str(search_item))
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element(By.NAME,'query')
    targets = driver.find_elements(By.CSS_SELECTOR, 'div.info_area ul.menu_area > li')
    for target in targets:
        print(target.text)

