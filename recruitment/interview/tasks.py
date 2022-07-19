from celery import shared_task 
from utils.dingtalk import send_message

@shared_task
def send_dingtalk_message(message):
    send_message(message)