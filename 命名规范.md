# 命名

## 创建文件记得在文件的头部添加文件【创建日期】

文件命名采用：

1. 实际的内容用：“demo_”开头
2. 测试的内容用：“test_”开头
3. 成品的内容用：“应用方向简写_”开头
4. 描述性文件用：“explain_”开头

文件夹命名方式：单个词或多个词组的名，首字母小写以下划线链接 ，如：test_case 

## 源码下的文件夹：

Tip

module_name,
package_name,
ClassName,
method_name,
ExceptionName,
function_name,
GLOBAL_VAR_NAME,
instance_var_name,
function_parameter_name,
local_var_name.
应该避免的名称

单字符名称, 除了计数器和迭代器.
包/模块名中的连字符(-)
双下划线开头并结尾的名称(Python保留, 例如__init__)

## 命名约定

所谓”内部(Internal)”表示仅模块内可用, 或者, 在类内是保护或私有的.
用单下划线(_)开头表示模块变量或函数是protected的(使用import * from时不会包含).
用双下划线(__)开头的实例变量或方法表示类内私有.
将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
对类名使用大写字母开头的单词(如CapWords, 即Pascal风格), 但是模块名应该用小写加下划线的方式(如lower_with_under.py). 尽管已经有很多现存的模块使用类似于CapWords.py这样的命名, 但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致, 这会让人困扰.

```
Type                          Public(公共)              Internal(内部)
Modules                       lower_with_under          _lower_with_under
Packages                      lower_with_under
Classes                       CapWords                  _CapWords
Exceptions                    CapWords
Functions                     lower_with_under()        _lower_with_under()
Global/Class                  Constants                 CAPS_WITH_UNDER _CAPS_WITH_UNDER
Global/Class Variables        lower_with_under          _lower_with_under
Instance  Variables           lower_with_under          _lower_with_under (protected) or __lower_with_under (private)
Method Names                  lower_with_under()        _lower_with_under() (protected) or __lower_with_under() (private)
Function/Method Parameters    lower_with_under
Local Variables               lower_with_under

_xxx      不能用'from module import *'导入
__xxx__ 系统定义名字
__xxx    类中的私有变量名
```

核心风格：避免用下划线作为变量名的开始。

"单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；如果修改，无需通知外部。
"双下划线" 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。

以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入；除非在__init__.py中使用__all__显示定义。
以双下划线开头的（__foo）代表类的私有成员；编译时会翻译成：_classname__foo, 且不会被子类覆盖。
以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如 __init__（）代表类的构造函数。

python中类里的属性变量以：
_xxx 单下划线开头，类似于php中的protected，意思是受保护的，只能再本类以及子类中访问
__xxx 双下划线，类似于private，私有的，只能本类中访问，连子类都无法访问


项目集要求：
成品或待完成项目，在项目集中建立目录，项目名称要求完整英文且首字母大写
demo统一在system中

github项目管理：
1.只能在私用网络下上传个人本地项目代码
2.git commit的备注格式：
     1.日期 用户名 提交类型  需求概述（20170301 jayzhen,push/update/delate collect phone device infos）
     2.多个提交或多个更新，以";"间隔


备注：本项目的文件命名与上面规则有点不一样

分类目录都是小写单词或以首字母小写第二个单词首字符大写

模块文件名：是每个单子的首字母都大写

类名：尽量与模块名一致

方法：就是小写单词加下划线

静态变量：全大写
