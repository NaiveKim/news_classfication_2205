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


category = ['판타지', '퓨전', '현대판타지', '무협', '스포츠', '대체역사', '로맨스', "SF", 'BL', '전쟁·밀리터리']

url = 'https://novel.munpia.com/269750'

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
df_titles = pd.DataFrame()

driver.get(url)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/section[1]/div/section/header/div/a').click()
time.sleep(1)
driver.find_element_by_xpath(('//*[@id="NAV-TABLE"]/ul/li[2]/ul/li[3]/a/span')).click()
time.sleep(1)

for i in range(1, 106):
    titles = []
    intros = []
    genres = []

#######
    if i in range(1, 6):
        driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[{}]/a'.format(i)).click()
        time.sleep(0.3)
        for j in range(2, 51):
            driver.find_element_by_xpath('//*[@id="SECTION-LIST"]/ul/li[{}]/a[2]'.format(j)).click()
            time.sleep(0.3)
            x_path_title = '//*[@id="board"]/div[1]/div[3]/h2/a'
            x_path_intro = '//*[@id="STORY-BOX"]/p[1]'
            x_path_genre = '//*[@id="board"]/div[1]/div[3]/p[1]/strong'
            try:
                title = driver.find_element_by_xpath(x_path_title).text
                title = re.compile('[^가-힣 ]').sub('', title)
                titles.append(title)
                intro = driver.find_element_by_xpath(x_path_intro).text
                intro = re.compile('[^가-힣 ]').sub('', intro)
                intros.append(intro)
                genre = driver.find_element_by_xpath(x_path_genre).text
                genre = re.compile('[^가-힣 ]').sub('', genre)
                genres.append(genre)
            except NoSuchElementException as e:
                time.sleep(1)
                print(NoSuchElementException)
            except StaleElementReferenceException as e:
                print(e)
            except:
                print('error')
    else:
        driver.find_element_by_xpath('//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[6]/a').click()
        time.sleep(1)
        for j in range(2, 51):
            driver.find_element_by_xpath('//*[@id="SECTION-LIST"]/ul/li[{}]/a[2]'.format(j)).click()
            time.sleep(0.3)
            x_path_title = '//*[@id="board"]/div[1]/div[3]/h2/a'
            x_path_intro = '//*[@id="STORY-BOX"]/p[1]'
            x_path_genre = '//*[@id="board"]/div[1]/div[3]/p[1]/strong'
            try:
                title = driver.find_element_by_xpath(x_path_title).text
                title = re.compile('[^가-힣 ]').sub('', title)
                titles.append(title)
                intro = driver.find_element_by_xpath(x_path_intro).text
                intro = re.compile('[^가-힣 ]').sub('', intro)
                intros.append(intro)
                genre = driver.find_element_by_xpath(x_path_genre).text
                genre = re.compile('[^가-힣 ]').sub('', genre)
                genres.append(genre)
            except NoSuchElementException as e:
                time.sleep(1)
                print(NoSuchElementException)
            except StaleElementReferenceException as e:
                print(e)
            except:
                print('error')


    ##### for 문 작업해야됨 #####
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
    if i % 10 == 0:
        # df_novels = pd.DataFrame([titles, intros, genres], columns=['titles', 'intros', 'genres'])
        df_novels = pd.DataFrame({'titles':titles, 'intros':intros, 'genres':genres})
        df_novels.to_csv('./Moonpia_crawling_data_{}.csv'.format(i), index=False)
df_novels = pd.DataFrame(titles, intros, genres, columns=['titles', 'intros', 'genres'])
    # df_intros = pd.DataFrame(intros, columns=['intro'])
    # df_genres = pd.DataFrame(genres, columns=['genre'])
    # df = pd.concat([df_titles, df_intros, df_genres], ignore_index=True)
df_novels.to_csv('./Moonpia_crawling_data.csv', index=False)
    # df_intros.to_csv('./Moonpia_intro_crawling_data.csv', index=False)
    # df_genres.to_csv('./Moonpia_genre_crawling_data.csv', index=False)
driver.close()





#//*[@id="NOVELOUS-CONTENTS"]/section[4]/ul/li[6]/a