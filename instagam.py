from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
import os
#instagramにアクセス

DRIVER_PATH = os.path.join(os.path.dirname(__file__),'chromedriver')
driver = webdriver.Chrome(DRIVER_PATH)
driver.get("https://www.instagram.com/accounts/login/")

#ログインID・PWを入力
elem_search_word = driver.find_element_by_class_name("_2hvTZ")
elem_search_word.send_keys("username")#username
password = driver.find_element_by_name('password')
password.send_keys("password")#password
password.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
keyword=''#キーワード指定

#ポップアップの後でを選択
elem_search_word = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
driver.implicitly_wait(2)

#検索窓をアドレスバーに直接入力
adress="https://www.instagram.com/explore/tags/"+str(keyword)+"/"
driver.get(adress)
driver.implicitly_wait(6)
driver.find_element_by_xpath("//article/div[1]/div[1]/div[1]/div[1]/div[1]/a").click()

#エラーになるまでいいねしつづける
likecount = 0
while (likecount < 200):
 #いいねをクリック
 driver.implicitly_wait(4)
 driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
 likecount += 1
 #いいねした数を表示
 print("いいね")
 print(likecount)
 driver.implicitly_wait(2)
 #次ボタンをクリック
 elem_search_word = driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()

print ("200いいね!")