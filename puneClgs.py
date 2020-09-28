import json, time,requests,pprint
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/home/ng-1/programming/py/chromedriver')
driver.get('https://collegedunia.com/engineering/pune-colleges')
driver.maximize_window()
time.sleep(30)
print(1)
driver.find_element_by_xpath('//*[@id="js-lead-btn-close"]').click()
time.sleep(30)
print(2)

# page loading for total data 
# col-xs-9 nopadding college-content js-sticky-compare
last_height = driver.execute_script("return document.body.scrollHeight")
SCROLL_PAUSE_TIME = 10
print(3)
countA = 0
while True:
    countA+=1
    driver.execute_script('window.scrollTo(0,'+str(last_height//2+last_height//3)+')')
    print("sscrolling")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(countA)
    if new_height == last_height:
        break
    last_height = new_height
    time.sleep(1.2)

htmlParsingData = driver.execute_script('return document.documentElement.outerHTML')
fileData = open('engineeringClgs.com.html',"w+")
fileData.write(htmlParsingData)
print(5)




    

