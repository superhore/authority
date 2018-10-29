from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index_views(request):

    if request.user.is_authenticated:
        # Do something for authenticated users.认证过的用户如何处理
        return HttpResponse("你好")
    else:
        return HttpResponse('hello')

def index(request):
    common_dict={
    "sitename":"我的网站测试中。。。",
    "sitedomain":"127.0.0.1",
    'app_label':'',
    }
    content='fffffffff'
    username='amouysuser'
    if request.user.is_authenticated:
        username = request.session.get('username', None)
        content=' 认证的用户'
    else:
        content='  匿名用户'
    return HttpResponse(content)