#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author: jayzhen
@message: jayzhen_testing@163.com
@site: https://github.com/gitjayzhen
@software: PyCharm & Python 2.7
@file: HesssianClient.py 
@time: 2018/09/14 12:27 
"""
from pyhessian.client import HessianProxy
# 从pyhessian导入HessianProxy，用它来发请求
from pyhessian import protocol


# 这个是用来进行把咱们python的数据类型序列化成二进制的

def dubbo_api(url, interface, method, param_obj, **kwargs):
    '''
    :param url: url地址
    :param interface: 接口名称，因为这里可能还有别的服务要测，接口名不一样，这里定义成变量
    :param method: 调用哪个方法
    :param param_obj: 入参的对象
    :param kwargs: 这个用关键字参数，因为每个接口的参数都不一样，不固定，所以这里用关键字参数
    :return:
        '''
    req_param = protocol.object_factory(param_obj, **kwargs)
    # 这个是用来构造二进制的入参的，也就是把入参序列化
    try:  # 用try捕捉一下异常
        req_obj = HessianProxy(url + interface)
        # 这个req是生成一个请求对象
        res = getattr(req_obj, method)(req_param)
        # getattr是python的内置方法，获取对象的方法，咱们从构造的请求对象里面获取到方法，然后调用，把前面生成的
        # 序列化好的参数传进去，然后获取到返回的数据
    except Exception as e:
        print('有异常了，异常信息是：%s' % e)
        res = {"msg": "异常：%s" % e, "code": 300}
        # 这个是自己定义的异常，如果调用出错了，就返回这个
    return res


if __name__ == '__main__':
    url = 'http://192.168.1.100:8181/api/'
    interface = 'yz.rpc.api.HelloApi'
    method = 'hello'
    param_obj = 'yz.rpc.api.param.Param'
    params = {"sth": "rpc", "ints": [1, 2, 3], "maps": {"name": "rpc"}}
    # 这个入参，为了不定义多个变量，咱们把它写成字典形式的,就和stu=dubbo这种方式调用是一样的
    over = dubbo_api(url, interface, method, param_obj, **params)
    # 测试调用一下
    print(over)  # 打印结果