# _*_ coding:utf-8 _*_ 



import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from config import email,code 
from log import write_log


my_sender=email  # 发件人邮箱账号
my_pass = code            # 发件人邮箱密码
my_user=email     # 收件人邮箱账号，我这边发送给自己



def mail(msg='填写邮件内容',title="菜鸟教程发送邮件测试"):
    ret=True
    try:
        msg=MIMEText(msg,'plain','utf-8')
        msg['From']=formataddr(['',email])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(['',email])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=title                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(email, code)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(email,[email,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        log=u'邮件发送成功'
        # print log
        write_log(log=log)
        write_log(log=u'********************************************\n')
    except Exception,e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        # print e
        write_log(log=str(e))
        ret=False
        # print("邮件发送失败")
        
    return ret
 
if __name__=='__main__':

    ret=mail()
