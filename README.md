# OWL

>The owl(override the world limit) project is a tidy implementation for testing purposes

<!-- TOC -->
* [OWL](#owl)
  * [项目设计](#)
  * [运行环境](#)
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

