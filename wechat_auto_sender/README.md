# WeChat Auto Sender 工程化版

## 功能简介
- 自动激活微信窗口，支持自动发送文本和文件。
- 支持命令行调用。

## 目录结构
```
wechat_auto_sender/
    __init__.py
    core.py
    __main__.py
config.py
requirements.txt
README.md
```

## 安装依赖
```bash
pip install -r requirements.txt
```

## 使用方法
### 命令行方式
发送文本：
```bash
python -m wechat_auto_sender --contact "联系人" --message "你好，测试消息"
```
发送文件：
```bash
python -m wechat_auto_sender --contact "联系人" --file "文件路径"
```
两者都发：
```bash
python -m wechat_auto_sender --contact "联系人" --message "你好" --file "文件路径"
```

## 注意事项
- 需保证微信已登录。
- explorer自动复制文件需桌面前台操作。
