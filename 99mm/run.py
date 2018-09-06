#_*_ coding:utf-8 _*_

from item import generate_item
from html import get_html_url
from img import get_img_info
from sql import mysql
from config import database
import os,json,logging
from traceback import format_exc
import time
from download import download

class Run():

    def __init__(self,):
        ##创建数据库99mm，以及table（item,html,img）

        try:
            self.sql=mysql(db=database)

        except:

            log=u'cant find db:%s,will create this db!'%database
            logging.info(log)

            sql=mysql()
            sql.create_database()
            sql.close()

            self.sql=mysql(db=database)
            self.sql.create_table_item()
            self.sql.create_table_html()
            self.sql.create_table_img()

    
    def insert_data_to_item(self,deepth=0):

        items=generate_item(deepth=deepth)
        for item in items:
            host=item.get('host')
            total=item.get('total')
            num=item.get('num')
            page=item.get('page')
            keyword=item.get('keyword')

            self.sql.insert_table_item(host=host,total=total,num=num,page=page,keyword=keyword)





    def insert_data_to_html(self,data):
        #item_url like http://www.99mm.me/qingchun/mm_3_3.html

        # result=self.sql.check_table_item()
        # data=result.get('data')
        for each in data:
            page=each.get('page')
            host=each.get('host')
            num=each.get('num')
            keyword=each.get('keyword')

            item_url='%s/%s/mm_%s_%s.html'%(host,keyword,num,page)
            if page==1:
                item_url='%s/%s/'%(host,keyword)
            
            html_info=get_html_url(url=item_url)
            for info in html_info:
                
                path=info.get('path')
                host=info.get('host')
                self.sql.insert_table_html(path=path,host=host)

            self.sql.update_table_item_status(keyword=keyword,page=page)
            log=u'keyword=%s,page=%s have finished'%(keyword,page)
            logging.info(log)

            
            log=u'sleep 1 second !'
            logging.info(log)
            time.sleep(1)


    def insert_data_to_img(self,):

        result=self.sql.check_table_html()
        data=result.get('data')


        for item in data:

            path=item.get('path')
            host=item.get('host')
            html_url=host+path
            img_info=get_img_info(url=html_url)

            path=img_info.get('path')
            host=img_info.get('host')
            total=img_info.get('total')
            iaStr=img_info.get('iaStr')
            title=img_info.get('title')

            self.sql.insert_table_img(path=path,host=host,total=total,iaStr=iaStr,title=title,refer=html_url)

            
            log=u'sleep 1 second!!!'
            logging.info(log)
            time.sleep(1)





    def run_spider(self,deepth=0):
        ##deepth为爬取深度，deepth=3表示每个主题只爬取三页，deepth=0表示不限制爬取深度

        log=u'start insert data into item'
        logging.info(log)
        self.insert_data_to_item(deepth=deepth)

        log=u'start insert data into html'
        logging.info(log)
        result=self.sql.check_table_item()
        data=result.get('data')
        self.insert_data_to_html(data=data)

        log=u'start insert data into img'
        logging.info(log)
        self.insert_data_to_img()

        ##默认不开启下载模块，需要下载请将下面三行取消注释
        # log=u'start downlaod img to localtion'
        # logging.info(log)
        # download()



    def update_spider(self,deepth=3):
        ##deepth为更新深度，如果距离上次爬取时间不长，建议将deepth设置小一点
        log=u'start generate item info deepth=%s'%deepth
        logging.info(log)
        data=generate_item(deepth=deepth)


        log=u'start update data to html'
        logging.info(log)
        self.insert_data_to_html(data=data)

        log=u'start update data into img'
        logging.info(log)
        self.insert_data_to_img()


        ###默认不开启下载模块，需要下载请将下面三行取消注释
        # log=u'start download img to localtion'
        # logging.info(log)
        # download()




def test_run_spider():
    run=Run()
    run.run_spider(deepth=1)


def test_update_spider():
    run=Run()
    run.update_spider(deepth=2)
            

            

    




if __name__=='__main__':

    test_run_spider()
    test_update_spider()
    pass
