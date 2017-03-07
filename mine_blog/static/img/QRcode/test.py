#coding:utf8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
title = 'test'
message = 'asfjkajkfaf'
from_email = 'Joklin'
to_email = ['shunchang.lin@teamtopgame.com','suriealli@163.com']
file_name = './qrcode_Joklin.png'
HOST = 'smtp.joklin.com'
PORT = 25
USER = 'joklin'
PWD  = '12'
fp = open(file_name,'rb')
attach = MIMEImage(fp.read())
fp.close()
attach.add_header('User:',USER)
msg = MIMEMultipart('related')
msgtext1 = MIMEText(message,"text","utf-8")
msg.attach(msgtext1)
msg.attach(attach)
attach = MIMEText(open(file_name,"rb").read(),"base64","utf8")
attach["Content-Type"] = "application/octet-stream"
attach["Content-Disposition"] = "attachment; filename=\"%s.png\"" %USER
msg.attach(attach)
msg['Subject'] = title
msg['From'] = from_email
for email in to_email:
    try:
        server = smtplib.SMTP()
        server.connect(HOST,str(PORT))
        server.login(USER,PWD)
        server.sendmail(USER,email,msg.as_string())
        server.quit()
        print  "邮件成功发送!!"
    except Exception,e:
        print "邮件发送失败:" + str(e)
