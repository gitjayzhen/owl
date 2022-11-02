#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author: jayzhen
@message: jayzhen_testing@163.com
@site: https://github.com/gitjayzhen
@software: PyCharm & Python 2.7
@file: ImageGenerate.py 
@time: 2018/06/22 17:08 
"""
from PIL import Image, ImageDraw, ImageFont
import os


def gen_image(text, file_path):
    # 创建一个新的图片对象
    i = Image.new("RGB", (1900, 1080), (255, 255, 255))
    # 把这个底片先画出来
    dr = ImageDraw.Draw(i)
    # 为我们即将在这个底片上画东西调好颜料
    font = ImageFont.truetype(os.path.join("fonts", "simsun.ttc"), 18)
    # 开始下笔，用调好的颜料画给定的内容
    dr.text((30, 30), text, font=font, fill="#000000")
    # 画好了，展示一下
    i.show()
    # 记得保存
    i.save(file_path, "JPEG")


def gen_image_2(text, file_path):
    pass