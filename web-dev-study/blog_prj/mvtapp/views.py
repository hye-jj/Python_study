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

chromediver_path = 'D:/대학원/웹개발특론/vscode_prj/crawling/driver/chromedriver.exe'

def text_get(df, idx, search_item):
    # ua = UserAgent(user_cache_server=False) 
    # ua = UserAgent(verify_ssl=False) #https 도 들어갈 수 있도록
    # userAgent = ua.random
    # options.add_argument(f'user-agent={userAgent}')
    
    driver = webdriver.Chrome(chromediver_path ) # , ptions=options
    
    # 데이터를 추출할 url을 리스트로 묶어줌
    
    naver= "https://shopping.naver.com/home"
    daum ="https://shoppinghow.kakao.com/top"
    google = "https://shopping.google.com/?nord=1"

    driver.get(naver)
    df.loc[idx, 'title'] = driver.title
    df.loc[idx, 'current_url'] = driver.current_url
    df.loc[idx, 'search'] = search_item
    elem = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/input')
    elem.clear()

    elem.send_keys(str(search_item))
    elem.send_keys(Keys.RETURN)

    # elem = driver.find_element(By.NAME,'query')
    # targets = driver.find_elements(By.CSS_SELECTOR, 'div.info_area ul.menu_area > li')
    target = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li')
    df.loc[idx, 'text'] = target.text 
    
    idx =+ 1
    driver.get(google)
    df.loc[idx, 'title'] = driver.title
    df.loc[idx, 'current_url'] = driver.current_url
    df.loc[idx, 'search'] = search_item

    elem = driver.find_element(By.XPATH,'//*[@id="REsRA"]')
    elem.send_keys(str(search_item))
    elem.send_keys(Keys.RETURN)
    target = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]')
    df.loc[idx, 'text'] = target.text 
    return df, idx

li=[ 'title', 'current_url', 'search' , 'text' ]

global idx 
global df
df = pd.DataFrame(columns=li)
idx = 0


from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from mvtapp.models import LectureDetail, SearchDetail
from django.urls import reverse

# Create your views here.
def detail(request):
    # return HttpResponse('reponse detail')
    # return render(request, 'mvtapp/mvt_detail.html')
    # return render(request, 'mvtapp/new_mvt_detail.html')

    # request 인자 : http 패킷 전달. http 패킷 설정 :header,paybord, *세션(dstip, dst프로토콜)운반.
    if request.method == 'POST':
        target = request.POST.get('search')  # form 의 name - 변수명 request object 가 갖고있음.

        # ORM 을 위한, 모델 오브젝트 생성
        data = SearchDetail()
        data.item = target
        text_get(df, idx, str(target))
        data.std_date = str(datetime.now())

        data.title = df.loc[idx,'title']
        data.url = df.loc[idx,'current_url']
        data.text = df.loc[idx,'text']
        data.save()

        # after input, for review datas in DB
        # objects 클래스명 static method : class 아래 method
        # 일단 다 가져오는 편, 그러고 필터링하는 방법을 선호하심. - 개인의 차이
        datas = SearchDetail.objects.filter(item__contains=target)

        #context 딕셔너리형태
        return render(request, 'mvtapp/new_mvt_result.html', context={'datas':datas})  
        # return HttpResponseRedirect(reverse('mvtapp:detail'))
        # Redirect POST 세션 끝남을 알림(세션 비워줌). - reverse(urls.py 의 패턴 name에 등록한 이름)

    else:
        datas = SearchDetail.objects.all()

    return render(request, 'mvtapp/new_mvt_detail.html', context={'datas':datas})  

def result(request):
    datas = SearchDetail.objects.all()
    return render(request, 'mvtapp/new_mvt_result.html', context={'datas':datas})  










