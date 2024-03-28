# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: test_wordcloud.py
@time: 2023/12/21 13:10
"""

import jieba
import matplotlib.pyplot as plt
import numpy as np
import wordcloud
from PIL import Image
from wordcloud import WordCloud


def w1():
    # 读取文本
    with open("worker-need.txt", encoding="utf-8") as f:
        s = f.read()
    print(s)
    ls = jieba.lcut(s)  # 生成分词列表
    text = ' '.join(ls)  # 连接成字符串

    stopwords = {"的", "是", "了", "和", "或", "等", "及", "相关",
                 "负责", "职责", "其他", "熟悉", "任职", "与",
                 "并", "工作", "能", "项目", "质量", "设计", "问题",
                 "C", "同事", "合作", "产品", "以上学历", "参与", "测试",
                 "以及", "具有"
                 }  # 去掉不需要显示的词

    wc = wordcloud.WordCloud(font_path="/System/Library/Fonts/PingFang.ttc",
                             width=1000,
                             height=700,
                             background_color='white',
                             max_words=100,
                             stopwords=stopwords)
    # msyh.ttc电脑本地字体，写可以写成绝对路径
    wc.generate(text)  # 加载词云文本
    wc.to_file("worker-need.png")  # 保存词云文件


def w2():
    # 打开文本
    with open("lhy_comments.txt", encoding="utf-8") as f:
        s = f.read()

    # 中文分词
    text = ' '.join(jieba.cut(s))

    # 生成对象
    img = Image.open("mask_pic.png")  # 打开遮罩图片
    mask = np.array(img)  # 将图片转换为数组

    stopwords = ["我", "你", "她", "的", "是", "了", "在", "也", "和", "就", "都", "这"]
    wc = WordCloud(font_path="msyh.ttc",
                   mask=mask,
                   width=1000,
                   height=700,
                   background_color='white',
                   max_words=200,
                   stopwords=stopwords).generate(text)

    # 显示词云
    plt.imshow(wc, interpolation='bilinear')  # 用plt显示图片
    plt.axis("off")  # 不显示坐标轴
    plt.show()  # 显示图片

    # 保存到文件
    wc.to_file("李焕英2.png")


if __name__ == '__main__':
    w1()
