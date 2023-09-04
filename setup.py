# -*- coding: utf-8 -*-

"""
@author: jayzhen <jayzhen_testing@163.com>
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: setup.py
@time: 2023/8/15 17:07
"""
import io

from setuptools import setup, find_packages


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(
    name='owl',  # 打包后的包文件名
    version='1.0.0',  # 版本号
    keywords=["owl", "testing", "ui", "interface"],  # 关键字
    description='over the world limit',  # 说明
    long_description=long_description(),  # 详细说明 readme
    long_description_content_type="text/markdown",
    license="Apache License",  # 许可
    url='git@github.com:gitjayzhen/owl.git',  # 一般是GitHub项目路径
    author='gitjayzhen',
    author_email='jayzhen_testing@163.com',
    include_package_data=True,
    platforms="any",
    install_requires=[
        'selenium',
        'requests',
        'beautifulsoup4',
        'redis',
        'pymysql',
        'toml'
    ],  # 引用到的第三方库 可以设定版本
    # py_modules=[],  # 你要打包的文件，这里用下面这个参数代替
    packages=find_packages(include=['owl', 'owl.*', 'owl.**'], exclude=['tests', 'tests.*', 'tests.**']),
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"owl": "owl"},
    python_requires=">=3.8",
    zip_safe=False
)
