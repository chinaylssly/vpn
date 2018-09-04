# _*_ coding:utf-8 _*_ 
import platform

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/5"}
username='chinaylssly@qq.com'
password=u'chinasun00'


email='chinaylssly@qq.com' 
code='nxxqptscflqubbfh'

system=platform.system()

if system=='Windows':
    cookies_file='cookies.json'
    log_file='vpn.log'

elif system=='Linux':
    log_file='/var/log/vpn.log'
    cookies_file='/python/vpn/cookies.json'

else:
    assert 0 ,u'unexcept system :%s'%system


