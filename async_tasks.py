# -*- coding: utf-8 -*-
from celery import Celery
from database import Logs
app = Celery()
app.config_from_object("celeryconfig")


@app.task
def add(x, y):
    return x + y


@app.task(name="jinjia2.add_log")
def add_log(remark=None):
    Logs.add(remark)



