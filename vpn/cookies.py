# _*_ coding:utf-8 _*_ 


'''

选择cookies加载方式


'''


from log import write_log
from login import login
from config import cookies_file
import json,os

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



if __name__=='__main__':

    pass