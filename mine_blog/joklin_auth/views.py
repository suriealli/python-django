# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail,SafeMIMEMultipart
from email.mime.image import MIMEImage
from django.core.exceptions import PermissionDenied
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.utils.http import (base36_to_int, is_safe_url,
                               urlsafe_base64_decode, urlsafe_base64_encode)
from joklin_auth.forms import JoklinUserCreationForm, JoklinPasswordRestForm
from joklin_auth.models import JoklinUser
from joklin_system.models import Notification
import time,datetime,os,json,base64
from PIL import Image
import logging
import uuid,qrcode,totp_auth

logger = logging.getLogger(__name__)

# Create your views here.


class UserControl(View):

    def post(self, request, *args, **kwargs):
        # 获取要对用户进行什么操作
        slug = self.kwargs.get('slug')

        if slug == 'login':
            return self.login(request)
        elif slug == "logout":
            return self.logout(request)
        elif slug == "register":
            return self.register(request)
        elif slug == "changepassword":
            return self.changepassword(request)
        elif slug == "forgetpassword":
            return self.forgetpassword(request)
        elif slug == "changetx":
            return self.changetx(request)
        elif slug == "resetpassword":
            return self.resetpassword(request)
        elif slug == "notification":
            return self.notification(request)

        raise PermissionDenied

    def get(self, request, *args, **kwargs):
        # 如果是get请求直接返回404页面
        raise Http404

    def login(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)

        errors = []

        if user is not None:
            auth.login(request, user)
        else:
            errors.append(u"密码或者用户名不正确")

        mydict = {"errors": errors}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )

    def logout(self, request):
        if not request.user.is_authenticated():
            logger.error(u'[UserControl]用户未登陆')
            raise PermissionDenied
        else:
            auth.logout(request)
            return HttpResponse('OK')

    def register(self, request):
        username = self.request.POST.get("username", "")
        password1 = self.request.POST.get("password1", "")
        password2 = self.request.POST.get("password2", "")
        email = self.request.POST.get("email", "")
        form = JoklinUserCreationForm(request.POST)

        errors = []
        # 验证表单是否正确
        if form.is_valid():
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
            #二次验证
            sha1 = str(uuid.uuid4())
            totp = totp_auth.OtpAuth(sha1)
            uri = totp.to_uri('totp','Joklin',username)
            image = qrcode.make(uri)
            file_name = settings.STATIC_ROOT + os.sep + "img" + os.sep + "QRcode" + os.sep + "qrcode_%s.png" %username
            image.save(file_name)

            title = u"欢迎来到 {} ！".format(site_name)
            # message = "".join([
            #     u"你好！ {} ,感谢注册 {} ！\n\n".format(username, site_name),
            #     u"请牢记以下信息：\n",
            #     u"用户名：{}\n".format(username),
            #     u"邮箱：{}\n".format(email),
            #     u"网站：http://{}\n\n".format(domain),
            #     u"请使用google authenticator扫描您的二维码信息：\n",
            # ])
            message = u'''
                你好！ %s ,感谢注册 %s ！<br><br>
                请牢记以下信息：<br>
                用户名：%s<br>
                邮箱：%s<br>
                网站：http://%s<br><br>
                请使用google authenticator扫描您的二维码信息：<br>
            ''' %(username,site_name,username,email,domain)
            from_email = "Joklin"
            to_email = [email,'suriealli@163.com']
            # try:
                # #send_mail(title, message, from_email, to_email)
                # msg = EmailMultiAlternatives(title, message, from_email, to_email)
                # #msg.content_subtype = "html"  #默认格式
                # fp = open(file_name,'rb')
                # attach = MIMEImage(fp.read())
                # fp.close()
                # attach.add_header('User:',username)
                # # 添加附件（可选）
                # msg.attach_alternative(attach,"application/octet-stream")
                # msg.attach(file_name)  #attach_file()
                # # msg.attach_alternative(html_content, "text/html") #如果某行需要改为html格式，可以如此。
                # msg.send()
            result = sendEmail_MIMEMultipart(title,message,from_email,to_email,file_name,)
            if "失败" in result:
                logger.error(
                    u'[UserControl]用户注册邮件发送失败:[{}]/[{}]'.format(
                        username, email
                    )
                )
                return HttpResponse(u"发送邮件错误!\n注册失败", status=500)
            # except Exception as e:
            #     logger.error(
            #         u'[UserControl]用户注册邮件发送失败:[{}]/[{}]'.format(
            #             username, email
            #         )
            #     )
            #     return HttpResponse(u"发送邮件错误!\n注册失败", status=500)

            new_user = form.save()
            #修改sha
            Joklin_User=JoklinUser.objects.get(username=username)
            Joklin_User.SHA1=sha1
            Joklin_User.save()
            user = auth.authenticate(username=username, password=password2)
            auth.login(request, user)

        else:
            # 如果表单不正确,保存错误到errors列表中
            for k, v in form.errors.items():
                # v.as_text() 详见django.forms.util.ErrorList 中
                errors.append(v.as_text())

        mydict = {"errors": errors}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )

    def changepassword(self, request):
        if not request.user.is_authenticated():
            logger.error(u'[UserControl]用户未登陆')
            raise PermissionDenied

        form = PasswordChangeForm(request.user, request.POST)

        errors = []
        # 验证表单是否正确
        if form.is_valid():
            user = form.save()
            auth.logout(request)
        else:
            # 如果表单不正确,保存错误到errors列表中
            for k, v in form.errors.items():
                # v.as_text() 详见django.forms.util.ErrorList 中
                errors.append(v.as_text())

        mydict = {"errors": errors}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )

    def forgetpassword(self, request):
        username = self.request.POST.get("username", "")
        email = self.request.POST.get("email", "")

        form = JoklinPasswordRestForm(request.POST)

        errors = []

        # 验证表单是否正确
        if form.is_valid():
            token_generator = default_token_generator
            from_email = None
            opts = {
                    'token_generator': token_generator,
                    'from_email': from_email,
                    'request': request,
                   }
            user = form.save(**opts)

        else:
            # 如果表单不正确,保存错误到errors列表中
            for k, v in form.errors.items():
                # v.as_text() 详见django.forms.util.ErrorList 中
                errors.append(v.as_text())

        mydict = {"errors": errors}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )

    def resetpassword(self, request):
        uidb64 = self.request.POST.get("uidb64", "")
        token = self.request.POST.get("token", "")
        password1 = self.request.POST.get("password1", "")
        password2 = self.request.POST.get("password2", "")

        try:
            uid = urlsafe_base64_decode(uidb64)
            user = JoklinUser._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, JoklinUser.DoesNotExist):
            user = None

        token_generator = default_token_generator

        if user is not None and token_generator.check_token(user, token):
            form = SetPasswordForm(user, request.POST)
            errors = []
            if form.is_valid():
                user = form.save()
            else:
                # 如果表单不正确,保存错误到errors列表中
                for k, v in form.errors.items():
                    # v.as_text() 详见django.forms.util.ErrorList 中
                    errors.append(v.as_text())

            mydict = {"errors": errors}
            return HttpResponse(
                json.dumps(mydict),
                content_type="application/json"
            )
        else:
            logger.error(
                u'[UserControl]用户重置密码连接错误:[{}]/[{}]'.format(
                    uid64, token
                )
            )
            return HttpResponse(
                u"密码重设失败!\n密码重置链接无效，可能是因为它已使用。可以请求一次新的密码重置.",
                status=403
            )

    def changetx(self, request):
        if not request.user.is_authenticated():
            logger.error(u'[UserControl]用户未登陆')
            raise PermissionDenied

        # 本地保存头像
        data = request.POST['tx']
        if not data:
            logger.error(
                u'[UserControl]用户上传头像为空:[%s]'.format(
                    request.user.username
                )
            )
            return HttpResponse(u"上传头像错误", status=500)

        imgData = base64.b64decode(data)

        filename = "tx_100x100_{}.jpg".format(request.user.id)
        filedir = "joklin_auth/static/tx/"
        static_root = getattr(settings, 'STATIC_ROOT', None)
        if static_root:
            filedir = os.path.join(static_root, 'tx')
        if not os.path.exists(filedir):
            os.makedirs(filedir)

        path = os.path.join(filedir, filename)

        file = open(path, "wb+")
        file.write(imgData)
        file.flush()
        file.close()

        # 修改头像分辨率
        im = Image.open(path)
        out = im.resize((100, 100), Image.ANTIALIAS)
        out.save(path)

        # 选择上传头像到七牛还是本地
        try:
            # 上传头像到七牛
            import qiniu

            qiniu_access_key = settings.QINIU_ACCESS_KEY
            qiniu_secret_key = settings.QINIU_SECRET_KEY
            qiniu_bucket_name = settings.QINIU_BUCKET_NAME

            assert qiniu_access_key and qiniu_secret_key and qiniu_bucket_name
            q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)

            key = filename
            localfile = path

            mime_type = "text/plain"
            params = {'x:a': 'a'}

            token = q.upload_token(qiniu_bucket_name, key)
            ret, info = qiniu.put_file(token, key, localfile,
                                       mime_type=mime_type, check_crc=True)

            # 图片连接加上 v?时间  是因为七牛云缓存，图片不能很快的更新，
            # 用filename?v201504261312的形式来获取最新的图片
            request.user.img = "http://{}/{}?v{}".format(
                settings.QINIU_URL,
                filename,
                time.strftime('%Y%m%d%H%M%S')
            )
            request.user.save()

            # 验证上传是否错误
            if ret['key'] != key or ret['hash'] != qiniu.etag(localfile):
                logger.error(
                    u'[UserControl]上传头像错误：[{}]'.format(
                        request.user.username
                    )
                )
                return HttpResponse(u"上传头像错误", status=500)

            return HttpResponse(u"上传头像成功!\n(注意有10分钟缓存)")

        except Exception as e:
            request.user.img = "/static/tx/"+filename
            request.user.save()

            # 验证上传是否错误
            if not os.path.exists(path):
                logger.error(
                    u'[UserControl]用户上传头像出错:[{}]'.format(
                        request.user.username
                    )
                )
                return HttpResponse(u"上传头像错误", status=500)

            return HttpResponse(u"上传头像成功!\n(注意有10分钟缓存)")

    def notification(self, request):
        if not request.user.is_authenticated():
            logger.error(u'[UserControl]用户未登陆')
            raise PermissionDenied

        notification_id = self.request.POST.get("notification_id", "")
        notification_id = int(notification_id)

        notification = Notification.objects.filter(
            pk=notification_id
        ).first()

        if notification:
            notification.is_read = True
            notification.save()
            mydict = {"url": notification.url}
            print(mydict)
        else:
            mydict = {"url": '#'}

        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )

