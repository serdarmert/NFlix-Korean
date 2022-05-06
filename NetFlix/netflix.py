from re import A
import selenium
import time
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions, Chrome


url = "https://www.netflix.com/browse"
s = Service("C:\\Users\Mojo\Documents\Chromedriver.exe")
email = ""
password = ""
profile = "UFBMC2MIZ5GUFCEH24DH7LOHNA\""
profile_link = "a[href^=\"/SwitchProfile?tkn=" + profile
options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=options,service=s)

driver.get(url)
time.sleep(1)


driver.find_element(by=By.NAME, value="userLoginId").send_keys(email)
driver.find_element(by=By.NAME, value="password").send_keys(password)

driver.find_element(by=By.CLASS_NAME, value="btn-submit").click()
time.sleep(1)
driver.find_element(by=By.CSS_SELECTOR,value=profile_link).click()
time.sleep(1)

driver.get("https://www.netflix.com/search?q=korean")
time.sleep(3)
for counter_ in range (1,5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

soup = BeautifulSoup(driver.page_source,"html.parser")
soup.prettify().encode("utf-8", errors="ignore")
titles = soup.find_all("div", class_="title-card")

print(str(len(titles)) + " -" + soup.original_encoding)

f = open("koreans.json", "w+")
f.write("{\n\t\"Kore\":[\n")
id = 1
for title in titles:
    movie_name = title.find("a").get("aria-label").replace("'","&#39;")
    movie_picture = title.find("img").get("src")
    movie_link = "https://www.netflix.com" + title.find("a").get("href")
    movie_id = title.find("a").get("href").replace("/watch/","")
    poz = movie_id.find("?")
    movie_id = movie_id[0:poz]

    f.write("\n\n\t\t{\n\t\t\"id\": \"" + movie_id + "\",\n\t\t\"Name\": \"" + movie_name  + "\",\n\t\t\"Boxart\": \"" + movie_picture  + "\",\n\t\t\"Link\": \"" + movie_link  + "\"\n\t\t},")
    id += 1



f.write("\n\n\t]\n}")
f.close()

