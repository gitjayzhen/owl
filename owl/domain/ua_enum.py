# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: ua_enum.py
@time: 2023/9/6 15:53
"""
from enum import Enum, unique

from owl.exception import EnumDirectValueMeta


@unique
class UserAgent(Enum, metaclass=EnumDirectValueMeta):

    chrome_browser = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/67.0.3396.87 Safari/537.36 "

    iphone_browser = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) " \
                     "Version/11.0 Mobile/15A372 Safari/604.1 "

    ipad_browser = "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) " \
                   "Version/11.0 Mobile/15A5341f Safari/604.1 "

    android_5_browser = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, " \
                        "like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36 "

    android_8_browser = "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, " \
                        "like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36"
