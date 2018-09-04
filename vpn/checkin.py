# _*_ coding:utf-8 _*_ 

import requests
from config import headers
from cookies import load_cookies
from sendemail import mail
from log import write_log
import traceback 



def checkin(cookies=None):

    url='http://poro.ws/user/checkin'
    response=requests.post(url=url,headers=headers,cookies=cookies,timeout=30)
    j=response.json()

    ret=j['ret']
    msg=j['msg']

  
    write_log(log=msg)
    
    return msg




