# _*_ coding:utf-8 _*_ 

import requests,re
from lxml import etree
import logging
from config import headers
from traceback import format_exc
import json


def get_content(url='http://www.99mm.me/xinggan/2826.html'):

    html=requests.get(url=url,headers=headers,timeout=30).content
    
    return html


def get_iaStr(html):
    
    iaStr=re.findall("iaStr.*?'(.*?)'",html,re.S)
    if not iaStr:
        return None

    return iaStr[0]


def parse_html(html):
    ##获取网页标题以及域名

    root=etree.HTML(html)
    img=root.find('.//div[@id="picbox"]/img')
    title=img.get('alt')
    src=img.get('src')
    host=src.rsplit('/',3)[0]

    return dict(title=title,host=host)




def parse_iaStr(iaStr,url=None):

    log=u'iaStr is:%s'%(iaStr)
    logging.debug(log)
    keys=[]
    if iaStr:
        l=iaStr.split(',')
        year=l[4] 
        index=l[0] 

        path='%s/%s'%(year,index)

        total=int(l[2])  #total 为图片总张数

        for page in range(1,total+1):##某些网页会发生总页码与图片总索引数不一致的情况，此时跳过异常
            try:
                name=l[page+7]
                key=u'%s-%s'%(page,name)
                keys.append(key)

            except:
                log=u'parse iaStr:%s catch excption:%s'%(iaStr,format_exc())
                logging.error(log)

        iaStr=u','.join(keys)

        return dict(path=path,total=total,iaStr=iaStr)


    else:
        log='cant get iaStr from %s,please check web rule!'%(url)
        logging.warning(log)
        return None
            
 
def get_img_info(url='http://www.99mm.me/xinggan/2826.html'):

    try:
        html=get_content(url=url)
        info=parse_html(html=html)
        iaStr=get_iaStr(html=html)
        iaStr_info=parse_iaStr(iaStr=iaStr,url=url)
        info.update(iaStr_info)
        j=json.dumps(info,ensure_ascii=False)
        log=u'parse url:%s,get info:%s'%(url,j)
        logging.info(log)
        return info
    except:
        log=u'parse url:%s,catch excption:%s'%(url,format_exc())
        logging.error(log)
        return None

def test():

    get_img_info()

    


if __name__ == '__main__':

    
    test()
    pass

