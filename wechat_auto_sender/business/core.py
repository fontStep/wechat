# -*- coding: utf-8 -*-
import pyautogui
import time
import os
import pyperclip
from pywinauto.application import Application
from wechat_auto_sender.config.config import WECHAT_PATH
from wechat_auto_sender.adapters.explorer import copy_file_by_explorer
from wechat_auto_sender.utils.misc import (
    retry_on_failure, print_cli_error, print_cli_info,
    WeChatSenderError, WeChatSenderRetryError
)
from wechat_auto_sender.utils.logger import LoggerHelper
import logging

class WeChatAutoSender:
    def __init__(self, log_file='wechat_sender.log', log_level=logging.INFO):
        self.logger = LoggerHelper.get_logger(log_file, log_level)
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1

    @retry_on_failure()
    def open_wechat(self):
        try:
            if not os.path.exists(WECHAT_PATH):
                raise WeChatSenderError(f"微信程序未找到: {WECHAT_PATH}")
            os.startfile(WECHAT_PATH)
            time.sleep(3)
            self.logger.info("微信已启动")
            print_cli_info("微信已启动")
            return True
        except Exception as e:
            self.logger.error(f"启动微信失败: {str(e)}")
            print_cli_error(f"启动微信失败: {str(e)}")
            raise WeChatSenderError(e)

    def activate_wechat(self):
        try:
            app = Application(backend="uia").connect(path=WECHAT_PATH)
            main_win = app.window(class_name="WeChatMainWndForPC")
            main_win.set_focus()
            self.logger.info("已激活微信窗口")
            print_cli_info("已激活微信窗口")
            return True
        except Exception as e:
            self.logger.error(f"激活微信窗口失败: {e}")
            print_cli_error(f"激活微信窗口失败: {e}")
            raise WeChatSenderError(e)

    @retry_on_failure()
    def search_contact(self, contact_name):
        try:
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(0.3)
            pyperclip.copy(contact_name)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.3)
            pyautogui.press('down')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.5)
            self.logger.info(f"已搜索联系人: {contact_name}")
            print_cli_info(f"已搜索联系人: {contact_name}")
            return True
        except Exception as e:
            self.logger.error(f"搜索联系人失败: {str(e)}")
            print_cli_error(f"搜索联系人失败: {str(e)}")
            raise WeChatSenderRetryError(e)

    @retry_on_failure()
    def send_message(self, contact_name, message):
        try:
            self.open_wechat()
            if not self.search_contact(contact_name):
                raise WeChatSenderError(f"未找到联系人: {contact_name}")
            pyperclip.copy(message)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            self.logger.info(f"消息已发送给 {contact_name}")
            print_cli_info(f"消息已发送给 {contact_name}")
            return True
        except Exception as e:
            self.logger.error(f"发送消息失败: {str(e)}")
            print_cli_error(f"发送消息失败: {str(e)}")
            raise WeChatSenderRetryError(e)

    @retry_on_failure()
    def send_file(self, contact_name, file_path):
        try:
            if not self.search_contact(contact_name):
                raise WeChatSenderError(f"未找到联系人: {contact_name}")
            copy_file_by_explorer(file_path=file_path)
            self.activate_wechat()
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.2)
            self.logger.info(f"文件已发送给 {contact_name},文件名称：{file_path}")
            print_cli_info(f"文件已发送给 {contact_name}, 文件名称：{file_path}")
            return True
        except Exception as e:
            self.logger.error(f"发送文件失败: {str(e)}")
            print_cli_error(f"发送文件失败: {str(e)}")
            raise WeChatSenderRetryError(e) 