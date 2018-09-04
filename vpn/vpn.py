# _*_ coding:utf-8 _*_ 


import requests
import time
import json,os
import traceback

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/5"}
username='chinaylssly@qq.com'
password=u'chinasun00'
log_file='/var/log/vpn.log'
email='chinaylssly@qq.com' 
code='nxxqptscflqubbfh'

cookies_file='/root/python/vpn/cookies.json'

def get_time():

    return time.asctime().decode('utf-8')

###################################
def init_log():
    if not os.path.exists(log_file):
        log=u'init log file:%s'%log_file
        write_log(log=log)
        with open(log_file,'w')as f:

            pass


#####################################

def write_log(log=''):
    if not isinstance(log,unicode):
        log=log.decode('utf-8','ignore')
    t=get_time()
    log=t+u'--'+log+u'\n'
    with open(log_file,'a')as f:
        log=log.encode('utf-8','ignore')
        f.write(log)

#####################################

import threading

class Wait():
    def __init__(self,timeout=2,message=u'please type your key:'):
        self.timeout=timeout
        self.message=message
        self.p=None
        self.run()

    def wait(self):
        self.p=raw_input(self.message)

    def run(self):
        t=threading.Thread(target=self.wait)
        t.setDaemon(True)
        t.start()
        t.join(self.timeout)

        return self.p


#####################################

def load_cookies(flag=2):
    '''选择载入cookies方式，默认为本地载入'''

    assert flag in [0,1,2],u'flag=0表示从本地载入cookies，flag=1表示从网络载入cookies，flag=2表示用户选择从网络还是本地载入cookies'

    if flag==2:
                                                                                                                                                                                    
        message=u'load cookies from internet please input any key,from location please click ENTER key:'
        
        p=Wait(timeout=5,message=message).p
        print '\n'

        if p==None:
            #p=None,表示用户无输入，默认从本地载入cookies
            cookies=read_cookies()
            if cookies==None:
                '''本地获取不到cookies，将从网络获取cookies'''
                cookies=cookies_from_internet()
                
        else:
            #表示用户有输入，将从将从网络载入cookies
            cookies=cookies_from_internet()

    elif flag==1:
        cookies=cookies_from_internet()
        
    elif flag==0:
        cookies=read_cookies()


    # assert isinstance(cookies,dict),u'cookies must be dict.now get type(cookies) is:'%type(cookies)

    return cookies


def cookies_from_internet():
    '''网络载入cookies'''
    log=u'load cookies from internet!'
    write_log(log=log)

    cookiesjar=login()
    if cookiesjar==0:#登录失败
        return cookiesjar

    elif cookiesjar==None:#网络故障
        return cookiesjar

    else:#登录成功
        cookies=cookiesjar_to_dict(cookiesjar=cookiesjar)
        write_cookies(cookies=cookies)
        return cookies



def write_cookies(cookies):
    '''将网络cookies写入本地'''

    
    j=json.dumps(cookies,ensure_ascii=False)
    log=u'write cookies dict into cookies.json......'
    print log
    write_log(log=log)
    with open(cookies_file,'w')as f:
        f.write(j)


def read_cookies():
    '''从本地载入cookies '''

    if not os.path.exists(cookies_file):
        log=u'localtion cookies.json doest exists,will load cookies from internet'
        write_log(log=log)
        print log
        return None

    with open(cookies_file,'r') as f:
        r=f.read()
    cookies=json.loads(r)
    return cookies

def cookiesjar_to_dict(cookiesjar=None):
    '''将cookiesjar对象转化成字典'''

    d={}
    for i,j in cookiesjar.items():
        d[i]=j

    return d


def dict_to_str(cookies):
    '''字典形式cookies转化成字符串，以便于放入headers中'''
    s=''
    for i in cookies.items():
        k=str(i[0])+'='+str(i[1])+';'
        s+=k

    return s


####################################

def checkin(cookies=None):

    url='http://poro.ws/user/checkin'
    response=requests.post(url=url,headers=headers,cookies=cookies,timeout=30)
    j=response.json()

    ret=j['ret']
    msg=j['msg']

    # print ret,msg
    write_log(log=msg)
    write_log(log=u'********************************************\n')
    return msg

####################################



import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(msg='填写邮件内容',title="菜鸟教程发送邮件测试"):
    ret=True
    try:
        msg=MIMEText(msg,'plain','utf-8')
        msg['From']=formataddr(['',email])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(['',email])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=title                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(email, code)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(email,[email,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print u'邮件发送成功'
    except Exception,e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print e
        ret=False
        print("邮件发送失败")
        
    return ret
###################################

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


##################################


def main():
    init_log()
    cookies=load_cookies(flag=1)
    t=time.asctime()
    if isinstance(cookies,dict):
        log=u'get cookies dict,will checkin'
        write_log(log=log)
        try:
            msg=checkin(cookies=cookies)
        except:
            log=traceback.format_exc()
            write_log(log=log)
    else:
        log=u'type of cookies is not dict'
        write_log(log=log)
        msg=u'can not get userful cookies,checkin failed'
    message=u'%s-%s'%(t,msg)
    mail(msg=message,title=u'vpn签到')



if __name__=='__main__':
    main()
    pass