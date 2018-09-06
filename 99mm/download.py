#_*_ coding:utf-8 _*_


import requests
from config import headers,download_path,database
from sql import mysql
import os,logging
from traceback import format_exc
import time


def download():
    ## img url like :http://fj.kanmengmei.com/2018/2935/1-81.jpg

    sql=mysql(db=database)
    ##connect mysql

    if not os.path.exists(download_path):
        ##创建下载目录
        os.mkdir(download_path)
        log=u'make download path:%s'%download_path
        logging.info(log)
    
    ##通过数据库99mm.img下载未下载的图片
    result=sql.check_table_img()
    data=result.get('data')
    count=result.get('count')
    log=u'本次更新共获取到%s条数据'%count
    logging.info(log)

    for item in data:
        # print item
        host=item.get('host')
        path=item.get('path')
        title=item.get('title')
        iaStr=item.get('iaStr')
        refer=item.get('refer')

        img_path=os.path.join(download_path,title)
        if not os.path.exists(img_path):
            ##创建下载文件夹
            os.mkdir(img_path)
            log=u'make image floder:%s'%(img_path)
            logging.info(log)
        
        ##生成img网络路径
        img_info=iaStr.split(',')
        for info in img_info:
            url=u'%s/%s/%s.jpg'%(host,path,info)
            try:

                headers['Host']=host.split('/')[-1]
                page=info.split('-')[0]
                Referer='%s?url=%s'%(refer,page)
                headers['Referer']=Referer

                ##图片请求需要加入Host，以及Referer
                content=requests.get(url=url,headers=headers,timeout=30).content
                
                name=url.split('/')[-1]
                filename=os.path.join(img_path,name)
                
                if os.path.exists(filename):
                    log=u'img : %s exists'%filename
                    logging.info(log)

                else:
                    with open (filename,'wb') as f:
                        f.write(content)
                        log=u'successfully download img :%s'%filename
                        logging.info(log)

            except:

                log=u'requests url:%s failed,catch exception:%s'%(url,format_exc())
                logging.info(log)

            
            log=u'sleep 0.5 second!'
            logging.info(log)
            time.sleep(0.5)

        sql.update_table_img_status(refer=refer)
        log=u'get all img from %s'%refer
        logging.info(log)


        
    
    
def test():

    download()

        


if __name__ =='__main__':

    test()

    