# OWL

>The owl(override the world limit) project is a tidy implementation for testing purposes

<!-- TOC -->
* [OWL](#owl)
  * [项目设计](#)
  * [环境](#)
  * [工作](#)
    * [20180331 设计完成工具类 utils](#20180331--utils)
    * [20180408 web自动化的基础架构已初步完成](#20180408-web)
    * [20180815 可以使用新的测试和报告库](#20180815-)
    * [20181215 对于http，thrift，dubbo，hessian协议的测试](#20181215-httpthriftdubbohessian)
    * [20190414 完善三类测试手册](#20190414-)
    * [20230816 升级到 selenium4、appium2](#20230816--selenium4appium2)
<!-- TOC -->

**背景：** 这个工程是为了练习或者总结什么而创建的？因为想过去一段时间使用到的 ui自动化(mobile、web)、接口自动化、网络爬虫都融合在同一个工具里，通过 python 来实现。
因为当前都是脚本曾层面的实现，希望后面有精力结合 flask/tornado 把 web 展示端也实现了。

<div align="center">    
<img src="owl/owl.jpg" width = "400" height = "300" alt="图片名称" />
</div>
## 内容

## 项目设计

* 基于 python 去做 Web UI 自动化、Mobile UI 自动化、接口自动化相关的事情；
* 应用一些经验上的需要：弱耦合，高内聚，复用性，易用性，可读性，易拓展；
* 引用的核心：selenium、appium、requests、allure、pytest；

## 运行环境

1. [anaconda](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)：类似于一个本地仓库，就像java的maven一样，第三方库很多，就显得很强大，管理起来也很方便（既然我们的需求本身就很大，那么就需要一个大的基础）
2. virtualenv：简单型虚拟环境控制工具，但是没有自己的管理仓库，需要手动添加
3. Pipenv 是一个python的依赖管理器，可以用pip管理依赖，但pip不能提供运行时环境，pipenv会帮你把包和environment的问题一起解决，及pip+virtualenv。

**开始选择了 virtualenv, 升级 python3+ 后用的 conda**

## 重要改动

### 20180331 设计完成工具类 utils

* 日志: 格式化日志的输入内容，文件和控制台形式打印日志。
* 文件检索：在项目目录下，检索是否存在给定文件名的文件。
* 字符串操作： 自定义fomat，及字符串转字典的场景方法。
* 日期格式化： 对date和time的输出进行格式化。
* 加密处理：zip等文件的解压操作，md5操作。
* 配置文件操作：对配置文件进行读写。

### 20180408 web自动化的基础架构已初步完成

### 20180815 可以使用新的测试和报告库

1. allure
2. allure-pytest
3. pytest
4. allure-pytset-adapter 通过 pytest 测试产生数据，让 allure 来展示

### 20181215 对于http，thrift，dubbo，hessian协议的测试

1. http -> requests\httpx
2. thrift -> thrift
3. dubbo -> dubbo-client
4. hessian -> python-hessian (forked mustaine)

### 20190414 完善三类测试手册

详细的功能模块内容：
* [mobile](owl/api/mobile/README.md)
* [web](owl/api/browser/README.md)
* [interface](owl/api/interface/README.md)

### 20230816 升级到 selenium4、appium2

- https://github.com/gitjayzhen/airtest-uitesting-template/blob/main/pytest.ini
- https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/upgrade_to_selenium_4/
- https://appium.io/docs/en/2.0/quickstart/test-py/
- https://www.selenium.dev/zh-cn/documentation/webdriver/browsers/safari/

**UIAutomator2 is only supported since Android 5.0 (Lollipop)** 

### 20240328

- 项目用于归纳脚本级内容

1. 新技术或设计模式脚本
2. thrift 接口测试脚本
3. 自动化测试脚本
4. http 测试脚本
5. web3 测试脚本
6. websocket 测试脚本

- 去除conda前的(base) 标识

`conda config --set changeps1 false`

- [接口测试工具 Pycurl vs Requests](https://github.com/0xyd/Pycurl-vs-Requests)