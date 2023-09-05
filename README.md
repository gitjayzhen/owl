# OWL

>The owl(override the world limit) project is a tidy implementation for testing purposes


背景：这个工程是为了什么而建立？因为想把 ui自动化(client、browser)、接口自动化、网络爬虫都融合在同一个工具里，使用 python 来实现。
因为当前都是脚本曾层面的实现，希望后面有精力结合 flask/tornado 把 web 展示端也实现了。

![](doc/image/owl.jpg "owl")

## 内容

### 项目设计

* 基于 python 去做 Web UI 自动化、Mobile 自动化、接口自动化相关的事情；
* 应用一些经验上的需要：弱耦合，高内聚，复用性，易用性，可读性，易拓展；
* 引用的核心：selenium、appium、requests、allure、pytest；

```text
.
├── LICENSE
├── README.md
├── configs # 测试配置文件
│   ├── Youku_11.0.40_19babfbcea8e1838.apk
│   ├── appium-service.ini
│   ├── chromedriver
│   ├── owl-appium.ini
│   ├── owl-framework.ini
│   ├── owl-selenium.ini
│   └── permission.json
├── doc
│   ├── UsersLogin.xls
│   ├── districtcode.txt
│   ├── image
│   └── 接口测试用例集.xlsx
├── naming-convention.md
├── owl
│   ├── __init__.py
│   ├── __pycache__
│   ├── api # 手机ui自动化及appium的一系列操作, 接口测试使用及requests的一系列操作, webui自动化及selenium的一系列操作
│   ├── configs
│   ├── core    # 封装的adb底层命令,封装的window命令 
│   ├── database    # 数据模型对象，处理各种数据驱动；数据库操作对象（mysql、redis、mongodb、rabbitmq）
│   ├── domain
│   ├── exception
│   └── lib # 将普通的输入格式化为标准输入、处理数据、处理日期、处理实体加密、文件类、报告模块、字符串处理
├── requirements.txt
├── setup.py
├── shell   # 一些bat和sh脚本
│   ├── local-se.bat
│   ├── remote-se.bat
│   ├── start-appium.bat
│   └── stop-appium.bat
├── tests   # 这里构建一些框架测试的脚本
│   ├── __init__.py
│   ├── test_appium_case.py
│   ├── test_http_one.py
│   └── test_ui_se_local.py
└── result
    ├── log: 公共log日志
    ├── mobile：手机特殊的日志目录
    └── web： web特殊的日志目录
```

## 环境

1. [anaconda](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)：类似于一个本地仓库，就像java的maven一样，第三方库很多，就显得很强大，管理起来也很方便（既然我们的需求本身就很大，那么就需要一个大的基础）
2. virtualenv：简单型虚拟环境控制工具，但是没有自己的管理仓库，需要手动添加
3. Pipenv 是一个python的依赖管理器，可以用pip管理依赖，但pip不能提供运行时环境，pipenv会帮你把包和environment的问题一起解决，及pip+virtualenv。

**开始选择了 virtualenv, 升级 python3+ 后用的 conda**

## Version

### 20180331 设计完成工具类 utils

* 日志: 格式化日志的输入内容，文件和控制台形式打印日志。
* 文件检索：在项目目录下，检索是否存在给定文件名的文件。
* 字符串操作： 自定义fomat，及字符串转字典的场景方法。
* 日期格式化： 对date和time的输出进行格式化。
* 加密处理：zip等文件的解压操作，md5操作。
* 配置文件操作：对配置文件进行读写。

### 20180408 web自动化的基础架构已初步完成（）

### 20180815 可以使用新的测试和报告库

1. allure
2. allure-pytest
3. pytest
4. allure-pytset-adapter 通过 pytest 测试产生数据，让allure来展示

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

- https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/upgrade_to_selenium_4/
- https://appium.io/docs/en/2.0/quickstart/test-py/