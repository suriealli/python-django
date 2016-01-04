from django.contrib import admin
from app01 import models
# Register your models here.
admin.site.register(models.BBS)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
