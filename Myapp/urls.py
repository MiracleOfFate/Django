from django.urls import path,re_path
from Myapp.views import *

urlpatterns = [
    path('welcome/',welcome),
    path('index/',index),

    path('basic/',basic),
    path('home/',home),

    # Django2. 0中可以使用 re_path() 方法来兼容 1.x 版本中的 url() 方法，一些正则表达式的规则也可以通过 re_path() 来实现 
    # 正则：获取url中的这俩个变量
    re_path(r'^child/(?P<eid>.+)/(?P<oid>.*)/$',child),
]