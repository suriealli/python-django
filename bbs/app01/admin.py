from django.contrib import admin
from app01 import models
# Register your models here.
admin.site.register(models.Article)
admin.site.register(models.Author)
admin.site.register(models.Tag)
admin.site.register(models.Classification)
