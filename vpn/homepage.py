# _*_ coding:utf-8 _*_ 

from cookies import load_cookies
from config import headers
import requests,os
from lxml import etree

def homepage(cookies):

    url='http://poro.ws/user'
    response=requests.get(url=url,headers=headers,timeout=30,cookies=cookies)
    content=response.content
    return content

def write_html(html):

    with open('vpn.html','w')as f:
        f.write(html)
    print u'write html into vpn.html'

def read_html():
    print u'read vpn.html from location'
    with open('vpn.html','r')as f:
        return f.read()


def test():
    if not os.path.exists('vpn.html'):
        cookies=load_cookies(flag=0)
        html=homepage(cookies=cookies)
        write_html(html=html)
    else:
        html=read_html()


    print parse_html(html=html)

def parse_html(html):

    selector=etree.HTML(html)

    section=selector.find('.//section[@class="panel panel-default"]')

    a=section.findall('.//a[@class="clear"]')
    d={}
    for i in a:
        strong=i.findtext('.//strong').strip()
        small=i.findtext('.//small').strip()
        d[small]=strong

    return d





if __name__=='__main__':

    test()