# -*- coding: utf-8 -*-

import ctypes
import logging
import os.path
import platform
import re
import subprocess
import time
from datetime import datetime, timedelta

import requests


def setup_logging():
    # 创建logger对象
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # 创建文件处理器，将日志写入到文件中
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), 'get_reservation_info.log'))
    file_handler.setLevel(logging.DEBUG)

    # 创建控制台处理器，将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 定义日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到logger对象中
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 设置日志对象
logger = setup_logging()


def show_message_box(message):
    system = platform.system()
    if system == 'Windows':
        user_choice = ctypes.windll.user32.MessageBoxW(None, message, "提示", 1)
    elif system == 'Darwin':
        user_choice = subprocess.call(['osascript', '-e',
                                       'tell app "System Events" to display dialog "' + message + '" buttons {"确定", "取消"} default button "确定"'])
    elif system == 'Linux':
        user_choice = subprocess.call(['zenity', '--question', '--text', message])
    else:
        raise NotImplementedError("不支持的操作系统")

    if system != 'Linux' and user_choice == 1:
        logger.info("用户点击了取消按钮")
    elif system != 'Linux' and user_choice != 0:
        logger.info("用户关闭了提示框")
    else:
        logger.info("用户点击了确定按钮")


def get_info(glb="01020000", dt="2023-08-23"):
    header = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "cookie": "JSESSIONID_MOBILEAPP=z1UV6hyNPeR_B6hQM_T-UiFsa7ZtbzBTIPTD9IbHXS49Kg49mJHA!940968835; weixin-app-7003=BLSQDgMCEqwtYz9oBTgwMA$$",
        "Referer": "https://wx.csgjj.com.cn/mobileApp/weixin/loanBusAppointments.jsp",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    body = "jgdm={}&yydate={}&method=local.user.getTimeperiod&v=1.0&appkey=f8fer24f8797646b9a26" \
           "&timestamp={}&sign=ba8bc0a47a70a68a0a60067a258b96041430a4d2".format(glb, dt, int(time.time() * 1000))
    logger.info(body)
    resp = requests.post("https://wx.csgjj.com.cn/mobileApp/api/getwaynews.do",
                         headers=header, data=body)
    resp_data = resp.json()
    # print(json.dumps(resp_data, indent=4, ensure_ascii=False))
    logger.info(resp_data)
    for tmp in resp_data['timeperiod']:
        # 定义匹配模式
        pattern = re.compile("剩余：(\d+)")
        # 使用正则表达式进行匹配
        match = re.search(pattern, tmp['name'])
        if match and int(match.group(1)) > 0:
            # remaining = match.group(1)
            return "{}({}) - {} - {}({})".format(resp_data['jgdz'][0:6], glb, dt, tmp['name'], tmp['id'])
        else:
            return None


if __name__ == '__main__':
    while True:
        try:
            today = datetime.today()
            day_diff = (4 - today.weekday()) % 7  # 计算到本周五的天数差
            friday = today + timedelta(days=day_diff)
            logger.info("本周五日期是：" + friday.strftime("%Y-%m-%d"))  # 格式化输出本周五的日期
            # 获取今天的日期
            today = datetime.now().date()
            # 设置目标日期
            target_date = friday.date()
            # 循环迭代，生成日期列表
            current_date = today if today == target_date else today + timedelta(days=1)
            for b in ["01020000", "01030000", "01040000", "01050000", "01060000"]:
                logger.info("当前区代号：" + b)
                while current_date <= target_date:
                    logger.info(b + ", " + current_date.strftime("%Y-%m-%d"))
                    message = get_info(b, current_date.strftime("%Y-%m-%d"))
                    if message is not None:
                        show_message_box(message)
                    current_date += timedelta(days=1)
                current_date = today if today == target_date else today + timedelta(days=1)
                time.sleep(3)
        except Exception as e:
            logger.info(e)
        # 每半小时执行一次 1800s 900s=15分钟 600=10分钟
        time.sleep(600)
