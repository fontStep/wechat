import sys
import time
from wechat_auto_sender.config.config import RETRY_CONFIG
from functools import wraps

class WeChatSenderError(Exception):
    """致命错误"""
    pass

class WeChatSenderRetryError(Exception):
    """可重试错误"""
    pass

def print_cli_error(msg):
    print(f'\033[91m[错误] {msg}\033[0m', file=sys.stderr)

def print_cli_info(msg):
    print(f'\033[92m[提示] {msg}\033[0m')

def retry_on_failure(max_retries=RETRY_CONFIG["max_retries"], delay=RETRY_CONFIG["delay"]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except WeChatSenderError as e:
                    print_cli_error(str(e))
                    raise
                except Exception as e:
                    if attempt == max_retries - 1:
                        print_cli_error(f"重试{max_retries}次后失败: {e}")
                        raise WeChatSenderRetryError(e)
                    print_cli_info(f"发生异常: {e}，{delay}秒后重试({attempt+1}/{max_retries})...")
                    time.sleep(delay)
            return False
        return wrapper
    return decorator 