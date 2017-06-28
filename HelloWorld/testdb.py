# -*- coding: utf-8 -*-
# __author__ = 'libingxin'


from django.http import HttpResponse
from TestModel.models import Mysql


# 数据库操作
def testdb(request):
    # sample1
    # test1 = mysql(name='runoob1')
    # test1.save()
    # test2 = mysql(name='melody1')
    # test2.save()
    # return HttpResponse("<p>数据添加成功！</p>")

    # sample2

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    # list = mysql.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = mysql.objects.filter(id=1)

    # 获取单个对象
    # response3 = mysql.objects.get(id=2)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # mysql.objects.order_by('name')[0:2]

    #数据排序
    # mysql.objects.order_by("id")

    # 上面的方法可以连锁使用
    # mysql.objects.filter(name="runoob").order_by("id")

    # sample3
    # test1 = mysql.objects.get(id=1)
    # test1.name = 'Google'
    # test1.save()
    # return HttpResponse("<p>update successfully !</p>")

    # 初始化
    response = ""
    response1 = ""

    #输出所有数据
    list = Mysql.objects.all()
    for var in list:
        response1 += var.name + "##### "
    response = response1
    message = "<p>" + response + "</p>"
    return HttpResponse(message)

    # 删除所有数据
    # mysql.objects.all().delete()
    # message_del = '删除成功!'
    # return HttpResponse(message_del)
