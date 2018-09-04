# _*_ coding:utf-8 _*_ 

import requests
from config import headers,username,password
import os
from log import write_log
import traceback 

def login():

    url='http://poro.ws/auth/login'
    data={
        'email':username,
        'passwd':password,
        'remeber_me':'week',
        }

    try:

        response=requests.post(url=url,headers=headers,data=data,timeout=30)
        content=response.json()
        ret=content['ret']
        msg=content['msg']
        # print type(msg)
        # msg=msg.encode('utf-8')
        write_log(log=msg)
        if ret:
            # print msg
            print u'login successfully!'
            return response.cookies

        else:
            # print msg
            print u'login failed!'
            return 0


    except Exception,e:
        print e
        log=traceback.format_exc()
        write_log(log=log)
        return None