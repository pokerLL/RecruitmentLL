# pip install -U Celery
# pip install -U "celery[redis]"
# tasks.py
from celery import Celery

# 第一个参数 是当前脚本的名称，第二个参数是运行结果存储的位置 第三个位置消息队列的地址
app = Celery('tasks', backend='redis://localhost:6379/1', broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y