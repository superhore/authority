from django.db import models

# Create your models here.

class User(models.Model):
    uphone = models.CharField(max_length=11, verbose_name='手机号')
    upwd = models.CharField(max_length=32, verbose_name='密码')
    uname = models.CharField(max_length=30, default='匿名', verbose_name='用户名')
    uemail = models.EmailField(null=True, verbose_name='邮箱')