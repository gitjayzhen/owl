#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@email: jayzhen_testing@163.com
@software: PyCharm
@file: SuperFormatUtil
@time: 2017/12/12  13:59
"""
import re
import urllib


def sformat(source, param):
    """
    一个String的数据格式为“..{a}..{b}..{c}..”大括号中的参数必须有，且需要格式进去的数据，也必须有这个同名的对象
        1.获取字符串中大括号的待格式化的对象
        2.通过遍历将参数中与其匹配的数据加进去
        3.最后返回完整的字符串
    需要考虑的是class对象、dict、单个变量
    如果是对象，那就dict格式化并进行随后的操作
    如果是dict就直接执行
    如果是单个变量，那就先判断是否等于正则匹配的个数，不等就返回，相等就处理,因为单个匹配就不管是不是占位与参数名相同了
    :param lstring: 需要进行格式化的原对象字符串
    :param param:  供格式的数据源
    :return:  格式化后的完整字符串
    """

    if source is None or source.strip() == "":
        print "lstring 语句不能是空"
        return None
    if param is None:
        print "格式化的参数不能是None"
        return None

    res = re.findall(re.compile('{(.+?)}'), source)
    if res is None or len(res) <= 0:
        print "请检查你的String格式，是否为:'--{a}-{b}--',或者你可以直接只用python内置的方法str.format"
        return None

    res_set = set(res)
    length = len(res_set)

    if isinstance(param, str) or isinstance(param, int):
        if param.strip() == '':
            print "要格式化的内容为空"
        if length == 1:
            strs2 = source.split("{")
            result = []
            for n in range(len(strs2)):
                tmp = strs2[n].split("}")
                if tmp[0] in res_set:
                    tmp[0] = str(param).strip()
                result.extend(tmp)
            return '\''.join(result)
        elif length >= 1:
            print "你的参数个数少于字符串中占位的变量数"
            return None

    if not isinstance(param, dict) and not isinstance(param, str):
        pr = {}
        for name in dir(param):
            value = getattr(param, name)
            if not name.startswith('__') and not callable(value):
                pr[name] = value
        param = pr

    strs3 = source.split("{")
    result = []
    try:
        for n in range(len(strs3)):
            l = strs3[n].split("}")
            if l[0] in res_set:
                l[0] = str(param[l[0]])
            result.extend(l)
        return '\''.join(result)
    except KeyError, e:
        print "你的参数与原数据中的占位参数对应不上：(str='--{a}--', b=1) 应是 a=a, 不是 a=b"
        return None


def oct2chr(oct_str):
    """将一个十六进制的字符串转化为正常的字符串："""
    body = oct_str
    s = 0
    bin_data = ""
    while s < len(body):
        pri = body[s:s+2]
        if pri == r'\x':
            s += 2
            bins = body[s:s+2]
            b = chr(int(('0x' + bins), 16))
            bin_data += b
            s += 2
        else:
            b = chr(int(hex(ord(body[s])), 16))
            bin_data += b
            s += 1
    return bin_data


def string_lines_to_dict(strs):
    '''
    将一个多行的String内容转化为dict或是json格式，场景是我们对接口中header进行快速修改时需要加各种引号什么的，费时
    :param strs:
    :return:
    '''
    if strs is None or strs.strip() == "":
        return None
    str_dict = {}
    for i in strs.split("\n"):
        i = i.strip()
        if i is not None and i != "":
            str_list = i.split(":", 1)
            length = len(str_list)
            if length > 2:
                str_dict[str_list[0]] = ":".join(str_list[1:])
            elif length == 2:
                str_dict[str_list[0]] = str_list[1].strip()
            else:
                print "data is data, cant be dict"
                return None
    print str_dict


def string_to_dict(line_str):
    '''
    这个主要是处理接口中的post方式的body数据
    :param line_str:
    :return:
    '''
    if line_str is None or line_str.strip() == "":
        return None
    tmp = line_str.split('?', 1)
    if len(tmp) > 1:
        line_str = tmp[1]
    str_dict = {}
    for i in line_str.split("&"):
        i = i.strip()
        if i is not None and i != "":
            str_list = i.split("=")
            # 使用urllib.unquote()对ascll的url参数进行解码
            # （url的编码格式采用的是ASCII码，而不是Unicode，这也就是说你不能在Url中包含任何非ASCII字符，
            # 例如中文。否则如果客户端浏览器和服务端浏览器支持的字符集不同的情况下，中文可能会造成问题。）
            try:
                str_dict[str_list[0]] = urllib.unquote(str_list[1].strip())
            except IndexError, e:
                print "Confirm your data"
                return None
    print str_dict

