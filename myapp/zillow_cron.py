import requests
from bs4 import BeautifulSoup
import json
import time
import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
#import pymysql
import csv
import bs4
import certifi
import json
from django.views.decorators.csrf import csrf_exempt
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
from datetime import datetime


if _name_ == '__main__':
    scraper = ZillowScraper()
    scraper.run()


    authcookie = Office365('https://deepaksharma11.sharepoint.com', username='Deepak@deepaksharma11.onmicrosoft.com', password='MoreYeahs@11').GetCookies()
    site = Site('https://deepaksharma11.sharepoint.com/sites/MyTeam', version=Version.v2016, authcookie=authcookie)
    folder = site.Folder('apxn/zillow')
    filecon = open('zil.csv', 'rb')
    now = datetime.now()
    from datetime import date

    
    now = datetime.now()
 
    print("now =", now)


    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")

   
    res=str(dt_string)+".csv"
    
    print(res)
    folder.upload_file(filecon, res)


