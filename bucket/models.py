from django.db import models
from django.conf import settings

# Create your models here.
class Download(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="登録ユーザー",on_delete=models.CASCADE)
    url = models.URLField(max_length=200,verbose_name="url")
    finish = models.BooleanField(verbose_name="finish check",default=False)
