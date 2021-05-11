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

def realtor():
    url = "https://www.realtor.com/research/data"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    #gcontext = ssl.SSLContext()  # Only for gangstars
    web_byte = urlopen(req).read()

    webpage = web_byte.decode('utf-8')
    soup=bs4.BeautifulSoup(webpage,'html.parser')
    file_url=""
    for link in soup.find_all('a',href=True):
        if(link['href'].endswith('County.csv')):
            file_url =link['href']
            break
    from urllib.request import urlretrieve
    urlretrieve(file_url,'County.csv')
    print(file_url)
    filename = 'realtor1.csv'

    data = requests.get(file_url)  # request the link, response 200 = success

    with open(filename, 'wb') as f:
        f.write(data.content)  # write content of request to file
    f.close()
    authcookie = Office365('https://apxnproperty.sharepoint.com', username='dev1@apxnproperty.com', password='DV@apxn365').GetCookies()
    site = Site('https://apxnproperty.sharepoint.com/sites/CountySelection', version=Version.v2016, authcookie=authcookie)
    folder = site.Folder('apxn/Realtor')
    filecon = open('realtor1.csv', 'rb')
    now = datetime.now()
    from datetime import date
      
     
    now = datetime.now()
 
    print("now =", now)


    dt_string = now.strftime("%B")

   
    res=str(dt_string)+"_Realtor"+".csv"
    
    print(res)
    folder.upload_file(filecon, res)
#realtor()
