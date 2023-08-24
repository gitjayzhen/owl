# -*- coding:utf-8 -*-

import json
import urllib.parse
import urllib.request
from configparser import ConfigParser
from http.cookiejar import CookieJar


class Requester(object):
    """ 配置要测试接口服务器的ip、端口、域名等信息，封装http请求方法，http头设置"""

    def __init__(self, ini_file):
        config = ConfigParser.ConfigParser()

        # 从配置文件中读取接口服务器IP、域名，端口
        config.read(ini_file)
        self.host = config.get("HTTP", "host")
        self.port = config.get("HTTP", "port")
        self.headers = {}  # http 头

        # install cookie
        cookie = CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        urllib.request.install_opener(opener)

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port

    # 设置http头
    def set_header(self, headers):
        self.headers = headers

    # 封装HTTP GET请求方法
    def get(self, url, params):
        if not params and params != "":
            params = urllib.parse.urlencode(eval(params))  # 将参数转为url编码字符串
        url = 'https://' + self.host + ':' + str(self.port) + url + params
        request = urllib.request.Request(url, headers=self.headers)

        try:
            response = urllib.request.urlopen(request)
            response_content = response.read().decode('utf-8')  # decode函数对获取的字节数据进行解码
            print(response.geturl())
            print(response.info())
            json_response = json.loads(response_content)  # 将返回数据转为json格式的数据
            return json_response
        except Exception as e:
            print('%s' % e)
            return {}

    # 封装HTTP POST请求方法
    def post(self, url, data):
        data = json.dumps(eval(data))
        data = data.encode('utf-8')
        url = 'https://' + self.host + ':' + str(self.port) + url
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request, data)
            response = response.read().decode('utf-8')
            json_response = json.loads(response)
            return json_response
        except Exception as e:
            print('%s' % e)
            return {}
