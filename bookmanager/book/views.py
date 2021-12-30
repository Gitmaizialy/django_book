from django.shortcuts import render

# Create your views here.
"""
1. 接收请求request 即HttpRequest的类对象
2. 返回的响应HttpResponse
"""

from django.http import HttpRequest, HttpResponse

# 定义http://localhost:8000/index/ 访问函数
def index(request):
    return HttpResponse('ok')
