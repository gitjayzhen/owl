# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license:  Apache Licence
@software: PyCharm & Python 3.8+
@file: test_http_one.py
@time: 2023/8/16 12:43

Epic:
Feature: 标注主要功能模块
Story: 标注Features功能模块下的分支功能
Severity: 标注测试用例的重要级别
Step: 标注测试用例的重要步骤
Issue和TestCase: 标注Issue、Case，可加入URL
"""
import allure

from owl.api.interface.http_requests import Requester


@allure.epic("HTTP 协议接口测试")
@allure.feature("单个 HTTP 接口测试用例集")
class TestHttpInterface:

    def test_http_get(self):
        """
        3A 原则
        """
        allure.dynamic.story("pass for http get")
        allure.dynamic.title("test_http_interface")
        allure.dynamic.description("testing for owl")
        allure.dynamic.tag("HTTP", "GET", "Authentication")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.label("owner", "jayzhen")
        allure.dynamic.link("https://dev.example.com/", name="Website")
        allure.dynamic.issue("AUTH-123")
        allure.dynamic.testcase("TMS-100")
        url = "https://api.vvhan.com/api/hotlist?type=baiduRD"
        resp = Requester().do_get(url=url)
        assert resp['success'], "接口请求异常"

    @allure.epic("HTTP 协议接口测试")
    # @allure.feature("bt 接口测试")
    @allure.story("bt testnet gas price")
    @allure.title("test_bt_pre")
    @allure.description("testing for jayzhen")
    @allure.tag("NewUI", "Essentials", "Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "jayzhen")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-123")
    @allure.testcase("TMS-200")
    def test_bt_pre(self):
        url = "https://pre-rpc.bt.io/"
        param = {
            "jsonrpc": "2.0",
            "id": "10",
            "method": "eth_gasPrice"
        }
        resp = Requester().post_json(url, json_data=param)
        print(resp)
        assert resp['result'] == "0x1ff973cafa8000", "gasPrice had changed"
        # bytearray.fromhex()
        # bytes.fromhex()

    @allure.story("pass for get account token balance new")
    def test_address_asset(self):
        url = "https://newtestapi.bt.io/bttc/bridgeTokenMap/getAccountTokenBalanceNew?accountAddress=0x23efda6afe6166f685fe647b812a5e338fa72ad1&content=&from_chain_id=4&to_chain_id=2"
        resp = Requester().do_get(url)
        print(resp)
        assert resp['result'] == "0x1ff973cafa8000", "gasPrice had changed"

    @allure.story("pass for get relayer list ")
    def test_relayer_list(self):
        url = "https://newtestapi.bt.io/bttc/relayer/list?token=TZDXJyYhSjM8T4cUYqGj2yib718E7ZmGQc&chain_id=1&refuel_mode=true"
        resp = Requester().do_get(url)
        print(resp)
        assert resp['data']['total'] > 0, "relayer dont online"
