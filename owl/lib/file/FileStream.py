#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import os


class FileStream(object):

    # 文件输入流
    def file_input_stream(self, filename):
        try:
            f = open(filename, 'r')
            for line in f:
                for byte in line:
                    yield byte
        except StopIteration as e:
            f.close()
            return

    # 文件输出流
    def file_output_stream(self, input_stream, filename):
        try:
            f = open(filename, 'w')
            while True:
                byte = input_stream.next()
                f.write(byte)
        except StopIteration as e:
            f.close()
            return

    def show_file_properties(self, filepath):
        """显示文件的属性：包括路径、大小、创建日期、最后修改日期、最后访问日期"""
        file_prop = {}
        for root, dirs, files in os.walk(filepath, True):
            for filename in files:
                if filename.split(".")[1] != "py":
                    continue
                state = os.stat(os.path.join(root, filename))
                abs_key = (filename.split(".")[0]).lower()
                # file_prop[abs_key]["createTime"] = time.strftime("%Y-%m-%d%X", time.localtime(state[-1]))
                # file_prop[abs_key]["updateTime"] = time.strftime("%Y-%m-%d%X", time.localtime(state[-2]))
                # file_prop[abs_key]["latestVisitTime"] = time.strftime("%Y-%m-%d%X", time.localtime(state[-3]))
                createTime = time.strftime("%Y-%m-%d %X", time.localtime(state[-1]))
                updateTime = time.strftime("%Y-%m-%d %X", time.localtime(state[-2]))
                latestVisitTime = time.strftime("%Y-%m-%d %X", time.localtime(state[-3]))
                file_prop[abs_key] = {"createTime": createTime, "updateTime": updateTime, "latestVisitTime": latestVisitTime}
        return file_prop


if __name__ == "__main__":
    obj = FileStream()
    dicts = obj.show_file_properties("T:\OneDrive\icloud\Project\PyRequestsForInterfaceTest\src\com\interface\common\UrlManager.py")
    print(dicts)
