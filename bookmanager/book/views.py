from django.shortcuts import render

# Create your views here.
"""
1. 接收请求request 即HttpRequest的类对象
2. 返回的响应HttpResponse
"""

from django.http import HttpRequest, HttpResponse


# 定义http://localhost:8000/index/ 访问函数
def index(request):
    # return HttpResponse('ok')

    # 视图返回渲染的模板
    # render            渲染模板
    # request,          请求
    # template_name,    模板名字
    # context=None,     上下文 将视图views中的数据传递给html模板   模板html采用{{key值}}方式接收views中的值
    # 模拟数据库数据
    context_value = {
        'name': '这是模拟数据库里的数据value值'
    }

    # 在此处实现增删改查的操作

    return render(request, 'book/templatesindex.html', context=context_value)


"""
基于orm进行的数据库操作
在python manage.py shell中 实现数据的增删改查的操作
"""
from book.models import BookInfo

###### 查询数据 ######
# 方式一
# all查询多个结果
books = BookInfo.objects.all()
books
# get查询单一结果， 如果不存在则抛出DoesNitExist异常
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询数据不存在')
book
# count查询数量
BookInfo.objects.all().count()
BookInfo.objects.count()

# 方式二 过滤查询
# 例：模型类名.objects.filter(属性名_运算符=值)
# 例：模型类名.objects.get(属性名_运算符=值)
# 例：模型类名.objects.exclude(属性名_运算符=值)
# filter 过滤出多个结果
# get 过滤单一结果
# exclude 条件排除返回多个结果

# 查询编号为1的图书
book = BookInfo.objects.get(pk=1)  # pk 主键值
book = BookInfo.objects.get(id=1)  # 简写形式 （属性名=值）
book = BookInfo.objects.get(id_exact=1)  # 完整形式 （属性名_运算符=值）
# 查询书名包含 湖 的图书
books = BookInfo.objects.filter(name__contains='湖')
# 查询书名以 部 结尾的图书
books = BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
books = BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
books = BookInfo.objects.filter(id__in=[1, 3, 5])
# 查询编号大于3的图书 大于：gt  大于等于：gte  小于：lt  小于等于：lte
books = BookInfo.objects.filter(id__gt=3)
# 查询编号不等于3的图书
books = BookInfo.objects.exclude(id=3)
# 查询1980年发表的图书
books = BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
books = BookInfo.objects.filter(pub_date__gt='1990-1-1')

###### 增加数据 ######
# 方式一
book = BookInfo(
    name='django',
    pub_date='2000-1-1',
    readcount=10
)
# 在python manage.py shell中执行时，需调用save方法实现数据保存到数据库
book.save()

# 方式二
# objects 相当于代理 实现增删改查
BookInfo.objects.create(
    name='django1',
    pub_date='2000-1-1',
    readcount=100
)

###### 修改数据 ######
# 方式一
book = BookInfo.objects.get(id=2)
book.name = '修改后的名称'
book.save()

# 方式二
# filter 过滤
BookInfo.objects.filter(id=2).update(name='再次修改的名称', commentcount=666)

###### 删除数据 ######
# 物理删除（一条数据的删除）
# 方式一
book = BookInfo.objects.get(id=6)
book.delete()
# 方式二
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=6).delete()

# 逻辑删除（修改标记位 例如 is_delete=False）
