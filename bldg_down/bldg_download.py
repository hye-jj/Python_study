from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import pandas as pd
# import lxml
from tqdm import tqdm
import configparser

from datetime import datetime
from calendar import monthrange
from dateutil.relativedelta import relativedelta 

import os


def webtable(driver, from_date, to_date):
    webtable_df = pd.read_html(driver.find_element(By.XPATH, "//table[@class='bbs_type3']").get_attribute('outerHTML'))[0]
    webtable_df['서비스명1'] = webtable_df['서비스명'].str.split(' ').str[0]
    webtable_df['no'] = range(2,12)
    webtable_df = webtable_df[(webtable_df['데이터제공년월'] > from_date )& (webtable_df['데이터제공년월'] <= to_date)]
    return webtable_df

def fild_download(start, driver, no, file_name, df) :
    global download_list
    # 파일 다운로드    
    driver.find_element(By.XPATH, f'//*[@id="boardMasivDataVO"]/div[5]/table/tbody/tr[{no}]/td[7]/span/a').click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="rad5"]').click()
    driver.find_element(By.ID, 'btnOk').click()

    print('+'*20,f'{file_name} 다운로드','+'*20)

    download_time = df[df.no == no]['파일크기(Mb)'].values[0]*0.75
    print(f'{round(download_time/60,3)} 분')

    #time.sleep(download_time) # 다운로드 MB 나눠서 초로 계산
    for i in tqdm(range(int(download_time))):
        time.sleep(1)

    end = time.time()

    print(f"{df[df.no == no]['파일크기(Mb)'].values[0]*0.7}, {end - start:.5f} sec")

    print('Next')
    download_list.remove(file_name)
    print('남은 파일 (', len(download_list),'개) : ' , download_list)
    
    return driver

def bldg_down(op, from_date, to_date): 
    global download_list, page_num

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
    start = time.time()

    # 로그인 없이 다운로드 가능
    site_url = 'https://open.eais.go.kr/opnsvc/opnSvcInqireView.do?viewType=7'
    driver.get(site_url)
    driver.implicitly_wait(5)

    # 건축물대장 검색
    driver.find_element(By.XPATH, '//*[@id="searchCondition"]/option[4]').click()
    driver.find_element(By.XPATH, '//*[@id="boardMasivDataVO"]/div[4]/span/a').click()
    driver.implicitly_wait(5)

    # 파일목록 테이블 읽기
    webtable_df = webtable(driver, from_date, to_date)

    for file_name in download_list:
        print(file_name)
        
        if len(download_list)  == 0:
            driver.close()
            print('done')
            break

        try:
            no = webtable_df[webtable_df['서비스명1'] == file_name]['no'].values[0]
            driver = fild_download(start, driver, no, file_name, df = webtable_df)
            print(file_name ,': 첫번쨰 페이지에서 다운로드 완료')

        except Exception as error:
            print('=======', error, ': 첫번째 페이지에 없음')
            time.sleep(0.5)

            # 페이지 전환 
            try:
                if len(download_list) > 0 : 
                    driver.find_element(By.XPATH, f'//*[@id="boardMasivDataVO"]/div[7]/a[{page_num}]').click()
                    page_num = page_num + 1 # 페이지 3으로
                    driver.implicitly_wait(30)
                    webtable_df = webtable(driver, from_date, to_date)
                    
                    no = webtable_df[webtable_df['서비스명1'] == file_name]['no'].values[0]
                    driver = fild_download(start,driver, no, file_name, df = webtable_df)
                    print(file_name ,': 두번쨰 페이지에서 다운로드 완료')
                    time.sleep(3)

                    if len(download_list)  == 0:
                        driver.close()
                        print('done')
                        return
                
            except Exception as error:
                print('=======', error, ': 두번째 페이지에 없음')
                time.sleep(0.5)
                if len(download_list) > 0 : 
                    driver.find_element(By.XPATH, f'//*[@id="boardMasivDataVO"]/div[7]/a[{page_num}]').click()
                    driver.implicitly_wait(30)
                    webtable_df = webtable(driver, from_date, to_date)
                    no = webtable_df[webtable_df['서비스명1'] == file_name]['no'].values[0]
                    driver = fild_download(start,driver, no, file_name, df = webtable_df)
                    print(file_name ,': 세번쨰 페이지에서 다운로드 완료')
                    time.sleep(3)

                    if len(download_list)  == 0:
                        driver.close()
                        print('done')
                        return
                    
    chk_end = time.time()
    print(f"중간종료 : {(chk_end - start)/60:.5f} 분")

def check_list(li_path):
    file_list = os.listdir(li_path)
    file_list_zip = [file for file in file_list if file.endswith(".zip")]
    download_list = ['전유공용면적', '오수정화시설', '기본개요', '주택가격', '표제부', '전유부', '부속지번',
                     '지역지구구역', '총괄표제부', '소유자구분정보','층별개요']
    
    li = [file_list[i].split('_')[2].split('+')[0] for i in range(len(file_list_zip))]
    li_d = list(set(download_list) - set(li)) 
    return li_d


if __name__ == "__main__":
    from_date = datetime(datetime.today().year, datetime.today().month, 1) + relativedelta(months=-1)
    from_date = from_date.strftime('%Y-%m-%d')
   
    # 20240926 수정
    # 현재 날짜를 기준으로 전월의 년도와 월을 구합니다.
    today = datetime.today()
    last_month = today + relativedelta(months=-1)
    # monthrange를 사용하여 해당 월의 마지막 날짜를 구합니다.
    last_day_of_last_month = monthrange(last_month.year, last_month.month)[1]
    # 전월의 마지막 날짜를 구합니다.
    to_date = datetime(last_month.year, last_month.month, last_day_of_last_month)
    to_date = to_date.strftime('%Y-%m-%d')

    print('건축물대장 데이터제공년월', from_date, ' ~ ' , to_date)

    root_path = os.getcwd()
    change_dir = f"{root_path}\\files"
    os.makedirs(change_dir, exist_ok=True)
    os.chdir(change_dir)
    download_path = os.getcwd()

    op = Options()
    op.add_experimental_option('prefs',{'download.default_directory': download_path})
    os.chdir("..")

    global download_list
    # 처음 리스트 
    download_list = check_list(download_path)

    global page_num

    # 다운로드 시간 확인
    today = time.strftime('%Y%m%d %H:%M:%S', time.localtime())
    start = time.time()
    print(f"{today} 시작,  목록확인 : ",download_list)

    
    # 누락 list 다운로드 재시도
    while len(download_list) > 0 :
        page_num = 3
        print('다운로드 목록 읽기','='*20)
        print(download_list)
        bldg_down(op, from_date, to_date)  #service, login_url, id, pw, 

        download_list = check_list(download_path)
        end = time.time()
        if end - start > 10800:
            print(f'timeout, {(end - start)/60:.3f} 분, 다운로드 시작 3시간 경과')
            break

    end = time.time()
    end_check = time.strftime('%Y%m%d %H:%M:%S', time.localtime())

    print(f"전체 작업 종료 : {(end - start)/60:.3f} 분, 종료시각 : {end_check}")