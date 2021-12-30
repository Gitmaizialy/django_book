#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: maizi-pc
@time: 2021/12/30
@func: 
"""

from django.urls import path
from book.views import index

# 固定写法 urlpatterns[]
urlpatterns = [
    # path(路由, 视图函数名)
    path('index/', index)
]
