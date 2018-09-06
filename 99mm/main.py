# _*_ coding:utf-8 _*_ 

from run import Run
from config import system

def main():

    message=u'输入run将运行run_spider,输入update将运行update_spider：'
    if system=='Windows':
        message=message.encode('gbk')

    else:
        message=message.encode('utf-8')
    flag=raw_input(message)

    run=Run()
    if flag=='run':
        run.run_spider()

    elif flag=='update':
        run.update_spider()

    else:
        run.update_spider()



if __name__=='__main__':

    main()

