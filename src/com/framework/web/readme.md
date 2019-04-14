# web automation testing

# CSS Selector

```
1,input[name=\”xxx\”]  标签名+属性名中的值

2,class直接用 .
例如  class=”aabb”   那定位   .aabb

3，id用 #
例如  id=”bbcc”  那定位  #bbcc

4,同时选择多个条件匹配
例如 input a1=”abc”,a2=”bdf” 定位   input[a1=\”abc\”][a2=”\bdf\”]

5,层级定位，相领定位
a1>a2>a3
a+b   例如a[name=”abc”]+a    属性name=abc同级相邻的元素
a~b    匹配a的同级元素之后中的b


6,通配符定位
a[name^=\”abc\”]  ##name属性abc开头的
a[name$=\”abc\”]  ##name属性abc结尾的
a[name*=\”abc\”]  ##name中包含abc的


7,匹配全部后代元素， 空格
a[name=”abc”] b[name=”12”]   #匹配元素a节点下面name为12的元素
a[name=”abc”],b[name=”12”]   #匹配元素a或者匹配元素b 用逗号分隔


8，按照位置匹配
8.1,  p:first-of-type   匹配p元素列表中，第一个p元素。
8.2， p:last-of-type   匹配p元素列表中，最后一个p元素
注：上述是按照p元素的父元素下，全部P元素，按照位置生成一个列表去取，中间若有其它非P元素，不影响   规则可能不是这样的
8.3， p:nth-child(i)   匹配p元素列表中，指定位置i的P元素  从1开始计数 从前往后
注:是按照同为父元素全部位置，如果中间含有其它非p元素，也占一个位置
8.4,  p:nth-last-child(i)  匹配p元素列表中指定位置i的P元素，从1开始计数，从后往前
注:是按照同为父元素全部位置，如果中间含有其它非p元素，也占一个位置
8.5，p:nth-of-type(i)  匹配属于p元素中父元素下的指定位置i的P元素，从前往后
注：是只取该父元素下的P元素来生成一个数列，若中间含有其它非P元素，不占一个位置
8.6，p:nth-last-of-type(i)  同上，但是从后往前数
8.7，p:first-child   区配p元素当前列表中，排在第1个位置，
8.8，p:last-child   匹配p元素当前列表中，排在最后1个的位置

注：若当前节点第1个位置为非p，则匹配失败
```

## 20180508

1. 对于selenium执行页面js遇到的问题：window与document的区别？两者对那些页面元素能够直接操作
2. selenium的键盘和鼠标事件问题：actionChains和webelement的send_keys区别？
3. 新项目的测试用例设计需要继续优化
4. 断言机制：是通过绝对断言？还是个性化处理？
