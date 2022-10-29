# owl@override the world limit

这个工程是为了什么而建立？因为想把 ui自动化(client、browser)、接口自动化、网络爬虫都融合在同一个工具里，使用 python 来实现。
因为当前都是脚本曾层面的实现，希望后面有精力结合 flask/tornado 把 web 展示端也实现了。

![](doc/image/owl.jpg "owl")

## 项目管理

### 规范

* 基于python的web自动化、mobile自动化、接口自动化的整合项目
* 弱耦合，高内聚，复用性，易用性，可读性，易拓展
* 核心：selenium、appium、requests

```text
owl@override the world limit

2018年3月28日
23:51

Src
    com/framework:
        utils ：将普通的输入格式化为标准输入
            dataUtil: 处理数据
            dateUtil: 处理日期
            encryptUtil： 处理实体加密
            fileUtil： 文件类
            reporterUtil：报告模块
            stringUtil: 字符串处理
            Conifg
        Core:
            adb: 封装的adb底层命令
            dos: 封装的window命令
        Services ：独立的完整服务，有特有的逻辑处理能力，并能给出结果：服务的供给
            HttpClient
            Report
            Monitor
        database ：数据模型对象，处理各种数据驱动；数据库操作对象（mysql、redis、mongodb、rabbitmq）
        mobile ：手机ui自动化及appium的一系列操作
        interface : 接口测试使用及requests的一系列操作
        web ：webui自动化及selenium的一系列操作
    test: 这里构建一些框架测试的脚本
resources : 测试配置文件
    config ：框架使用的所有配合文件都在这里
    doc: 一些框架设计相关的文档
    driver: webdriver驱动
    excel: 测试使用的数据
    image：图片
    shell： 一些bat和sh脚本
result:
    log: 公共log日志
    mobile：手机特殊的日志目录
    web： web特殊的日志目录
```

## 环境管理（开始选择了 virtualenv, 升级3后用的 conda）

1. [anaconda](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)：类似于一个本地仓库，就像java的maven一样，第三方库很多，就显得很强大，管理起来也很方便（既然我们的需求本身就很大，那么就需要一个大的基础）
2. virtualenv：简单型虚拟环境控制工具，但是没有自己的管理仓库，需要手动添加
3. Pipenv 是一个python的依赖管理器，可以用pip管理依赖，但pip不能提供运行时环境，pipenv会帮你把包和environment的问题一起解决，及pip+virtualenv。

版本控制：GitHub

## python库（截至20190414）

1. python 2.7 (64位）
2. selenium 3.5
3. [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html) 0.8.2
4. beautifulsoup4                4.6.0
5. Appium-Python-Client          0.24
6. beautifulsoup4                4.6.0
7. chardet                       3.0.4
8. cx-Oracle                     6.0.3
9. imageio                       2.1.2
10. numpy                         1.13.3
11. pandas                        0.22.0
12. Pillow                        4.2.1
13. PyMySQL                       0.7.11
14. requests                      2.18.4
15. selenium                      3.5.0
16. xlrd                          1.0.0
17. XlsxWriter                    1.0.2
18. xlutils                       2.0.0
19. xlwt                          1.3.0

## 工具类utils（20180331）

* 日志: 格式化日志的输入内容，文件和控制台形式打印日志。
* 文件检索：在项目目录下，检索是否存在给定文件名的文件。
* 字符串操作： 自定义fomat，及字符串转字典的场景方法。
* 日期格式化： 对date和time的输出进行格式化。
* 加密处理：zip等文件的解压操作，md5操作。
* 配置文件操作：对配置文件进行读写。
* ...

## web自动化的基础架构已初步完成（20180408）

## 可以使用新的测试和报告库（20180815）

1. allure
2. allure-pytest
3. pytest
4. allure-pytset-adapter 通过 pytest 测试产生数据，让allure来展示

## 对于http，thrift，dubbo，hessian协议的测试

1. http -> requests\httpx
2. thrift -> thrift
3. dubbo -> dubbo-client
4. hessian -> python-hessian (forked mustaine)

## 20190414 备注并 init github project

详细的功能模块内容：

* [mobile](framework/mobile/README.md)
* [web](framework/web/readme.md)
* [interface](framework/api/interface/readme.md)
