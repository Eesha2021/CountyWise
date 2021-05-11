from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
#import pymysql
import csv
import bs4
import certifi
import json
from django.views.decorators.csrf import csrf_exempt
#from django_cron import CronJobBase, Schedule
from .realtor import *
from .countywise import *
from .zillow import *
from .analysis import *
@csrf_exempt
def index(request):
    an()
    #countywise()
    #realtor()
    return HttpResponse("Data Successfully inserted in Database releator")




    

