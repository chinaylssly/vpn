# _*_ coding:utf-8 _*_ 
import time
import threading


p=None

def wait(timeout=2,message=u'please type your key:'):
  
    def input_flag():
        global p
        p=raw_input(message)


    t=threading.Thread(target=input_flag)
    t.setDaemon(True)##设置主线程为守护线程，子线程随主线程一起退出
    t.start()
    t.join(timeout)

    return p

if __name__=='__main__':

    print wait()
