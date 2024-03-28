# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: test_cls.py
@time: 2023/9/4 19:30

在Python中，`__new__`、`__call__`和`__init__`是特殊的双下划线方法（也称为魔术方法或魔法方法）。它们在类的创建、实例化和初始化过程中起着重要的作用。

1. `__new__`方法：
   - 角色：`__new__`方法是用于创建并返回一个新的实例对象的静态方法。
   - 功能：它在对象实例化之前被调用，负责创建实例对象，并返回该对象。通常用于控制对象的创建过程，可用于自定义实例的创建逻辑或在特定条件下返回缓存的对象实例。
   - 参数：`__new__`方法的第一个参数是类本身，之后可以接收其他参数作为实例化时的输入。
   - 返回值：必须返回一个新的实例对象。

2. `__call__`方法：
   - 角色：`__call__`方法使得一个类的实例可以被像函数一样被调用，即对实例使用`()`调用。
   - 功能：它定义了类实例被调用时执行的行为。
   - 参数：`__call__`方法的第一个参数是类实例本身，之后可以接收其他参数作为调用时的输入。
   - 返回值：根据需要返回相应的结果。

3. `__init__`方法：
   - 角色：`__init__`方法是用于在创建实例对象后进行初始化的实例方法。
   - 功能：它在对象实例化之后被调用，用于对实例属性进行赋值或执行其他初始化操作。
   - 参数：`__init__`方法的第一个参数是类实例本身，之后可以接收其他参数作为初始化时的输入。
   - 返回值：无需返回任何值。

这些特殊方法在类定义和实例化过程中自动触发，并且允许我们自定义类的行为以满足特定的需求。通过重写这些方法，我们可以实现自己的逻辑来控制实例的创建、初始化和调用等操作。
"""


# 使用json.dumps将JSON对象转换为字符串，并设置缩进和排序参数
# json_str = json.dumps(resp.json(), indent=4)
#
# # 定义一个递归函数来处理嵌套的JSON对象并保留引号和括号
# def pretty_print_json(obj, indent=0):
#     if isinstance(obj, dict):
#         print('{' + (' ' if obj else ''))
#         for key, value in obj.items():
#             print(' ' * (indent + 4) + '"' + str(key) + '": ', end='')
#             pretty_print_json(value, indent + 4)
#         print(' ' * indent + '}' + ('' if indent == 0 else ','))
#     elif isinstance(obj, list):
#         print('[' + (' ' if obj else ''))
#         for item in obj:
#             print(' ' * (indent + 4), end='')
#             pretty_print_json(item, indent + 4)
#         print(' ' * indent + ']' + ('' if indent == 0 else ','))
#     else:
#         print(json.dumps(obj), end='')
#
# # 调用递归函数打印格式化后的JSON字符串
# pretty_print_json(json.loads(json_str))


class MyObject(object):

    def __str__(self):
        return "__str__"

    def __init__(self):
        print("__init__")

    def __call__(self, *args, **kwargs):
        print("__call__")
        return super.__call__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        print("\n__new__")
        return super().__new__(cls)


class MyObject2(MyObject):
    def __new__(cls, *args, **kwargs):
        print("\n__new__2")
        return super().__new__(cls)


class TestMyObject:

    def test_cls(self):
        a = MyObject()
        print(a)
        a()
