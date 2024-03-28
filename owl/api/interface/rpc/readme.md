[TOC]

# thrift接口测试 python

在window上使用python + thrift库来进行接口测试，通过官网下载的thrift-0.11.0.exe进行接口文件生成

## 一 .基础的命令

默认的命令

```text
thrift-0.11.0.exe -r  --gen py xAnti.thrift
```

修改输入路径的命令(设置gen-*包的输出目录(默认值是当前目录),他会生成`gen-py`目录)

```text
thrift-0.11.0.exe -o ../src/xAnti/ --gen py xAnti.thrift
```

修改输入路径的命令(为生成的文件设置输出位置(不会创建gen-*文件夹))

```text
thrift-0.11.0.exe -out ../src/xAnti/ --gen py xAnti.thrift
```

使用docker： thrift构建代码(兼容mac、liunx、window；避免thrift版本冲突）

```text
cd /Users/apple/jayzhen/qadev/qadev-test-script/thrift_test
docker run --rm --privileged -v "$PWD:/data" thrift:0.11.0 thrift -out /data/src/kgc/lib --gen py /data/thrift-files/kgc_bridge.thrift

如果有`include`其他文件(注意生成后的文件引入问题)

docker run --rm --privileged -v "$PWD:/data" thrift:0.11.0 thrift -r -out /data/src/jayzhen --gen py /data/thrift-files/doc/jayzhen_storage.thrift

```

**如果想在指定目录下生成指定的目录层级**

1. 自己先创建好对应的目录树，然后在`-out`加上路径
2. 在thrift文件中的`namespace`后面定义包空间
3. 注意thrift文件名一定要放到最后面，不然会报错`Unrecognized option`

## 二. thrift的sever设计

在服务器端启动thrift框架的部分代码比较简单，不过在写这些启动代码之前需要先确定服务器采
用哪种工作模式对外提供服务，Thrift对外提供几种工作模式，例如：TSimpleServer、
TNonblockingServer、TThreadPoolServer、TThreadedSelectorServer等模式，每种服务模
式的通信方式不一样，因此在服务启动时使用了那种服务模式，客户端程序也需要采用对应的通信
方式。

**另外**，Thrift支持多种通信协议格式：TCompactProtocol、TBinaryProtocol、
TJSONProtocol等，因此，在使用Thrift框架时，客户端程序与服务器端程序所使用的通信
协议一定要一致，否则便无法正常通信。


## 三. thrift的client设计

有上面生成的gen-py文件夹，所有接口对应的服务代码都在里面了，我们需要设计客户端代码来进行调用

1.创建一个传输层对象（TTransport），具体采用的传输方式是TFramedTransport，要与服务器端保持一致，这里的THRIFT_HOST, THRIFT_PORT分别是Thrift服务器程序的主机地址和监听端口号，这里的2000是socket的通信超时时间；即：

```java
m_transport =new TFramedTransport(newTSocket(THRIFT_HOST,THRIFT_PORT, 2000));
```

```python
tsocket = TSocket.TSocket(host, port)
transport = TTransport.TFramedTransport(tsocket)
```

2.创建一个通信协议对象（TProtocol），具体采用的通信协议是二进制协议，这里要与服务器端保持一致，即：

```java
TProtocol protocol =new TBinaryProtocol(m_transport);
```

```python
protocol = TBinaryProtocol.TBinaryProtocol(transport)
```

3.创建一个Thrift客户端对象（TestThriftService.Client），Thrift的客户端类TestThriftService.Client已经在文件TestThriftService.java中，由Thrift编译器自动为我们生成，即：

```java
TestThriftService.ClienttestClient =new TestThriftService.Client(protocol);
```

```python
client = Client(protocol)
```

4.打开socket，建立与服务器直接的socket连接，即：

```java
m_transport.open();
```

```python
transport.open()
```

5.通过客户端对象调用服务器服务函数getStr，即：

```java
String res = testClient.getStr("test1","test2");
System.out.println("res = " +res);
```

```python
dta = UserNumReq()
dta.Uid = 115775
dta.NumTypes = [1, 2]
result = client.get_user_num(dta)
```

6.使用完成关闭socket，即：

```java
m_transport.close();
```

```python
transport.close()
```

***这里有以下几点需要说明：***

1. 在同步方式使用客户端和服务器的时候，socket是被一个函数调用独占的，不能多个调用同时使用一个socket，
例如通过m_transport.open()打开一个socket，此时创建多个线程同时进行函数调用，这时就会报错，
因为socket在被一个调用占着的时候不能再使用；

2. 可以分时多次使用同一个socket进行多次函数调用，即通过m_transport.open()打开一个socket之后，
你可以发起一个调用，在这个次调用完成之后，再继续调用其他函数而不需要再次通过m_transport.open()
打开socket；

## 三. 通信之间的关注点

1.Thrift的服务器端和客户端使用的通信方式要一样，否则便无法进行正常通信；

```text
Thrift的服务器端的种模式所使用的通信方式并不一样，因此，服务器端使用哪种通信
方式，客户端程序也要使用这种方式，否则就无法进行正常通信了。例如，上面的代码2.3
中，服务器端使用的工作模式为TNonblockingServer，在该工作模式下需要采用的传输
方式为TFramedTransport，也就是在通信过程中会将tcp的字节流封装成一个个的帧，
此时就需要客户端程序也这么做，否则便会通信失败。
```

2.在服务器端或者客户端直接使用IDL生成的接口文件时，可能会遇到下面两个问题：

```text
[1] Cannotreduce the visibility of the inherited method fromProcessFunction<I,TestThriftService.getStr_args>

[2] The typeTestThriftService.Processor<I>.getStr<I> must implement theinherited abstract methodProcessFunction<I,TestThriftService.getStr_args>.isOneway()
```

问题产生的原因：

```text
问题[1] 是继承类的访问权限缩小所造成的；
问题[2] 是因为存在抽象函数isOneWay所致;
```

解决办法：

```text
问题[1]的访问权限由protected修改为public；
问题[2]的解决办法是为抽象函数添加一个空的函数体即可。
```

3.还有就是thrift的版本和生成代码的有必要加上版本号

## 四.thrift 基本语法

### 编写IDL文件时需要注意的问题

```text
函数的参数要用数字依序标好，序号从1开始，形式为：“序号:参数名”;

每个函数的最后要加上“,”，最后一个函数不加；

在IDL中可以使用/*……*/添加注释
```

### IDL支持的数据类型

[IDL](http://thrift.apache.org/docs/idl)大小写敏感，它共支持以下几种基本的[数据类型](http://thrift.apache.org/docs/types)：

```text
string， 字符串类型，注意是全部小写形式；例如：string aString

i16, 16位整形类型，例如：i16 aI16Val;

i32，32位整形类型，对应C/C++/java中的int类型；例如：      I32  aIntVal

i64，64位整形，对应C/C++/java中的long类型；例如：I64 aLongVal

byte，8位的字符类型，对应C/C++中的char，java中的byte类型；例如：byte aByteVal

bool, 布尔类型，对应C/C++中的bool，java中的boolean类型； 例如：bool aBoolVal

double，双精度浮点类型，对应C/C++/java中的double类型；例如：double aDoubleVal

void，空类型，对应C/C++/java中的void类型；该类型主要用作函数的返回值，例如：void testVoid(),
```

除上述基本类型外，ID还支持以下类型：

```text
map，map类型，例如，定义一个map对象：map<i32, i32> newmap;

set，集合类型，例如，定义set<i32>对象：set<i32> aSet;

list，链表类型，例如，定义一个list<i32>对象：list<i32> aList;
```

### 在Thrift文件中自定义数据类型

在IDL中支持两种自定义类型：枚举类型和结构体类型，具体如下：

```text
enum， 枚举类型，例如，定义一个枚举类型：

enum Numberz
{
  ONE = 1,
  TWO,
  THREE,
  FIVE = 5,
  SIX,
  EIGHT = 8
}
```

注意: 枚举类型里没有序号

```text
struct，自定义结构体类型，在IDL中可以自己定义结构体，对应C中的struct，c++中的struct和class，java中的class。例如：

struct TestV1 {
       1: i32 begin_in_both,
       2: string old_string,
       3: i32 end_in_both
}
```

注意: 在 struct 定义结构体时需要对每个结构体成员用序号标识：“序号: ”。

### 定义类型别名

Thrift的IDL支持C/C++中类似typedef的功能，例如：

```text
typedef i32  Integer 
```

就可以为i32类型重新起个名字Integer。

### 支持的数据类型、数据传输格式、数据传输方式和服务器类型

数据类型

```text
Base Types：基本类型
Struct：结构体类型
Container：容器类型，即List、Set、Map
Exception：异常类型
Service： 定义对象的接口，和一系列方法
```

数据传输格式
Thrift支持二进制和文本2类协议，二进制协议比本文协议更优。但是文本协议在某些情况下更有用（如debug）。

```text
TBinaryProtocol –二进制编码格式
TCompactProtocol –使用Variable-Length Quantity (VLQ) 编码对数据进行压缩，高效
TJSONProtocol – JSON编码格式
TSimpleJSONProtocol –只提供JSON只写协议, 生成的文件很容易通过脚本语言解析。
TDebugProtocol – 使用易懂的可读的文本格式，以便于debug
TDenseProtocoal – 和TCompactProtocol相似，但在发送时省略了meta信息，在接收端重新加上。还在实验中，java实现还不可用。
```

数据传输方式

```text
TSocket -阻塞式socketI/O
TFramedTransport – 以frame为单位进行传输，要求服务器为非阻塞式方式。
TFileTransport – 以文件形式进行传输，不支持java方式，但实现起来也很简单。
TMemoryTransport – 使用内存I/O，如同Java中的ByteArrayOutputStream实现。
TZlibTransport – 使用zlib进行压缩， 与其他传输方式联合使用。当前无java实现。
```

服务器类型

```text
TSimpleServer –单线程服务模型，使用标准的阻塞式I/O,常用于测试
TThreadPoolServer – 多线程服务模型，使用标准的阻塞式I/O。
TNonblockingServer – 多线程服务模型，使用非阻塞式I/O（需使用TFramedTransport数据传输方式）
```
