#_*_ coding:utf-8 _*_

import requests
from config import headers
from lxml import etree
from traceback import format_exc
import logging,json


def get_html_url(url='http://www.99mm.me/qingchun/'):
    
    try:
        log=u'start new request to :%s'%url
        logging.info(log)

        html=requests.get(url=url,headers=headers,timeout=30).content
        host='http://www.99mm.me'
        selector=etree.HTML(html)

        ul=selector.findall('.//ul[@id="piclist"]//dt/a')
        for a in ul:
            href=a.get('href')
            info=dict(host=host,path=href)
            j=json.dumps(info,ensure_ascii=False)
            log=u'parse url:%s,get info:%s'%(url,j)
            logging.info(log)
            yield info

    except:

        log=u'requests to: %s catch exception: %s'%(url,format_exc())
        logging.error(log)


def test():

    items=get_html_url()
    for item in items:
        print item



if __name__=='__main__':

    test()


    
 



