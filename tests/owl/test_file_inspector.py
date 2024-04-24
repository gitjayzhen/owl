# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: test_file_inspector.py
@time: 2024/3/25 14:11

pytest用例运行级别：
●模块级（setup_module/teardown_module）开始于模块始末，全局的（类外生效、函数中生效）
●函数级（setup_function/teardown_function）只对函数用例生效（类外有函数时生效）
●类级（setup_class/teardown_class）只在类中前后运行一次(在类中生效，类外不生效)
●方法级（setup_method/teardown_method）开始于方法始末（在类中生效，类外不生效）
●类里面的（setup/teardown）运行在调用方法的前后（类中生效、类外有函数时生效）
"""
import allure

from owl.lib.processor.file_processor import FileInspector


def setup_module():
    print("——setup_module:整个.py模块开始执行一次【函数】")


def teardown_module():
    print("——teardown_module:整个.py模块结束执行一次【函数】")


def setup_function():
    print("====setup_function:每个用例开始前都会执行【函数】")


def teardown_function():
    print("====teardown_function:每个用例结束后都会执行【函数】")


def test_one():
    print("正在执行---test_one【函数】")


def test_two():
    print("正在执行---test_two【函数】")


def setup():
    print("@@@@@setup：每个用例开始前执行（调用方法前）【函数】")


def teardown():
    print("@@@@@teardown：每个用例结束后执行（调用方法后）【函数】")


@allure.epic("owl framework unittest")
@allure.feature("本地文件检测公共类测试")
class TestFileInspector:
    fc = None

    def setup(self):
        self.fc = FileInspector()
        print("setup：每个用例开始前执行（调用方法前）")

    def teardown(self):
        print("teardown：每个用例结束后执行（调用方法后）")

    def setup_class(self):
        self.fc = FileInspector()
        print("setup_class:所有用例执行之前（类级）")

    def teardown_class(self):
        print("teardown_class:所有用例执行之后（类级）")

    def setup_method(self):
        print("setup_method:每个用例开始前执行（方法级）")

    def teardown_method(self):
        print("teardown_method:每个用例结束后执行（方法级）")

    @allure.story("本地存在文件")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_has_file(self):
        assert self.fc.is_has_file("test_file_inspector.py")

    @allure.story("本地不存在文件")
    def test_not_has_file(self):
        assert not self.fc.is_has_file("test_file_ins.py")
