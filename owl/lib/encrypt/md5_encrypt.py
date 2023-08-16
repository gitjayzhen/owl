# -*- coding:utf-8 -*-

import hashlib
import os
import datetime
import sys
import struct
import binascii

# python 检测文件MD5值

"""
1.bin(数字)十进制-》二进制，有0b，用replace('0b','')
2.int(浮点型数字) float-》int
3.chr(数字a)a在0~255之间。int-》ascii码（即只有8位）
4.ard(字符a)ascii码-》int。3的反向
5.hex(数字a)十进制-》十六进制
6.binascii.b2a_hex(字符串)字符串-》十六进制
7.binascii.a2b_hex(十六进制数)十六进制-》字符串。6的反向
"""


def get_str_md5(src):
    """
    简单的测试一个字符串的MD5值
    :param src:
    :return:
    """
    m0 = hashlib.md5()
    m0.update(src.encode("utf8"))
    print(m0.digest())
    print(m0.digest_size)
    a = ""
    for i in m0.digest():
        # print hex(bytes(i).decode('ascii') & 0xFF)
        print(struct.unpack('<h', bytes("\xFF" + i)))
        # a += binascii.b2a_hex(i.decode(encoding='utf-8', errors='strict'))
        b = binascii.b2a_hex(i)
        # print int(b) & 0xFF
        if len(b) == 1:
            a += "0"
        a += b
    print(a)
    print(m0.hexdigest())
    print(m0.hexdigest().upper())
    print(type(m0.hexdigest()))


def get_file_md5(filename):
    """
    大文件的MD5值
    :param filename:
    :return:
    """
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def calc_sha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
        return hash


def calc_md5(filepath):
    with open(filepath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        print(hash)
        return hash


# filepath = raw_input('请输入文件路径：')
#
# # 输出文件的md5值以及记录运行时间
# starttime = datetime.datetime.now()
# print GetFileMd5(filepath)
# endtime = datetime.datetime.now()
# print '运行时间：%ds'%((endtime-starttime).seconds)


if __name__ == "__main__":
    # if len(sys.argv) == 2:
    #     hashfile = sys.argv[1]
    #     if not os.path.exists(hashfile):
    #         hashfile = os.path.join(os.path.dirname(__file__), hashfile)
    #         if not os.path.exists(hashfile):
    #             print("cannot found file")
    #         else:
    #             CalcMD5(hashfile)
    #     else:
    #         CalcMD5(hashfile)
    #         # raw_input("pause")
    # else:
    #     print("no filename")

    get_str_md5("7455302211407071221")
