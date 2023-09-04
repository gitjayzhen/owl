# 使用 python 来设计简单的接口自动化测试框架

# 接口api管理平台
1. [API管理平台XXL-API](https://github.com/xuxueli/xxl-api)
2. [Web接口管理工具](https://github.com/thx/RAP)
3. [网易接口管理平台](https://nei.netease.com/login?url=%2Fprogroup%2Fhome%2Fmanagement%2F)
4. [WireMock](http://wiremock.org/)


## 20170605
1. http请求中的host、port、path、header、parms(get)、body(psot)、cookie、session等；
2. 请求中的parms和body中涉及到的数据类型：string、int、dict(json)等；
3. 请求数据的格式有：转码的base64字符串（图片识别接口）、普通字符串、gzip文件等；
4. 返回的数据我们需要关注的：网络状态码、cookie、session、接口返回数据格式(json、html)等；

5. 我们要做的是封装一套网络请求的api，初始化和配置好我们需要的接口请求参数（url+parms），
再封装一套解析接口返回数据的api，保存或校验接口返回的数据；
6. 封装各种处理文件的api，包括文件的编码和解码；

httpclient.py 模块主要处理接口的请求组合和请求发送

参数化方式：class进行类变量定义、config进行定义、excel进行定义、数据库进行定义

## 20180620
1. 接口自动化如果做到线上监控，那么结合网络爬虫的方式来达到监控和定位的效果
2. 针对接口还是像之前那样确认接口需要的资源，并对其进行规则化管理
3. 数据模板方式（excel、cvs、数据库）,使用pandas库来读写数据
