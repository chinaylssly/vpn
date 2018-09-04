# _*_ coding:utf-8 _*_ 

from cookies import load_cookies
from sendemail import mail
from log import write_log
import traceback 
import time
from homepage import homepage,parse_html
import json
from checkin import checkin

def main():
    # init_log()
    t=time.asctime()
    cookies=load_cookies(flag=1)
    if isinstance(cookies,dict):
        log=u'get cookies dict,will checkin'
        write_log(log=log)
        try:
            msg=checkin(cookies=cookies)
            html=homepage(cookies=cookies)
            status=parse_html(html=html)
        except:
            log=traceback.format_exc()
            print log
            write_log(log=log)
    else:
        log=u'type of cookies is not dict'
        write_log(log=log)
        msg=u'can not get userful cookies,checkin failed'

    message=dict(logintime=time.asctime(),msg=msg,status=status)
    message=json.dumps(message,ensure_ascii=False)
    # print message
    mail(msg=message,title=u'vpn签到')



if __name__=='__main__':

    main()
    pass
