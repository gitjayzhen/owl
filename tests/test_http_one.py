# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license:  Apache Licence
@software: PyCharm & Python 3.8+
@file: test_http_one.py
@time: 2023/8/16 12:43
"""

from owl.api.interface.http_requests import Requester


class TestHttpInterface:

    def test_http_interface(self):
        """
        3A 原则
        """
        url = "https://api.vvhan.com/api/hotlist?type=baiduRD"
        resp = Requester().do_get(url=url)
        assert resp['success'], "接口请求异常"

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

    def test_address_asset(self):
        url = "https://newtestapi.bt.io/bttc/bridgeTokenMap/getAccountTokenBalanceNew?accountAddress=0x23efda6afe6166f685fe647b812a5e338fa72ad1&content=&from_chain_id=4&to_chain_id=2"
        resp = Requester().do_get(url)
        print(resp)
        assert resp['result'] == "0x1ff973cafa8000", "gasPrice had changed"

    def test_relayer_list(self):
        url = "https://newtestapi.bt.io/bttc/relayer/list?token=TZDXJyYhSjM8T4cUYqGj2yib718E7ZmGQc&chain_id=1&refuel_mode=true"
        resp = Requester().do_get(url)
        print(resp)
        assert resp['data']['total'] > 0, "relayer dont online"
