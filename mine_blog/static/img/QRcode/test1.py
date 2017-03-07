#!/usr/bin/env python
#coding=utf8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = "smtp.joklin.com"
USER = "joklin"
PWD = '12'
TO = "shunchang.lin@teamtopgame.com"
TITLE = "testasjfasjf"
IMAGE = "./qrcode_Joklin.png"
def addimg(src,imgid):
    fp = open(src,'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID',imgid)
    return msgImage

msg = MIMEMultipart('related')
msgtext1 = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")
msg.attach(msgtext1)
msg.attach(addimg(IMAGE,"weekly"))
attach = MIMEText(open(IMAGE,"rb").read(),"base64","utf8")
attach["Content-Type"] = "application/octet-stream"
attach["Content-Disposition"] = "attachment; filename=\"qrcode_Joklin.png\""

msg.attach(attach)

msg['Subject'] = TITLE
msg['From'] = USER
msg['To'] = TO
try:
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    server.login(USER,PWD)
    server.sendmail(USER,TO,msg.as_string())
    server.quit()
    print  "邮件成功发送!!"
except Exception,e:
    print "邮件发送失败:" + str(e)

