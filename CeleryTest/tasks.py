#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: tasks.py
# Desc:
# Author: chenhui.shang
# Email: chenhui.shang@woqutech.com
# HomePage: www.woqutech.com
# Version: 0.0.1
# LastChange:  2020/2/21 下午2:26
# History:
#=============================================================================
"""
import datetime
from celery import Celery

celery_app = Celery()


def func_a():
    print(datetime.datetime.now())


task_func_a = celery_app.task(func_a, name="hello world")

task_func_a.delay()
