from unicodedata import name
from django.db import models

'''
    Django数据模型中自带主键[id]，且主键自动递增。所以我们在写模型类时，不需要管主键
'''
# Create your models here.
# 准备书籍列表信息的模型类---对应一个数据表
class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=10)
    """返回一个对象的描述信息---字符串"""
    def __str__(self):
        return self.name

# 准备人物列表信息的模型类---对应一个数据表
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE) # 外键约束：人物属于哪本书；删除关联数据,与之关联也删除
