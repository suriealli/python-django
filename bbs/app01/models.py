from django.db import models
#from django.core.serializers.python import Model
from django.contrib.auth.models import User
# Create your models here.

class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count =  models.IntegerField()
    ranking = models.ImageField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 32,unique=True)
    admin = models.ForeignKey('BBS_user')

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='111')
    photo = models.ImageField(upload_to="up_photo",default="up_photo/default.jpg")
    def __unicode__(self):
        return self.user
