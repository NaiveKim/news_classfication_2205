######## 연재 완결 변환 X path#########

# //*[@id="SECTION-MENU"]/ul/li[1]/a/span
#
# //*[@id="SECTION-MENU"]/ul/li[2]/a

####페이지 변경######

# 1p //*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[1]/a
# 2p //*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[2]/a
# 3p //*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[3]/a
# 10p //*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[5]/a


##### 제목(리모콘) ########
# 유황숙네 천재 아들 //*[@id="SECTION-LIST"]/ul/li[1]/a[2]
# 프랑스왕가의      //*[@id="SECTION-LIST"]/ul/li[2]/a[2]
# 천재 쉐프        //*[@id="SECTION-LIST"]/ul/li[3]/a[1]
#//*[@id="SECTION-LIST"]/ul/li[3]/a[2]
# 마도군단의 아포칼 //*[@id="SECTION-LIST"]/ul/li[4]/a[2]
# 아포칼립스의 좀비 //*[@id="SECTION-LIST"]/ul/li[5]/a[2]
# 천재타자        //*[@id="SECTION-LIST"]/ul/li[6]/a[2]


##### 제목 ############
# 유황숙네 천재 아들 //*[@id="board"]/div[1]/div[3]/h2/a
#  -- 소개 -- //*[@id="STORY-BOX"]/p[1]
# 프랑스 왕가 //*[@id="board"]/div[1]/div[3]/h2/a
#  -- 소개 -- //*[@id="STORY-BOX"]/p[1]

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time


# category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
# pages = [110, 110, 110, 78, 110, 66]

url = 'https://novel.munpia.com/269750'
# url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
df_titles = pd.DataFrame()

for i in range(1, 106):
    pages = []
    # driver.get()
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/section[1]/div/section/header/div/a').click()
    time.sleep(2)
    driver.find_element_by_xpath(('//*[@id="NAV-TABLE"]/ul/li[2]/ul/li[3]/a/span')).click()
    time.sleep(1)
#######
    # if i == 1:
    driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[1]/a').click()
    time.sleep(1)
    for j in range(2, 52):
        driver.find_element_by_xpath('//*[@id="SECTION-LIST"]/ul/li[{}]/a[2]'.format(j)).click()
        #.format(j)).click()
        time.sleep(1)
    # elif i == 2:
    #     driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[2]/a').click()
    # elif i == 3:
    #     driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[3]/a').click()
    # elif i == 4:
    #     driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[4]/a').click()
    # elif i == 5:
    #     driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[5]/a').click()
    # else:
    #     driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[6]/a').click()

    # url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}#&date=%2000:00:00&page={}'.format(i, j)
    # X_path 값을(?)로 받아오기
    # 1~4번까지
    # 5번 지속적으로 5번 클릭(!) 하는 코드를 만든다.
    # 클릭메소드
    # driver.get(url)
    time.sleep(1)

#     for k in range(1, 5):
#         for l in range(1, 6):
#             x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt[2]/a'.format(k, l)
#             try:
#                 title = driver.find_element_by_xpath(x_path).text
#                 title = re.compile('[^가-힣 ]').sub('', title)
#                 titles.append(title)
#             except NoSuchElementException as e:
#                 time.sleep(0.5)
#                 try:
#                     title = driver.find_element_by_xpath(x_path).text
#                     title = re.compile('[^가-힣 ]').sub('', title)
#                     titles.append(title)
#                 except:
#                     try:
#                         x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt/a'.format(k, l)
#                         title = re.compile('[^가-힣 ]').sub('', title)
#                         titles.append(title)
#                     except:
#                         print('no such enlement')
#             except StaleElementReferenceException as e:
#                 print(e)
#                 print(category[i], j, 'page', k * l)
#             except:
#                 print('error')
#     if j % 30 == 0:
#         df_section_titles = pd.DataFrame(titles, columns=['titles'])
#         df_section_titles['category'] = category[i]
#         df_titles = pd.concat([df_titles, df_section_titles], ignore_index=True)
#         df_titles.to_csv('./crawling_data_{}_{}.csv'.format(category[i], j), index=False)
#         titles = []
#     df_section_titles = pd.DataFrame(titles, columns=['titles'])
#     df_section_titles['category'] = category[i]
#     df_titles = pd.concat([df_titles, df_section_titles], ignore_index=True)
#     df_titles.to_csv('./crawling_data_{}_{}.csv'.format(category[i], j), index=False)
#     titles = []
# driver.close()





