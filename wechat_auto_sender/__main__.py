import os
import argparse
from wechat_auto_sender.business.core import WeChatAutoSender

def main():
    parser = argparse.ArgumentParser(description='微信自动发送工具')
    parser.add_argument('--contact', required=True, help='联系人名称')
    parser.add_argument('--message', help='要发送的文本消息')
    parser.add_argument('--file', help='要发送的文件路径')
    args = parser.parse_args()

    sender = WeChatAutoSender()
    if args.message:
        sender.send_message(args.contact, args.message)
    if args.file:
        sender.send_file(args.contact, args.file)

if __name__ == '__main__':
    main() 