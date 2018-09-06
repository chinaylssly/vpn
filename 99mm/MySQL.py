#_*_ coding:utf-8 _*_

import MySQLdb
import MySQLdb.cursors
import logging
from traceback import format_exc
from config import log_file
##logging为单例模型


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename=log_file,
                    filemode='a'
                    ) 

class MySQL(object):
    u'''数据库主类'''

    def __init__(self,host="localhost",user='root',password='',port=3306,db='99mm',cursorclass=MySQLdb.cursors.DictCursor,charset='utf8'):
        u'''初始化'''

        self.host=host
        self.user=user
        self.password=password
        self.port=port
        self.db=db
        self.cursorclass=cursorclass
        self.charset=charset
        self.connect=MySQLdb.connect(host=self.host,user=self.user,passwd=self.password,db=self.db,port=self.port,charset=self.charset,cursorclass=self.cursorclass)
        self.cursor=self.connect.cursor()
        log=u'connect to %s.%s,current db is:%s'%(host,user,db)
        logging.info(log)


    def execute(self,query):

        try:

            count=self.cursor.execute(query)
            data=self.cursor.fetchall()
            self.connect.commit()
            log=u'run command:"%s",fetchall count is：%s'%(query,count)
            logging.info(log)

            return dict(count=count,data=data)

        except:

            log=u'run command:"%s",catch exception：%s'%(query,format_exc())
            logging.error(log)
            # assert 0,log
            return None



    def close(self,):

        self.connect.close()


    
if __name__ == '__main__':


    mysql=MySQL()
    

    sql='create database if not exists class_test'

    mysql.execute(query=sql)
