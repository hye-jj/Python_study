from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# 영화목록 읽기
import pandas as pd

cols = list(pd.read_csv('영화데이터_항목명.txt'))
col_li = []
for i in cols:
    col_li.append(i.strip())

movie_li = pd.read_csv('영화데이터(KOBIS_개봉일람_20240408조회).txt', sep='|')
movie_li = movie_li.T.reset_index(drop=True).T
movie_li.columns = col_li
movie_li.sort_values(by=['전국 관객수'])
movie_li = movie_li[movie_li['전국 관객수'] > 1000]
# print(movie_li.shape)
# movie_li.head(1)

os.makedirs('./data', exist_ok=True)



def movie_crawl(movie_name):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://search.naver.com/')
    elem = driver.find_element_by_id('query')
    elem.send_keys('영화 '+ movie_name + " 관람평")
    elem.send_keys(Keys.RETURN)
    
    actions = driver.find_element(by=By.CLASS_NAME, value='lego_review_list._scroller')
    # actions = driver.find_element(by=By.CSS_SELECTOR, value='#main_pack > div.sc_new.cs_common_module.case_empasis.color_4._au_movie_content_wrap > div.cm_content_wrap > div > div > div:nth-child(4) > div.lego_review_list._scroller')
    time.sleep(1)
    location = actions.location_once_scrolled_into_view
    time.sleep(1)
    print(location)

    # btn = driver.find_element(by=By.CSS_SELECTOR, value='#main_pack > div.sc_new.cs_common_module.case_empasis.color_4._au_movie_content_wrap > div.cm_content_wrap > div > div > div:nth-child(4) > div.lego_review_list._scroller > ul > li:nth-child(2) > div.area_review_content > div > button')
    # btn.click()

    try:
        for i in range(1,1000):
            data1 = driver.find_element(By.XPATH, f'//*[@id="main_pack"]/div[3]/div[2]/div/div/div[4]/div[4]/ul/li[{i}]')
            time.sleep(1)
            location1 = data1.location_once_scrolled_into_view
            time.sleep(1)

            try:
                btn = driver.find_element(By.XPATH, f'//*[@id="main_pack"]/div[3]/div[2]/div/div/div[4]/div[4]/ul/li[{i}]/div[2]/div/button')
                btn.click()
                time.sleep(1)
                
            except Exception as e:
                pass

    except Exception as e:
        print('예외가 발생했습니다. ') #, e



    finally:
        raw_data = actions.text
        raw_li = raw_data.split('별점(10점 만점 중)') 
        df = pd.DataFrame(index=range(len(raw_li)), columns=['리뷰'], data=raw_li) 
        df['영화명'] = movie_name

        filename = f"./data/{movie_name.split(':')[0]}_review_300.pkl"
        df.to_pickle(filename)

        time.sleep(3)
        driver.close()
        return print(filename + "  저장!!!")
    


if __name__ == "__main__":
    # start_time을 체크
    start_time = time.time()

    cnt = len(list(os.listdir('./data')))

    for movie_name in movie_li['영화명'][cnt:]:
        try :
            movie_crawl(movie_name)
        except:
            print(movie_name)

    print("---{}s seconds---".format(time.time()-start_time))
            
        