from .realtor import *
from .countywise import *
from .zillow import *
def my_scheduled_job():
    print("hello")
    realtor()
    
def countywise_cron():
    countywise()

#def zillow_cron():
    #zillow()


  