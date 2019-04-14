# coding=gbk

import hashlib
import os
import datetime
import sys
import struct
import binascii
# python ����ļ�MD5ֵ
# python version 2.6
"""
1.bin(����)ʮ����-�������ƣ���0b����replace('0b','')
2.int(����������) float-��int
3.chr(����a)a��0~255֮�䡣int-��ascii�루��ֻ��8λ��
4.ard(�ַ�a)ascii��-��int��3�ķ���
5.hex(����a)ʮ����-��ʮ������
6.binascii.b2a_hex(�ַ���)�ַ���-��ʮ������
7.binascii.a2b_hex(ʮ��������)ʮ������-���ַ�����6�ķ���
"""


def get_str_md5(src):
    """
    �򵥵Ĳ���һ���ַ�����MD5ֵ
    :param src:
    :return:
    """
    m0 = hashlib.md5()
    m0.update(src.encode("utf8"))
    print m0.digest()
    print m0.digest_size
    a = ""
    for i in m0.digest():
        # print hex(bytes(i).decode('ascii') & 0xFF)
        print struct.unpack('<h', bytes("\xFF"+i))
        # a += binascii.b2a_hex(i.decode(encoding='utf-8', errors='strict'))
        b = binascii.b2a_hex(i)
        # print int(b) & 0xFF
        if len(b) == 1:
            print "1111111111"
            a += "0"
        a += b
    print a
    print m0.hexdigest()
    print m0.hexdigest().upper()
    print type(m0.hexdigest())


def get_file_md5(filename):
    """
    ���ļ���MD5ֵ
    :param filename:
    :return:
    """
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename, 'rb')
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


# filepath = raw_input('�������ļ�·����')
#
# # ����ļ���md5ֵ�Լ���¼����ʱ��
# starttime = datetime.datetime.now()
# print GetFileMd5(filepath)
# endtime = datetime.datetime.now()
# print '����ʱ�䣺%ds'%((endtime-starttime).seconds)



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

