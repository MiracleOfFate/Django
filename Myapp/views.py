from django import http
from django.shortcuts import render

# Create your views here.
def index(request): # 为了使 django 自动调用，需定义一个参数，以方便传入必要的信息。这里的参数名可任意取，但为了可理解，一般取request
    # pass  # 占位，是一个标记，为了保证完整性，构造了一个不做任何事情的主体，可将来再实现其函数体
    '''
        定义了一个视图（在页面上显示“OK”）
        :param request
        :
    '''
    return http.HttpResponse("OK")
