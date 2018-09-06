#_*_ coding:utf-8 _*_
import platform

system=platform.system()

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/5"}

if system=='Linux':

    host='47.94.247.249'
    user='aliyun'
    password='chinasun00'
    database='99mm'
    download_path='/root/99mm'
    log_file='/var/log/99mm.log'


elif system=='Windows':

    host='localhost'
    user='root'
    password=''

    database='99mm_linux'
    download_path='download'
    log_file='99mm.log'