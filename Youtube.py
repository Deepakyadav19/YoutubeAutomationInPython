from selenium import webdriver
from time import sleep
import re
import pickle
import sys
from bs4 import BeautifulSoup

try:
    topic=input("Enter the search keyword for the video : ")
except Exception as e:
    print("Invalid input ")
    ch=input("Do You Want to See the Error ????? (y/n) ")
    if ch=='y':
        print(e)
    sys.exit()
try:
    driver = webdriver.Chrome()
except Exception as e:
    print("ERROR : DRIVER NOT FOUND")
    ch=input("Do You Want to See the Error ????? (y/n) ")
    if ch=='y':
        print(e)
    sys.exit()
try:
    driver.get('https://www.youtube.com/')
except Exception as e:
    print("ERROR : CONNECTION PROBLEM") 
    driver.quit()
    ch=input("Do You Want to See the Error ????? (y/n) ")
    if ch=='y':
        print(e)
    sys.exit()
try:
    # search_box=driver.find_element_by_xpath('//*[@id="search"]')
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(topic)
except Exception as e:
    print("!!!!!!!Error !!!!!!")
    ch=input("Do You Want to See the Error ????? (y/n) ")
    if ch=='y':
        print(e)
    driver.quit()
    sys.exit()
try:
    driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
except Exception as e:
    print('!!!!!!! ERROR !!!!!!!')
    ch=input("Do You Want to See the Error ????? (y/n) ")
    if ch=='y':
        print(e)
    driver.quit()
    sys.exit()
sleep(5)
Youtube_source = driver.page_source
soup = BeautifulSoup(Youtube_source, 'lxml')
for div in soup.find_all('a', {'id': 'video-title'}):
    url='https://www.ssyoutube.com'+div.get('href')
    break
try:
    driver.get(url)
except Exception as e:
    print("ERROR : CONNECTION PROBLEM") 
    driver.quit()
    ch=input("Do You Want to See the Error ????? (y/n) ")
    if ch=='y':
        print(e)
    sys.exit()
downloadPage=driver.page_source
soup2=BeautifulSoup(downloadPage,'lxml')
sleep(5)
try:
    driver.find_element_by_class_name('def-btn-box').click()
except Exception as e:
    print('!!!!!!!! ERROR !!!!!!!')
    ch=input("Do You Want to See the Error ????? (y/n) ")
    if ch=='y':
        print(e)
    driver.quit()
    sys.exit()
ex=input('Enter Anything to Exit')
driver.quit()



    
    
    

