#_*_ coding:utf-8 _*_

##xinggan='http://www.99mm.me/xinggan/'
##http://www.99mm.me/xinggan/mm_2_2.html
##total=86

import requests
from lxml import etree
from config import headers
import logging


def get_total_by_key(keyword='meitui'):

    url='http://www.99mm.me/%s/'%(keyword)
    response=requests.get(url=url,headers=headers,timeout=30)
    html=response.content
    selector=etree.HTML(html)
    a_total=selector.findtext('.//a[@class="all"]')
    total=int(a_total.replace('.',''))

    log=u'parse url:%s,get total:%s'%(url,total)
    logging.info(log)
    return total





def generate_item(deepth=0):


    info=[
        {'keyword':'meitui','num':1},
        {'keyword':'xinggan','num':2},
        {'keyword':'qingchun','num':3}
        ]

    host='http://www.99mm.me'
    
    for i in info:
        
        keyword=i['keyword']
        num=i['num']

        total=get_total_by_key(keyword=keyword)

        if deepth>0:
            total=deepth

        for page in range(1,total+1):
            yield dict(host=host,num=num,total=total,page=page,keyword=keyword)



def test():

    for item in generate_item(4):
        print item



if __name__ == '__main__':

    test()    
    pass  

