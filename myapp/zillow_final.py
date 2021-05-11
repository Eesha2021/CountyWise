import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
import json
import math
import datetime
import pandas as pd
import numpy as np
import csv
import time
zips = pd.read_excel(r'/home/pc/Desktop/aditi/Zip Code Data.xlsx')
zips.zip = zips.zip.astype(str).str.zfill(5)
zips.county_fips = zips.county_fips.astype(str).str.zfill(5)
zips = zips.set_index('zip')

class Zillow:
    results=[]
    zips = pd.read_excel(r'/home/pc/Desktop/aditi/Zip Code Data.xlsx')
    zips.zip = zips.zip.astype(str).str.zfill(5)
    zips.county_fips = zips.county_fips.astype(str).str.zfill(5)
    zips = zips.set_index('zip')

    def fetch(self,state,i):
        #for i in range(1,3):
        if state=="NY":
            url='https://www.zillow.com/ny/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.74660200000001%2C%22east%22%3A-69.79347700000001%2C%22south%22%3A38.33396783381808%2C%22north%22%3A46.9435706624971%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=="AL":
            url='https://www.zillow.com/al/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-89.66901675000001%2C%22east%22%3A-83.69245425000001%2C%22south%22%3A30.104667922828853%2C%22north%22%3A35.04566822259082%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=="AK":
            url='https://www.zillow.com/ak/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-178.5115485%2C%22east%22%3A-130.6990485%2C%22south%22%3A50.20821746586177%2C%22north%22%3A71.87145665734515%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%7D'.format(str(i))
        if state=='AZ':
            url='https://www.zillow.com/az/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-117.90746850000001%2C%22east%22%3A-105.95434350000001%2C%22south%22%3A29.228446651691687%2C%22north%22%3A38.924833787189016%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A8%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='AR':
            url='https://www.zillow.com/ar/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-95.11965874999999%2C%22east%22%3A-89.14309624999999%2C%22south%22%3A32.32606606549018%2C%22north%22%3A37.14449242192138%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='CA':
            url='https://www.zillow.com/ca/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-131.259773%2C%22east%22%3A-107.353523%2C%22south%22%3A27.543269708915965%2C%22north%22%3A46.146290895404626%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A9%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A5%7D'.format(str(i))
        if state=='CO':
            url='https://www.zillow.com/co/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-111.5271285%2C%22east%22%3A-99.5740035%2C%22south%22%3A34.323863198344256%2C%22north%22%3A43.435709750118505%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A10%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='CT':
            url='https://www.zillow.com/ct/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-74.251646625%2C%22east%22%3A-71.263365375%2C%22south%22%3A40.39537683662447%2C%22north%22%3A42.59219143346026%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A11%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A8%7D'.format(str(i))
        if state=='DE':
            url='https://www.zillow.com/de/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-76.880796125%2C%22east%22%3A-73.892514875%2C%22south%22%3A38.00208888402229%2C%22north%22%3A40.27688144089235%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A8%7D'.format(str(i))
        if state=='FL':
            url='https://www.zillow.com/fl/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-89.7811625%2C%22east%22%3A-77.8280375%2C%22south%22%3A22.43843703051361%2C%22north%22%3A32.81219794526462%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A14%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='GA':
            url='https://www.zillow.com/ga/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-86.16657725%2C%22east%22%3A-80.19001475%2C%22south%22%3A30.206462932649835%2C%22north%22%3A35.141994421248256%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A16%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='HI':
            url='https://www.zillow.com/hi/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-160.51489525%2C%22east%22%3A-154.53833275%2C%22south%22%3A17.81219793084099%2C%22north%22%3A23.30261675796978%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A18%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='ID':
            url='https://www.zillow.com/id/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-120.1198225%2C%22east%22%3A-108.1666975%2C%22south%22%3A41.347418104368316%2C%22north%22%3A49.55683068207112%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='IL':
            url='https://www.zillow.com/il/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-97.90175990625%2C%22east%22%3A-80.63125209375%2C%22south%22%3A34.66031331664841%2C%22north%22%3A44.57324474133213%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A21%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='IN':
            url='https://www.zillow.com/in/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-90.758902953125%2C%22east%22%3A-82.123649046875%2C%22south%22%3A37.27188810611148%2C%22north%22%3A42.22975726101611%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A22%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='IA':
            url='https://www.zillow.com/ia/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-97.70742395312502%2C%22east%22%3A-89.07217004687502%2C%22south%22%3A39.51297061510098%2C%22north%22%3A44.311692205201574%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A19%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='KS':
            url='https://www.zillow.com/ks/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-102.637703953125%2C%22east%22%3A-94.002450046875%2C%22south%22%3A35.945864347506856%2C%22north%22%3A40.99470538505932%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A23%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='KY':
            url='https://www.zillow.com/ky/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-90.085865953125%2C%22east%22%3A-81.450612046875%2C%22south%22%3A35.242144040092214%2C%22north%22%3A40.33827702914507%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A24%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='LA':
            url='https://www.zillow.com/la/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-95.71849595312501%2C%22east%22%3A-87.08324204687501%2C%22south%22%3A28.153704089919263%2C%22north%22%3A33.68626153221312%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A25%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='ME':
            url='https://www.zillow.com/me/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-77.61995740624998%2C%22east%22%3A-60.34944959374998%2C%22south%22%3A40.50781440829048%2C%22north%22%3A49.59706499888995%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A28%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='MD':
            url='https://www.zillow.com/md/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.55459245312503%2C%22east%22%3A-72.91933854687503%2C%22south%22%3A36.25238342151048%2C%22north%22%3A41.280410459083065%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A27%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='MA':
            url='https://www.zillow.com/ma/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-73.8423139765625%2C%22east%22%3A-69.5246870234375%2C%22south%22%3A40.83318231791333%2C%22north%22%3A43.22943755167059%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A26%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A8%7D'.format(str(i))
        if state=='MI':
            url='https://www.zillow.com/mi/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-94.90580640625001%2C%22east%22%3A-77.63529859375001%2C%22south%22%3A40.35976095757713%2C%22north%22%3A49.47082766733896%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A30%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='MN':
            url='https://www.zillow.com/mn/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-101.99654340625%2C%22east%22%3A-84.72603559375001%2C%22south%22%3A41.899426989362944%2C%22north%22%3A50.781291776223775%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A31%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='MS':
            url='https://www.zillow.com/ms/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-94.194074453125%2C%22east%22%3A-85.558820546875%2C%22south%22%3A29.845103056372103%2C%22north%22%3A35.28031644174357%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A34%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='MO':
            url='https://www.zillow.com/mo/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-96.754724953125%2C%22east%22%3A-88.119471046875%2C%22south%22%3A35.766799386964095%2C%22north%22%3A40.82773950010639%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A32%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='MT':
            url='https://www.zillow.com/mt/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-118.68003590625001%2C%22east%22%3A-101.40952809375001%2C%22south%22%3A42.12475132369289%2C%22north%22%3A50.97264596855242%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A35%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='NE':
            url='https://www.zillow.com/ne/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-108.31615490624999%2C%22east%22%3A-91.04564709374999%2C%22south%22%3A36.50762321867826%2C%22north%22%3A46.168967396894026%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A38%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='NV':
            url='https://www.zillow.com/nv/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-125.65831340625%2C%22east%22%3A-108.38780559375%2C%22south%22%3A33.36862780360857%2C%22north%22%3A43.45253271800579%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A42%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='NH':
            url='https://www.zillow.com/nh/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-75.88376545312501%2C%22east%22%3A-67.24851154687501%2C%22south%22%3A41.649763681889894%2C%22north%22%3A46.290625252158826%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A39%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='NJ':
            url='https://www.zillow.com/nj/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-79.04194895312499%2C%22east%22%3A-70.40669504687499%2C%22south%22%3A37.571947031031826%2C%22north%22%3A42.508897688589194%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A40%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='NM':
            url='https://www.zillow.com/nm/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-114.66132140625%2C%22east%22%3A-97.39081359375%2C%22south%22%3A28.713015462014482%2C%22north%22%3A39.37785426859083%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A41%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='NY':
            url='https://www.zillow.com/ny/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-80.08766645312501%2C%22east%22%3A-71.45241254687501%2C%22south%22%3A40.37507201082204%2C%22north%22%3A45.11081000846024%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='NC':
            url='https://www.zillow.com/nc/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-88.49624690625002%2C%22east%22%3A-71.22573909375002%2C%22south%22%3A29.74158317439987%2C%22north%22%3A40.28296388352682%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A36%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='ND':
            url='https://www.zillow.com/nd/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-104.619891453125%2C%22east%22%3A-95.984637546875%2C%22south%22%3A45.264586186446124%2C%22north%22%3A49.62542844666756%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='OH':
            url='https://www.zillow.com/oh/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-86.986878453125%2C%22east%22%3A-78.351624546875%2C%22south%22%3A37.89177439879914%2C%22north%22%3A42.80629453416435%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A44%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='OK':
            url='https://www.zillow.com/ok/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-103.034184453125%2C%22east%22%3A-94.398930546875%2C%22south%22%3A32.651864186549474%2C%22north%22%3A37.91603531063371%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A45%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='OR':
            url='https://www.zillow.com/or/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-124.901027453125%2C%22east%22%3A-116.265773546875%2C%22south%22%3A41.82557678405706%2C%22north%22%3A46.45319084834253%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A46%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='PA':
            url='https://www.zillow.com/pa/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.922324453125%2C%22east%22%3A-73.287070546875%2C%22south%22%3A38.65772252022174%2C%22north%22%3A43.517966919384456%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A47%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='RI':
            url='https://www.zillow.com/ri/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-72.57732023828126%2C%22east%22%3A-70.41850676171876%2C%22south%22%3A40.9525377062436%2C%22north%22%3A42.15975410016233%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A50%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D'.format(str(i))
        if state=='SC':
            url='https://www.zillow.com/sc/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-85.24424045312499%2C%22east%22%3A-76.60898654687499%2C%22south%22%3A30.91152217681095%2C%22north%22%3A36.283128898522406%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A51%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='SD':
            url='https://www.zillow.com/sd/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-104.564789953125%2C%22east%22%3A-95.929536046875%2C%22south%22%3A41.881114949370016%2C%22north%22%3A46.50453614925782%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A52%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='TN':
            url='https://www.zillow.com/tn/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-94.61385190625%2C%22east%22%3A-77.34334409375%2C%22south%22%3A30.434795976097288%2C%22north%22%3A40.89138217484895%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A53%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='TX':
            url='https://www.zillow.com/tx/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-108.71209540625%2C%22east%22%3A-91.44158759375%2C%22south%22%3A25.651219152330498%2C%22north%22%3A36.6664689661023%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='UT':
            url='https://www.zillow.com/ut/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-120.18228090625%2C%22east%22%3A-102.91177309375%2C%22south%22%3A34.39253424925378%2C%22north%22%3A44.341248575484%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A55%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='VT':
            url='https://www.zillow.com/ut/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-120.18228090625%2C%22east%22%3A-102.91177309375%2C%22south%22%3A34.39253424925378%2C%22north%22%3A44.341248575484%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A55%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='VA':
            url='https://www.zillow.com/va/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-83.738550953125%2C%22east%22%3A-75.103297046875%2C%22south%22%3A35.432209763844696%2C%22north%22%3A40.51563790565401%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A56%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='WA':
            url='https://www.zillow.com/wa/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-125.199902953125%2C%22east%22%3A-116.564649046875%2C%22south%22%3A45.067788523159116%2C%22north%22%3A49.444280616118206%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A59%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='WV':
            url='https://www.zillow.com/wv/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-84.49931645312499%2C%22east%22%3A-75.86406254687499%2C%22south%22%3A36.38719334439272%2C%22north%22%3A41.40602511620737%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A61%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        if state=='WI':
            url='https://www.zillow.com/wi/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-95.546052%2C%22east%22%3A-83.592927%2C%22south%22%3A40.64950274391737%2C%22north%22%3A48.95326990191947%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A60%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%7D'.format(str(i))
        if state=='WY':
            url='https://www.zillow.com/wy/land/{0}_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-111.872192953125%2C%22east%22%3A-103.236939046875%2C%22south%22%3A40.629297678049944%2C%22north%22%3A45.346278993077995%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A62%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'.format(str(i))
        
        return url 
    def parse(self,url):            
    #import webdrivermanager
        driver = webdriver.Chrome(ChromeDriverManager().install())
        time.sleep(20)
        driver.get(url)
        time.sleep(30)
        html=driver.page_source

        soup=bs4.BeautifulSoup(html,"lxml")
        #content = BS(response, 'lxml')
        collection = soup.find('ul', class_='photo-cards photo-cards_wow photo-cards_short photo-cards_extra-attribution')
        if collection is None:
            print("It worked")
            collection=soup.find('ul',class_='photo-cards photo-cards_wow photo-cards_short')        
        status="Closed"
        #results=[]
        if collection is not None:
            print(len(collection.contents))
            for card in collection.contents:
                script = card.find('script', {'type':'application/ld+json'})
                if script:
                    script_json = json.loads(script.contents[0])
                    if 'latitude' not in script_json['geo']:
                        latitude = np.nan
                        longitude = np.nan
                    else:
                        latitude = float(script_json['geo']['latitude'])
                        longitude = float(script_json['geo']['longitude'])
                    url = script_json['url']

                    
                    acres = card.find('ul', class_='list-card-details').text
                    #print(acres)
                    acres=acres.split(" ")
                    #print(acres[1])
                    if acres[1] == 'acres':
                        final_acres = acres[0]
                    elif acres[1] == 'sqft':
                        #print("Its working!!!")
                        if(acres[0]=='--'):
                            final_acres = np.nan
                        else:
                            acres[0]=acres[0].replace(",","")
                            final_acres = float(acres[0])/43560
                            final_acres=round(final_acres,2)
                    else:
                        final_acres = np.nan
                    if acres[-1]=='sale':
                        status=" ".join(acres[-3:])
                    if acres[-1]=='Sold':
                        status=acres[-1]
                    #print(status)  
                    try:
                        price = card.find('div', class_='list-card-price').text.replace(',', '').replace('$', '')
                        if 'M' in price:
                            price = int(float(price[:-1])*1000000)
                        elif ('K' in price) or ('k' in price):
                            price = int(float(price[:-1])*1000)
                        elif price == '--':
                            price = np.nan
                        else:
                            price = int(price)
                    except:
                        price = np.nan

                    try:
                        address = card.find('address', class_='list-card-addr').text

                        state__ = address.split(',')[2][1:3]

                        zipcode = address[-5:]
                        if not zipcode.isnumeric():
                                #zipcode = 'n/a'
                            zipcode = ''
                    except:
                        address = ''
                        state__ = ''
                        zipcode = ''

                    idx = self.zips.index.to_series()
                    key = idx.get(zipcode, 'missing')
                    if key != 'missing':
                        county = self.zips.loc[zipcode, 'county_name']
                    else:
                        #county = 'n/a'
                        county = ''
                    ''' 
                    try:
                        #status = card.find('div', class_='list-card-variable-text list-card-img-overlay').text
                        note = card.find('div', class_='list-card-type').text
                    except:
                        #status = ''
                        note = ''
                    '''   

                    self.results.append({'Acres': final_acres, 
                                            'Price': price, 
                                            'Address': address,
                                            'State': state__,
                                            'County': county,
                                            'Zip': zipcode,
                                            'Status': status,
                                            'Latitude': latitude,
                                            'Longitude': longitude,                                         
                                            'Link': url})
        else:
            print('None')
    def to_csv(self,name):
        try:
            name=name+".csv"
            
            with open(name, 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
                writer.writeheader()

                for row in self.results:
                    writer.writerow(row)
            self.results=[]
        except:
            time.sleep(120)
    def run(self,state_,state_name):
        date = datetime.datetime.today().strftime('%B')
        print(date)
        print(state_)
        print(state_name)
        name=str(date)+"_"+str(state_)+"_"+"zillow"
        self.results=[]
        for i in range(1,9):
            print()
            url=self.fetch(state_,i)
            self.parse(url)
        self.to_csv(name)
if __name__ == '__main__':
    scraper=Zillow()
    df = pd.read_excel(r'/home/pc/Desktop/Zillow_Query_Parameters.xlsx')
    df = df.set_index('State')
    statename=df['State Name']
    statename.to_dict()
    state_list=['AL','AZ','AR','CO','GA','ID','IN','KY','ME','MN','MS','MO','MT','NV','NH','NY','NC','OK','OR','SC','SD','TN','TX','UT','VT','WA','WI','WY']
    for state_id,state_name in statename.items():
        if state_id in state_list:
            #break
            scraper.run(state_id,state_name)
            #scraper.run(state_id,state_name)