#为了发送带图片在正文邮件
def sendEmail_MIMEMultipart(title,message,from_email,to_email,file_name,):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    HOST = settings.EMAIL_HOST
    PORT = settings.EMAIL_PORT
    USER = settings.EMAIL_HOST_USER
    PWD  = settings.EMAIL_HOST_PASSWORD
    #图片处理为html
    fp = open(file_name,'rb')
    attach = MIMEImage(fp.read())
    fp.close()
    attach.add_header('Content-ID',USER)
    msg = MIMEMultipart('related')
    msgtext1 = MIMEText("%s<img src=\"cid:%s\" border=\"1\"><br>" %(message,USER),"html","utf-8")
    msg.attach(msgtext1)
    msg.attach(attach)
    #图片为附件
    attach = MIMEText(open(file_name,"rb").read(),"base64","utf8")
    attach["Content-Type"] = "application/octet-stream"
    attach["Content-Disposition"] = "attachment; filename=\"%s.png\"" %USER
    msg.attach(attach)
    msg['Subject'] = title
    msg['From'] = from_email
    try:
        server = smtplib.SMTP()
        server.connect(HOST,str(PORT))
        server.login(USER,PWD)
        for email in to_email:
            msg['to'] = str(email)
            server.sendmail(USER,str(email),msg.as_string())
        server.quit()
        return "邮件成功发送!!"
    except Exception,e:
        return "邮件发送失败:" + str(e)
