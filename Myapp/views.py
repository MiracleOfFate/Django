# 前端返回用的python包
from django import http
from django.shortcuts import render

# Create your views here.
def welcome(request): # 为了使 django 自动调用，必须定义一个参数，以方便传入必要的信息。这里的参数名可任意取，但为了可理解，一般取request（这个参数是必须存在的，只要是urls.py中映射的函数，必须有。它里面包含了所有这次请求的东西，比如请求者的ip，登陆的用户名，http请求等等，都会包含在此）
    # pass  # 占位，是一个标记，为了保证完整性，构造了一个不做任何事情的主体，可将来再实现其函数体
    '''
        定义了一个视图（在页面上显示“欢迎来到主页”）
        :param request
        :
    '''
    return http.HttpResponse("欢迎来到主页") # 返回一个ok字符串的html页面（即给浏览器返回ok）
