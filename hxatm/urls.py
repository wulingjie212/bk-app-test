# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('hxatm.views',
    (r'^index.html$', 'index'),
    (r'^detail.html$', 'detail'),
    (r'^tab.html$', 'tab'),
)
