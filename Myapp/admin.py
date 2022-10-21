from django.contrib import admin

from Myapp.models import BookInfo, PeopleInfo

# Register your models here.
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)