# -*- coding:utf-8 -*-

""" 
@author: jayzhen
@site: https://github.com/gitjayzhen
@software: PyCharm & Python 2.7
@file: gzip_encrypt.py
@time: 2018/09/03 16:54 
"""

import gzip
from io import StringIO


def gzip_compress(raw_data):
    buf = StringIO()
    f = gzip.GzipFile(mode='wb', fileobj=buf)
    try:
        f.write(raw_data)
    finally:
        f.close()
    return buf.getvalue()


def gzip_uncompress(c_data):
    buf = StringIO(c_data)
    f = gzip.GzipFile(mode='rb', fileobj=buf)
    try:
        r_data = f.read()
    finally:
        f.close()
    return r_data


def compress_file(fn_in, fn_out):
    f_in = open(fn_in, 'rb')
    f_out = gzip.open(fn_out, 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()


def uncompress_file(fn_in, fn_out):
    f_in = gzip.open(fn_in, 'rb')
    f_out = open(fn_out, 'wb')
    file_content = f_in.read()
    f_out.write(file_content)
    f_out.close()
    f_in.close()
