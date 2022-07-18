from django.conf import settings
from dingtalkchatbot.chatbot import DingtalkChatbot

# 引用 settings里面配置的钉钉群消息通知的WebHook地址
# 初始化机器人小丁, # 方式一：通常初始化方式
xiaoding = DingtalkChatbot(settings.DINGTALK_WEB_HOOK)

# 方式二：勾选“加签”选项时使用（v1.5以上新功能）
# xiaoding = DingtalkChatbot(webhook, secret=secret)
def send_message(message,at_mobiles=[]):
    xiaoding.send_text(msg=('测试：%s'%message),at_mobiles=at_mobiles)