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

    return render(request, 'book/templatesindex.html', context=context_value)
