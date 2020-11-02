from bs4 import BeautifulSoup
import requests
import json
import time
from urllib import request
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from shutil import which

class Film:
    def __init__(self):
        self.id = None
        self.title = None
        self.link = None
        self.downloadLink=None
        self.quality=None
        self.resolution=None
        self.size=None
        
    def __repr__(self):
        return str(self)  
    def __str__(self):  
        return("\nid: "+ str(self.id) +" quality:"+str(self.quality)+" resolution:"+str(self.resolution)+" size:"+str(self.size) +" downloadLink:" + str(self.downloadLink))

class Egybest():
    def getFilmById(Id):
        s = requests.Session()
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        url="https://zero.egybest.org/movie/" + Id
        content=s.get(url,headers={"User-Agent":user_agent}).text
        soup=BeautifulSoup(content,"html.parser")
        film=Film()
        film.id=Id
        film.link=url
        for tr in soup.select('#watch_dl > table > tbody > tr'):
            td=tr.select_one('td:nth-child(1)')
            film.quality=td.text
            td=tr.select_one('td:nth-child(2)')
            film.resolution=td.text
            td=tr.select_one('td:nth-child(3)')
            film.size=td.text
            td=tr.select_one('td.tar > a.btn.g.dl.nop._open_window')
            apiDownloadLink="https://zero.egybest.org" + td['data-url']
            vidsteamUrl=s.get(apiDownloadLink,headers={"User-Agent":user_agent}).url
        print(vidsteamUrl)
        """
        content=s.get(vidsteamUrl,headers={"User-Agent":user_agent}).text
        soup=BeautifulSoup(content,"html.parser")
        print(soup)
        """
        driver = webdriver.Firefox()
        driver.get(vidsteamUrl)
        main_window = driver.current_window_handle
        driver.find_element_by_xpath('/html/body/div[1]/div/p[2]/a[1]').click()
        driver.switch_to.window(main_window)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div/p[2]/a[1]').click()


        
Egybest.getFilmById("el-feel-el-azraq-2-2019")