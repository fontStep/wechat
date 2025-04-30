import os
import time
import pyautogui

def copy_file_by_explorer(file_path):
    """用pyautogui自动打开资源管理器并复制指定文件"""
    folder, filename = os.path.split(os.path.abspath(file_path))
    os.startfile(folder)
    time.sleep(1.5)
    pyautogui.write(filename)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5) 