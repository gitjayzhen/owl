# AppiumTestProject
<p> &nbsp; &nbsp; &nbsp; &nbsp;Appium自动化测试工具，比较好用的自动化工具，你值得学习。这个工程主要是个人对appium和Python理解的一个应用，可使用该工程进行app自动化测试。
工程还在一点一点的完善，补充的内容也一点一点的在时间轴中详细描述，工程具体的流程和代码逻辑可以自行review，代码中有相应的注释，如有需要也可以联系我 （邮箱：jayzhen_testing@163.com） ，希望你能通过这个工程获得一些你想获取的东西。
</P>

# 时间轴
## 20170321
- 需求：添加adb cmd的api<br>
- 项目下路径：/src/com/framework/ui_test_api/adb/commond.py<br>
- 需求概述：将adb 调试命令<br>


## 20170329
需求：封装appium基础的底层api, 在整个测试用例的编写过程，<br>
项目下路径：<br>
需求概述：<br>
1. 超时处理<br>
2. 异常处理<br>
3. 日志记录<br>
4. 代码弱耦合<br>
5. 逻辑强内聚<br>
6. 减小创建的次数<br>
7. APP监控了常用的men,cpu,fps<br>
8. 设备重连机制<br>
9. 邮件发送excel的测试报告<br>
10. 支持多设备andoird并行<br>

### 配置文件化-关于路径的操作
pathconfig.ini中的配置所需项的相对路径，通过getallpath调用configcommonctl来解析拿到数据数据，getallpath作为对外接口
提供最直接的操作


## 20170405
1. 第一封装层的api，不应该有超过4复杂度的设计<br>
2. 上层如果存在单一的逻辑直接写入底并提供调用方法


## 20170508
1. 使用mysqldb操作数据库<br>
2. 使用xlrd、xlwt和xlutils操作Excel文件


