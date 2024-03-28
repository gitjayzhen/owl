#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@email:     jayzhen_testing@163.com
@site:      https://github.com/gitjayzhen
@software:  PyCharm & Python 3.7
@file:      demo3
@time:      4/19/21 7:21 PM
"""

import string


class Solution:

    def __init__(self):
        self.UPPER = string.ascii_uppercase

    def change(self, s):
        if s in self.UPPER:
            s = s.lower()
        else:
            s = s.upper()
        return s

    def trans(self, s, n):
        # write code here
        content = ""
        if n > 500:
            n = 500
        elif n < 1:
            n = 0
        if len(s) > n:
            s = s[:n]
        s = s[::-1]
        res = []
        for i in s.split(" "):
            # res.append("".join(list(i.upper())))
            res.append("".join(map(self.change, i))[::-1])
        res[-1] = res[-1][0].lower() + res[-1][1:]

        return " ".join(res)


class Solutions:

    def __init__(self):
        self.UPPER = string.ascii_uppercase

    def change(self, s):
        if s in self.UPPER:
            s = s.lower()
        else:
            s = s.upper()
        return s

    def trans(self, s, n):
        s = s[::-1]
        print(s)
        # s = s.replace(" ", "#")
        res = []
        for i in s.split(" "):
            t = map(self.change, i)
            tmp = "".join(t)
            # print(tmp[::-1])
            res.append(tmp[::-1])

        return " ".join(res)


s = Solutions()
print(s.trans("This is a sample", 16))
print(s.trans(" h i", 4))
print(s.trans("h i ", 4))

"""
您的代码已保存
答案错误:您提交的程序没有通过所有的测试用例
case通过率为0.00%后台判题数据不一定包含示例数据，请认真调试代码

用例:
" h i",4
"h i ",4
"Now Co der",10
"NowCoder",8
"now coder",9
"NOW CODER",9
"now Coder",16
"p EUQxHnqEMFAiwoJdBr T oRPQwbffaw AOmgwQwCDSRDk",48
"PldinyLUShdbxwbAkeWLPHFH Cex iGkvdKWHl B sQLmmPzDHA",51
"XVWqpiqZUYhRVuC q",17
"fgPPu FQvKiddHpxW",17
"PxmGUeoRZAuQtulOZhvDPan zgKCEzMuKySmxtpcMFkMv dwpSfjLcHo EFQkPMIirtfTfKeiNnoMZsO ixHnBuYeluzV IWh",98

对应输出应该为:

"I H "
" I H"
"DER cO nOW"
"nOWcODER"
"CODER NOW"
"coder now"
"cODER NOW"
"aoMGWqWcdsrdK OrpqWBFFAW t euqXhNQemfaIWOjDbR P"
"SqlMMpZdha b IgKVDkwhL cEX pLDINYlusHDBXWBaKEwlphfh"
"Q xvwQPIQzuyHrvUc"
"fqVkIDDhPXw FGppU"
"iwH IXhNbUyELUZv efqKpmiIRTFtFkEInNOmzSo DWPsFJlChO ZGkceZmUkYsMXTPCmfKmV pXMguEOrzaUqTULozHVdpAN"

你的输出为:

SAMPLE A IS tHIS
"I H "
" I H"
"DER cO nOW"
"nOWcODER"
"CODER NOW"
"coder now"
"cODER NOW"
"aoMGWqWcdsrdK OrpqWBFFAW t euqXhNQemfaIWOjDbR P"
"SqlMMpZdha b IgKVDkwhL cEX pLDINYlusHDBXWBaKEwlphfh"
"Q xvwQPIQzuyHrvUc"
"fqVkIDDhPXw FGppU"
"iwH IXhNbUyELUZv efqKpmiIRTFtFkEInNOmzSo DWPsFJlChO ZGkceZmUkYsMXTPCm

"""
