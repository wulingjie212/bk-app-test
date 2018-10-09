# -*- coding: utf-8 -*-
from common.mymako import render_mako_context
from django.http import HttpResponse

def index(request):
    """
    首页
    """
    return render_mako_context(request, '/hxatm/index.html')


def detail(request):
    """
    开发指引
    """
    return render_mako_context(request, '/hxatm/detail.html')


def tab(request):
    """
    联系我们
    """
    return render_mako_context(request, '/hxatm/tab.html')
