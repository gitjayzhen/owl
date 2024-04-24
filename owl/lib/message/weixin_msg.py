# coding: utf-8

import time
import urllib.request
import json
import sys

"""
touser否成员ID列表（消息接收者，多个接收者用‘|’分隔，最多支持1000个）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
toparty否部门ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
totag否标签ID列表，多个接收者用‘|’分隔。当touser为@all时忽略本参数
msgtype是消息类型，此时固定为：text
agentid是企业应用的id，整型。可在应用的设置页面查看
content是消息内容
safe否表示是否是保密消息，0表示否，1表示是，默认0
"""


# baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
# securl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % access_token


class WeChatMessage(object):

    def __init__(self, content):
        self.gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        self.gettoken_content = {
            'corpid': '*',
            'corpsecret': '*-*',
        }
        self.main_content = {
            "touser": "@all",
            "agentid": 1,
            "msgtype": "text",
            "text": {
                "content": content,
            }
        }

    def get_access_token(self, string):
        token_result = json.loads(string.read())
        access_token = token_result['access_token']
        return access_token.encode('utf-8')

    def geturl(self, url, data):
        data = self.encodeurl(data)
        response = urllib.request.urlopen('%s?%s' % (url, data))
        return response.read().decode('utf-8')

    def posturl(self, url, data, isjson=True):
        if isjson:
            data = json.dumps(data, ensure_ascii=False)
            response = urllib.request.urlopen(url, data)
            return response.read().decode('utf-8')

    def encodeurl(self, dict):
        data = ''
        for k, v in dict.items():
            data += '%s=%s%s' % (k, v, '&')
        return data


if __name__ == '__main__':
    content = sys.argv[1]

    msgsender = WeChatMessage(content)
    access_token_response = msgsender.geturl(msgsender.gettoken_url, msgsender.gettoken_content)
    access_token = json.loads(access_token_response)['access_token']
    sendmsg_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % access_token
    msgsender.posturl(sendmsg_url, msgsender.main_content)
#
