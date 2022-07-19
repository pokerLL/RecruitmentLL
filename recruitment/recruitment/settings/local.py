from recruitment.settings.base import *

ALLOWED_HOSTS = ["*"]

DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=8fdfb07566eb88cf9a162fed379b4d54ea1678f09fe274d34e6a4ea7f65312c4"

# INSTALLED_APPS = INSTALLED_APPS + ['django_celery_results', ]

# Celery Configuration Options
CELERY_BORKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKNED = "redis://localhost:6379/1"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Shanghai"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
