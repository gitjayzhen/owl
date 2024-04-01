# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: demo_jieba.py
@time: 2024/3/29 10:51
"""

import jieba
import pandas as pd

if __name__ == '__main__':

    # 原句
    sentence = "我昨天去了超市，买了很多东西，然后又去了图书馆还借了几本书回家看。"

    # 使用 jieba 分词
    words = jieba.cut(sentence, cut_all=False)

    stopWords = pd.read_csv("/Users/jayzhen/Downloads/百度停用词表.txt", sep='hahaha')
    stopWords = ['\n', '还'] + list(stopWords.iloc[:, 0])
    processed_words = [i for i in words if i not in stopWords]

    # 去除冗词赘述并重组结构
    # processed_words = [word for word in words if "昨天" not in word]

    # 提炼关键信息
    # key_info = ["购物" if "超市" in word else "阅读" for word in processed_words]

    # 组合精简后的句子
    simple_sentence = "".join(processed_words)

    print(simple_sentence)
