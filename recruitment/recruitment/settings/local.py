from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
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


sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)
