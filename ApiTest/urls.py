"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from Myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Myapp/',include('Myapp.urls')), # 使用路由分发（include），让每个app目录都单独拥有自己的 urls
    # re_path(r'^child/(?P<eid>.+)/(?P<oid>.*)/$',child), # 返回子页面
]
