#coding=utf8
from django.db import models
#from django.core.serializers.python import Model
from django.contrib.auth.models import User
from collections import OrderedDict
from django.core.urlresolvers import reverse

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='This guy is too lazy to writing something')
    photo = models.ImageField(upload_to="up_photo",default="up_photo/default.jpg")
    email = models.EmailField(blank=True,max_length=256)
    website = models.URLField(blank=True,max_length=256)
    def __unicode__(self):
         return self.user.username

class TagManager(models.Manager):#自定义管理器
    def get_Tag_list(self):#返回文章标签列表，每个标签以及对应的文章数目
         tags = Tag.objects.all()#获取所有标签
         tag_list = []
         for i in range(len(tags)):
             tag_list.append([])
         for i in range(len(tags)):
             tmp = Tag.objects.get(name = tags[i])
             posts = tmp.article_set.all()
             tag_list[i].append(tags[i].name)
             tag_list[i].append(len(posts))
         return tag_list

class ClassManager(models.Manager):
    def get_Class_list(self):
         classf = Classification.objects.all()#获取所有分类
         class_list = []
         for i in range(len(classf)):
             class_list.append([])
             tmp = Classification.objects.get(name = classf[i])#获取当前类名
             posts = tmp.article_set.all()#获取当前类下的所有文章
             class_list[i].append(classf[i])
             class_list[i].append(len(post))
         return class_list


class ArticleManager(models.Model):
    def get_Article_onDate(self):#文章按月排档
        post_date = Article.object.dates('created_time','month')
        date_list = []
        for i in range(len(post_date)):
            date_list.append([])
            curyear = post_date[i].year
            curmonth = post_date[i].month
            tmpArticle = Article.objects.filter(created_time__year=curyear).filter(create_time__month=curmonth)
            date_list[i].append(post_date[i])
            date_list[i].append(len(tmpArticle))
            return date_list

class Tag(models.Model):#标签表
    name = models.CharField(max_length=20,blank=True)#标签名
    created_time = models.DateTimeField(auto_now_add=True)#标签创建时间
    object = models.Manager()#默认的管理器?
    tag_list = TagManager()#自定义的管理器?
    
    @models.permalink
    def get_absolute_url(self):
        return ('tagDetail',(),{'tag':self.name})
    def __unicode__(self):
        return self.name

class Classification(models.Model):
    name = models.CharField(max_length=25)
    object = models.Manager()#默认的管理器
    class_list = ClassManager()#自定义的管理器
    def __unicode__(self):
        return self.name

class Article(models.Model):#文章表
    title = models.CharField(max_length=64)#题名
    summary = models.CharField(max_length=256,blank=True,null=True)#概要
    tag = models.ManyToManyField(Tag,blank=True)#标签
    classification = models.ForeignKey('Classification')#分类，外键
    content = models.TextField()#内容
    author = models.ForeignKey('Author')#作者
    view_count =  models.IntegerField()#查看次数，浏览数
    ranking = models.CharField(max_length=100)# 排行
    created_time = models.DateTimeField()#创建时间
    updated_time = models.DateTimeField(auto_now_add=True)#最后更新时间
    
    objects = models.Manager()#默认管理器
    data_list = ArticleManager()#自定义管理器

    @models.permalink
    def get_absolute_url(self):
        return ('detail',(),{
        'year' : self.publish_time.year,
        'month' : self.publish_time.strftime('%m'),
        'day' : self.publish_time.strftime('%d'),
        'id' : self.id})
    def get_tags(self):#获取一个文章的标签
        tag = self.tags.all()
        return tag
    def get_before_article(self):#获取当前文章的前一篇
        tmp = Article.objects.order_by('id')
        cur = Article.objects.get(id=self.id)
        count = 0
        for i in tmp:
            if i.id == cur.id:
                index = count
                break
            else:
                count=count+1
        if index != 0:
            return tmp[index-1]
    def get_after_article(self):#获取下一篇文章
        tmp = Article.objects.order_by('id')
        max = len(tmp) - 1
        cur = Article.objects.get(id=self.id)
        count = 0
        for i in tmp:
            if i.id == cur.id:
                index = count 
                break
            else:
                count = count + 1
        if index != max:
            return tmp[index+1]        

    def __unicode__(self):
        return self.title
    class Meta:#按时间下降顺序排序
        ordering = ['-created_time']
