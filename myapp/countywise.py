#from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
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
from html_table_parser import HTMLTableParser
import pandas as pd
import time
def countywise():
    state=['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA',
           'KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH'
           ,'OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
    for i in state:
        j=i.lower()
        #if j=="nv":
        url = 'https://countywise.com/'+j+'/'
        res=requests.get(url)
        
        #r = requests.get(url)

        bs = BeautifulSoup(res.text, 'html.parser')
        p = HTMLTableParser()
        p.feed(res.text)
        table=p.tables[0]
        df=pd.DataFrame(table)
        name=j+'.csv'
        print(name)
        df.to_csv(name,index=False)
        time.sleep(10)
        authcookie = Office365('https://apxnproperty.sharepoint.com', username='dev1@apxnproperty.com', password='DV@apxn365').GetCookies()
        site = Site('https://apxnproperty.sharepoint.com/sites/CountySelection', version=Version.v2016, authcookie=authcookie)
    
        folder = site.Folder('apxn/CountyWise')
        #filecon = open(name, 'rb')
        with open(name, 'rb') as fh: 
            now = datetime.now()
            from datetime import date

            now = datetime.now()

            print("now =", now)


            dt_string = now.strftime("%B")

            name2='countywise_'+j
            res=str(dt_string)+"_"+name2+'.csv'

            print(res)
            time.sleep(10)
            folder.upload_file(fh, res)
#countywise()



