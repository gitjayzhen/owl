# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: test_file_inspector.py
@time: 2024/3/25 14:11
"""
from owl.lib.file.file_inspector import FileInspector


class TestFileInspector:

    def setup(self):
        self.fc = FileInspector()

    def test_has_file(self):
        assert self.fc.is_has_file("test_file_inspector.py")

    def test_not_has_file(self):
        assert not self.fc.is_has_file("test_file_ins.py")