## 20170513
1. 如何进行多台设备进行同时执行？通过命令启动服务<br>
    命令行参数：
    >-p:是指定监听的端口（也可写成 --port），也可以修改为你需要的端口；<br>
    -bp:(Android-only) 连接设备的端口号是连接Android设备bootstrap的端口号，默认是4724（也可写成--bootstrap-port）<br>
    -U:连接物理设备的唯一设备标识符，是连接的设备名称，如"adb devices"获取的设备标识（也可写成--udid）<br>
    --chromedriver-port:是chromedriver运行需要指定的端口号，默认是9515<br>
    -a:是指定监听的ip（也可写成 --address），后面“127.0.0.1”可以改为你需要的ip地址；<br>
    --session-override:是指覆盖之前的session；

    启动对各服务端：
    >appium -p 4492 -bp 2251 -U udid_num  
    appium -p 4493 -bp 2252 -U udid_num2  
    ......

    客户端多个连接：
    >在脚本的capabilities.setCapability("udid","udid_num")   
    driver.remote("http://127.0.0.1:4492/wd/hub",cpabilities")
    udid和对应启动的服务器的端口保持一致<br>
    端口生成、doc命令执行、获取设备列表、启动多服务器
    
2. 现在做的逻辑就是：获取当前连接的设备数，启动相同数量的服务器并分配好未被占用的端口，同时要确认每个设备连接的是独立的服务端口
那么脚本必须做到多线程执行，不然会报错
3. 编写实际的自动化脚本时，记得先实力化server服务，然后进行多线程的设计（待完成）


## 20170728  20170730 (计划)
获取app的启动和首页的activity，可以通过查看apk包和已安装的app<br>
** aapt dump badging a.apk **    
** adb logcat -c && adb logcat -s ActivityManager **<br>
1. 启动参数配置化（run.ini）,在配置文件中读取驱动app启动的desired capabilities参数、还有关于是否重新安装的开关值
apk的安装包路径、app的启动activity、app的首页activity<br>
2. 是否重新安装的开关值，为0时，检查是否安装，若安装了先卸载，再安装；为1时，检查是否安装，没有安装就先安装再执行后续操作
，若安装了，就直接继续后续操作<br>
3. 根据udid来过去设备对应的port（当然多设备的时候，需要将配置文件中的内容设置为list，逗号隔开）<br>
4. 在脚本获取appium driver时，在线程中实例化一个线程，并返回这个driver<br>


## 20170801
1. 如果进行渠道包验证（指定目录下的所有apk，一部或多部手机，多线程数据共享） （待完成）<br>
2. 修改command.py中的app的安装、卸载和是否安装等方法；<br>
3. run.ini配置文件中的内容，不在进行代码设计，因为通过代码来获取app的启动activity和首页activity，没有多少现实意义，后续有时间可以考虑添加该功能；
4. 修改initappiumdriver中的数据获取方式；

## 20170802
1. APPIUM DRIVER已经设计完成，需要后续再多线程实例化和初始化上做一个详细的流程。
2. 初次启动服务并实例化driver，会出现urllib2.URLError，因为服务启动占用了端口，但是正式的服务内容还没有启动完成，在此时去Remote(url)就报错了，
放弃之前使用的超时、校验端口的方式，使用异常处理的方式来建立driver。
3. 同时解除InitDriverOption与ServicePort的耦合。
4. 改造InitService.generate_service_command中的数据形式，使用dict代替list。

## 20170804
1. 做了个实验，python自己的日志模块做的很好，就像自己做一下封装，当前的日志模块可以有两种实现方式：
    >1.将所有日志等级的handler在类的__init__方法中实例化     
     2.在类的之前以普通方式实例handler      
     3.使用配置文件的方式设置logging，其中一个是fileconfig，一个是dictconfig
2. 第一种方法会出现同一个日志level的logger，会有个handler，也就是会重复打印n个日志内容。而第二中方法不会出现这种情况，如果想使用第一种方法，也可以，就是在
打印日志后，将当前的handler关闭并移除当前的logger.handlers[i]
3. fileconfig和dictconfig比较方便的使用，但是日志的格式无法自定义，但是可以自己进行封装。
4. 现在项目中已经demo好了四种日志模板，可以用到任意项目中。


## 20171023
1. 通过ServicePort进行初始化的服务并生成的ini配置文件中添加一个run字段，如果为0：未执行；为1：执行过
2. InitDriverOption中初始化appiumdriver时，首先读取第一步生成的配置文件如果有

## 20171027
1. 优化一下项目管理
2. 测试脚本设计的一个建议，在创建线程前，先实例化appium服务，这时候通过配置文件来获取sno和port，
随后有了唯一设备的driver，然后就去执行脚本

## 20171221
1. 优化了启动后台appium服务的逻辑，及采用了线程方式来执行启动服务的命令。
2. 多机执行将会使用multiprocessing.Pool.map_async(caseFunc, driverList)
3. 启动服务后将bootstrap对应的端口也写入配置文件中，以便关闭appium服务的时候同时关闭该端口

## 20171227
1. 引入设计模式思想对driver初始装备和api分装进行独立解耦，并隐藏实例化后的driver对象，仅适用api进行全局脚本操作者
2. 这种做法有什么缺点，就是每次实例化api都要做一次driver的实例化操作，繁琐，并且在并行操作的时候还会影响响应时间
3. 将driver的创建放到api封装类中，这个修改会在分支dev_171227中

## 20180507
1. 需要解决手机的wifi掉线问题
2. 手机重启
3. 远程调试

## 对appium自动化框架的预想
2017.01.31
1. 关于appium的通信服务如可通过代码进行开启、关闭、重启？
2. 如何监控设备的链接状态？容错处理获取到的手机可用信息
3. app版本迭代是否会影响到UIautomator Viewer的控件ID的获取？


2017.02.28
1. appium设计主链路功能UI测试的框架（数据驱动、关键字驱动）
2. 实现测试过程中的性能数据收集

## 2023.08.17

1. 通过一个对象来管理整个测试要说用的内容，包括 3A 原则
2. 实例化这个对象需要做几个事情
   - 获取当前机器上链接的测试机器有哪些 device_list
   - 检查每个 device 是否有对应 appium server 来进行操控，如果没有就启动一个对应的服务，并将这个映射记录下来
   - 根据上面的映射，来实例化操作 device 的 driver 对象
   - 用 driver 对象来实例化 api 
   - 然后 通过 api 来写自动化用例