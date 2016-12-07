#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

from django import template
from django.utils.safestring import mark_safe
from django.template.base import Node, TemplateSyntaxError

# 这个是不可变的,必须要写
register = template.Library()

@register.simple_tag
def f2(s1, s2, s3):
    return s1 + s2 + s3

@register.filter
def f3(value):
    if value == 'vvv':
        return True
    return False