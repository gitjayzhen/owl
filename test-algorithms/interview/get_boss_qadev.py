#!/usr/bin/env python
# -*- encoding: utf-8 -*-


'''
@Author  :   jayzhen
@Email   :   jayzhen_testing@163.com
@Ide     :   vscode & conda
@Blog    :   https://blog.csdn.net/u013948858
@File    :   get_boss_qadev.py
@Time    :   interview/08/28 15:10:47

解决 ModuleNotFoundError: No module named 'framework' https://www.cnblogs.com/hi3254014978/p/15202910.html
'''

'''
获取 boss 上的招聘信息和要求，进行分析

1. 测试开发:20-50K:5-10年: https://www.zhipin.com/web/geek/job?city=101010100&experience=106&position=100305&salary=406&page=1

https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91&city=101010100&experience=&degree=&industry=&scale=&stage=&position=100305&salary=&multiBusinessDistrict=&page=1&salary=406&pageSize=30

https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91&city=101010100&experience=&degree=&industry=&scale=&stage=&position=100305,100301,100302,100303,100304,100306,100309&salary=&multiBusinessDistrict=&page=1&salary=406&pageSize=30
https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101010100&experience=&degree=&industry=&scale=&stage=&position=100301,100302,100303,100304,100305,100306,100309,100310&salary=406&multiBusinessDistrict=&page=1&pageSize=30
https://www.zhipin.com/web/geek/job?city=101010100&experience=106&position=100301,100302,100303,100304,100305,100306,100309,100310&salary=406

https://www.zhipin.com/web/geek/job?city=101010100&experience=106&position=100301,100302,100303,100304,100305,100306,100309,100310&salary=406&areaBusiness=110108,110114,110105
https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91&city=101010100&experience=106&degree=&industry=&scale=&stage=&position=100301,100302,100303,100304,100305,100306,100309,100310&salary=406&multiBusinessDistrict=110108,110114,110105&page=1&pageSize=30
'''

# http 2.0 的请求头
# :authority: www.zhipin.com
# :method: GET
# :path: /wapi/zpgeek/search/joblist.json?scene=1&query=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91&city=101010100&experience=&degree=&industry=&scale=&stage=&position=100305,100301,100302,100303,100304,100306,100309&salary=&multiBusinessDistrict=&page=1&pageSize=30
# :scheme: https
BASE_HEADER = """
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7
cookie: lastCity=101010100; wd_guid=cbef9407-34d1-4f29-8837-9ddb0c1efdde; historyState=state; _bl_uid=X5lXX5q44g9pXeiCe5jF0sjh8ee7; __zp_seo_uuid__=2dcc8830-c863-4cfb-84d5-49d50ca85416; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1660284074,1660632669,1661671303; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1661671310; __zp_stoken__=395deE0Q5LkkRPCZQLAtxHH5UdGg%2FJn5FCnl2ZG5tYUcGYSsWS3URSQEkR15%2FFGwXczxyaF9RblgEAVV%2Fd3hqA35vUh4vdARKHnVlUDcKCAMRMGtkc1l7R3dqPVZaLg81XU0iICRHCR9wcDBQL1kSehYMSltwGW5QT2NLWXpJS2t2WykLJQhKDxsaAx0YFz08BkRIA210eg%3D%3D; __c=1661671303; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E6%25B5%258B%25E8%25AF%2595%25E5%25BC%2580%25E5%258F%2591%26city%3D101010100%26position%3D100305%2C100301%2C100302%2C100303%2C100304%2C100306%2C100309&s=3&g=&friend_source=0&s=3&friend_source=0; __a=63923714.1656816039.1660632669.1661671303.30.4.4.30
referer: https://www.zhipin.com/web/geek/job?query=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91&city=101010100&position=100305,100301,100302,100303,100304,100306,100309
sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
x-requested-with: XMLHttpRequest
"""

# 将所需要的目录加入到环境变量里
import sys
sys.path.append("/Users/apple/jayzhen/qadev/GITHUB/owl")


import json
# import httpx # https://www.python-httpx.org/http2/
import requests

from owl.utils.string.formatter import lines_str_to_dict

def get_data():
    query_url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91&city=101010100&experience=&degree=&industry=&scale=&stage=&position=100305&salary=&multiBusinessDistrict=&page=1&pageSize=100"
    req_header = lines_str_to_dict(BASE_HEADER)
    print("header", req_header)
    resp = requests.get(query_url, headers=req_header)
    save_file = open('100-boss.json', 'w+')
    json.dump(resp.json(), save_file)
    save_file.close()

def analysis_data():
    brand_name_set = set()
    read_file = open('100-boss.json', 'r')
    json_data = json.load(read_file)
    job_list = json_data['zpData']['jobList']
    for i in job_list:
        brand_name_set.add(i['brandName'])

    for i in brand_name_set:
        print(i)
        
if __name__ == '__main__':
    analysis_data()