# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:33:31 2020

@author: 630263
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list")
    ]