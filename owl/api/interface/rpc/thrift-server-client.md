Apache Thrift 是一个高效的、支持多种编程语言的远程服务框架。要使用 Python 快速编写一个简单的 Thrift 接口，你需要遵循以下步骤：

1. **定义 Thrift IDL 文件**

首先，你需要定义一个 Thrift 接口描述语言 (IDL) 文件。这个文件描述了你的服务及其方法、参数和返回类型。

例如，创建一个名为 `tutorial.thrift` 的文件：


```thrift
namespace py tutorial

struct Person {
    1: string name,
    2: i32 age,
    3: string email
}

service HelloService {
    string sayHello(1:Person person),
}
```
在这个例子中，我们定义了一个 `Person` 结构体和一个 `HelloService` 服务，该服务有一个 `sayHello` 方法。

2. **生成 Python 代码**

使用 Thrift 编译器生成 Python 代码。确保你已经安装了 Thrift 编译器。然后，在命令行中运行：


```bash
thrift --gen py tutorial.thrift
```
这将在当前目录下生成一个 `gen-py` 目录，其中包含从 IDL 文件生成的 Python 代码。

3. **编写 Python 服务器**

接下来，你可以编写一个 Python 服务器来实现 `HelloService`。创建一个名为 `server.py` 的文件：


```python
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransportUtils
from gen_py.tutorial import HelloService
from gen_py.tutorial.ttypes import Person

class HelloServiceHandler:
    def sayHello(self, person):
        print(f"Hello, {person.name}! You are {person.age} years old.")
        return "Hello from Thrift server!"

handler = HelloServiceHandler()
processor = HelloService.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransportUtils.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting the server...")
server.serve()
print("done.")
```
这个服务器在端口 9090 上监听连接，并实现了 `sayHello` 方法。

4. **编写 Python 客户端**

最后，你可以编写一个 Python 客户端来调用服务器上的 `sayHello` 方法。创建一个名为 `client.py` 的文件：


```python
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
from gen_py.tutorial import HelloService
from gen_py.tutorial.ttypes import Person

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloService.Client(protocol)

    transport.open()
    person = Person(name="Alice", age=30, email="alice@example.com")
    response = client.sayHello(person)
    print(response)

    transport.close()
except Exception as e:
    print(e)
```
这个客户端连接到服务器，创建一个 `Person` 对象，并调用 `sayHello` 方法。

5. **运行**
* 首先，确保 Thrift 编译器和 Python Thrift 库都已安装。
* 运行 `thrift --gen py tutorial.thrift` 生成 Python 代码。
* 运行 `python server.py` 启动服务器。
* 在另一个终端窗口中，运行 `python client.py` 启动客户端并调用服务器上的方法。你应该能在服务器终端窗口中看到打印的消息，并在客户端终端窗口中看到服务器的响应。