要使用 Python 快速编写一个简单的 gRPC 服务接口和客户端，你需要遵循以下步骤：

1. **安装 gRPC Python 工具**

首先，确保你已经安装了 gRPC Python 工具。你可以使用 `pip` 来安装：

```bash
pip install grpcio
pip install grpcio-tools
```

2. **定义服务接口（.proto 文件）**

创建一个 `.proto` 文件来定义你的 gRPC 服务接口。例如，创建一个名为 `helloworld.proto` 的文件：

```protobuf
syntax = "proto3";

package helloworld;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

3. **生成 Python 代码**

使用 `grpcio-tools` 提供的 `protoc` 插件来生成 Python 代码：

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. helloworld.proto
```

这将在当前目录下生成 `helloworld_pb2.py`（消息类）和 `helloworld_pb2_grpc.py`（服务类）。

4. **编写 gRPC 服务端**

创建一个 Python 文件来实现 gRPC 服务端。例如，`server.py`：

```python
import grpc
from concurrent import futures
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
```

5. **编写 gRPC 客户端**

创建另一个 Python 文件来实现 gRPC 客户端。例如，`client.py`：

```python
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    # 注意这里使用的是服务端监听的地址和端口
    with grpc.insecure_channel('[::]:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter received: " + response.message)

if __name__ == '__main__':
    run()
```

6. **运行服务端和客户端**

首先，启动 gRPC 服务端：

```bash
python server.py
```

然后，在另一个终端或命令提示符窗口中启动 gRPC 客户端：

```bash
python client.py
```

客户端应该会收到来自服务端的问候消息，并打印到控制台。

这就是使用 Python 编写简单的 gRPC 服务接口和客户端的基本步骤。请注意，这只是一个基本的示例，用于演示如何开始使用 gRPC。在实际应用中，你可能需要处理更多的错误情况、添加认证和授权机制、使用 TLS 进行加密通信等。