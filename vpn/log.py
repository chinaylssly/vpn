# _*_ coding:utf-8 _*_ 

from config import log_file
import time

def get_time():

    return time.asctime().decode('utf-8')

def init_log():
    if not os.path.exists(log_file):
        log=u'init log file:%s'%log_file
        write_log(log=log)
        with open(log_file,'w')as f:

            pass

def write_log(log=''):

    if not isinstance(log,unicode):
        log=log.decode('utf-8','ignore')
    t=get_time()
    log=t+u'--'+log+u'\n'
    with open(log_file,'a')as f:
        log=log.encode('utf-8','ignore')
        f.write(log)
