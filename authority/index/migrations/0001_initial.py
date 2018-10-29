# Generated by Django 2.1.2 on 2018-10-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uphone', models.CharField(max_length=11, verbose_name='手机号')),
                ('upwd', models.CharField(max_length=32, verbose_name='密码')),
                ('uname', models.CharField(default='匿名', max_length=30, verbose_name='用户名')),
                ('uemail', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
            ],
        ),
    ]
