import os

# 微信相关配置
WECHAT_PATH = os.environ.get('WECHAT_PATH', r"D:\Program Files\Tencent\WeChat\WeChat.exe")

# 重试配置
RETRY_CONFIG = {
    "max_retries": int(os.environ.get('WECHAT_RETRY', 3)),
    "delay": int(os.environ.get('WECHAT_RETRY_DELAY', 1))
} 