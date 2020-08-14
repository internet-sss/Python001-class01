1.为什么要学习Python
```python
1.python 特别简单
    如：AI工程师需要快速验证自己的想法，这时候需要胶水将想法与AI粘连到一起，Python就是这个胶水
2.python是高级语言
    python更贴近人类的语言

3.技能支持面向过程，也能支持面向对象
    对Java、C++程序员友好
    对运维开发的，用Shell的人员，也是友好的

4.第三方模块丰富
    Tensorflow等，C++大牛写出来
    有很丰富的扩展性

5.可以跨平台
    Windows、Linux、Max、树梅派上、IOT领域等
    windows开发，平滑迁移到Linux上

6.应用领域
    自动化运维、数据挖掘、数据科学家、深度学习、爬虫、web等

```

2.如何体系化地学习Python
```python
1.好的问题=70%的答案
    代码、报错、把问题具体化
    提问的智慧
    https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md

    1.旧论坛找答案
    2.上网
    3.手册
    4.常见问题FAQ
    5.找朋友
    6.源码

    问题提出在合适的论坛
    技术合适的场合
    找到合适的回答问题的人，不要随便发私信
    杜绝疯狂扫射素有帮助渠道，一个一个看会更好

    Stack Overflow
    Stack Exchange
    Stack Exchange community

    邮件列表
    有意义描述明确问题
    使问题容易回复：a b c三个选项等方法
    去掉无意义的问题赘述
    心存感激，简短说明等等等等

2.向谁发问
    目前：老师、同学
    google
    stackoverflow
    官网:
        较上个版本新的变化
        教程：入门基础
        ...
    github
        Github Help，搜索帮助

遵循python 代码规范
    官方：PEP8
         https://www.python.org/dev/peps/pep-0008/
    Google Python Style Guides
        http://google.github.io/styleguide/pyguide.html
```

3.不同操作系统中的环境变量配置方法
```bash
1.如何使用解释器
    更改python默认版本
    python -V
    目前Python3.x 更适合学习
    不选最新版本，某些库可嫩未做好兼容检测

    which python
    which python3
    echo $PATH
    为了让当前python版本先执行，
    export PATH=/.../python/bin:$PATH

    vim /etc/bashrc

```

4.加快第三方库的安装速度：配置pip源
```python
pip -V
pip3 -V
pip与python相关联

pip install requests

更换源
临时
pip install -i 源  包名

永久
pip install pip -U
pip config set global.index-url 源

国内源
豆瓣： https://pypi.doubanio.com/simple/
清华： https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
中科大： https://pypi.mirrors.ustc.edu.cn/simple/
阿里云： https://mirrors.aliyun.com/pypi/simple/

freeze功能，迁移
在 A 环境生成 env.txt
    pip3 freeze > env.txt
在 B 环境中克隆 A 环境
    pip3 install -r env.txt

```

5.提升开发效率：配置venv虚拟环境
```python
通过虚拟环境
    A项目中用第一个版本
    B项目中用第二个版本

设置虚拟环境
python3 -m venv venv1
python3 -m venv venv2

进入某一环境
    source venv1/bin/activate
        pip3 install requests

再打开一个终端
    source venv2/bin/activate
```

6.Visual Studio Code
```python
python(pylint 语法检查，并为发现)
autopep8 代码美观，格式化

点击左下角，可以选择不同python版本
点击右上角，运行python
下方会显示执行的python位置

```

7.Python基础语法概览
```python
1.如何交换两个变量的值，go一样
    var2, var1 = var1, var2

2.print辅助调试

3.可使用字节码方式，pyc这个文件交给python虚拟机运行
    
4.获取某类型的使用
    x = 1
    help(x)
    type(x)
    dir()   当前环境中被使用的变量和其类型
    exit()  退出命令行

5.内置数据类型
    数值、布尔
    字符串
    列表、元组、字典、集合

    数值：
        整数、浮点数、复数、布尔值
    布尔：
        True、False   大写首字母
    数值运算：
        + - * / //整除  %   **求幂


    不同引号都可以表示字符串
    元组不能更改，List不能代替元组
    字典：本质是哈希表，key 只能是数值、字符串、元组
    集合：由基本对象组成的无序集，唯一性
    False: 0 零值None 空（列表、字典、字符串等）
    True 其他值
    def 定义函数
    class 定义类
    固定写法的特殊方法
        __init__，双下划线

    标准库的使用





Python 标准语法： https://docs.python.org/zh-cn/3.7/tutorial/index.html
Python 内置函数： https://docs.python.org/zh-cn/3.7/library/functions.html
Python 内置类型： https://docs.python.org/zh-cn/3.7/library/stdtypes.html
Python 数据类型： https://docs.python.org/zh-cn/3.7/library/datatypes.html
Python 标准库： https://docs.python.org/zh-cn/3.7/library/index.html
Python 计算器使用： https://docs.python.org/zh-cn/3.7/tutorial/introduction.html
Python 数据结构： https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html
Python 其他流程控制工具 : https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html
Python 中的类： https://docs.python.org/zh-cn/3.7/tutorial/classes.html
Python 定义函数： https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions
```

8.语法
```
1.数字
    2 + 2 = 4
    50 - 5*6 = 20
    (50 - 5*6) / 4 = 5.0
    8 / 5 = 1.6 # division always returns a floating point number
    
    17 // 3 # floor division discards the fractional part
    5 ** 2 = 25

    j 或 J 表示虚数部分
2.魔法变量_
    交互模式下，上一次打印出来的表达式被赋值给变量_
    python作为桌面计算器会变得简单
3.字符串，immutable
    r，可以让字符串中的\以字符形式输出，而非转义
    乘法：3 * 'un' = 'ununun'
    相邻：'Py' 'thon' = 'Python'
    换行：text = ('Put a '
    ' to b')
        text--> Put a to b
    变量、表达式在 多个字符串自动连接情况报错

    有索引，可以负数索引（倒叙）
        word = 'Python'
        word[0] --> P
    切片
        word[0:2]、word[:2]、word[2:]、word[-2:]
    切片释义：
        将索引视作指向字符之间，第一个字符的左侧标为0，最后一个字符的右侧标为n
    索引越界
        word[42] --> 越界
        word[4:42] --> 不报错，会被自动处理掉

    immutable
        word[0] = 'J'  报错
        word[2:] = 'py'
    需要不同字符串，如下
        'J' + word[1:]

    内建函数返回长度
        len(s)

    文本序列类型 --- str
    字符串是一种 序列类型 ，因此也支持序列类型的各种操作。

    字符串的方法
    字符串支持许多变换和查找的方法。

    格式化字符串字面值
    内嵌表达式的字符串字面值。

    格式字符串语法
    使用 str.format() 进行字符串格式化。

    printf 风格的字符串格式化
    这里详述了使用 % 运算符进行字符串格式化。


4.列表,mutable
    squares = [1, 4, 9, 16, 25]
    索引、切片

    squares + [36, 49, 64, 81, 100]
    squares[0] = 0
    squares.append(121)
    squares[2:5] = []
    [[1, 2, 3], ['a'], 'b', 'c']

5.循环
    a,b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a+b

    print('The value of a is', a)
    end关键字，末尾追加字符串
    print(a, end=',') 


6.if
    if x < 0:
        print(x)
    elif x == 0:
        print(x)
    elif x == 1:
        print(x)
    else:
        print(x)

7.for
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

    循环时修改序列的值
    for w in words[:]:
        if len(w) > 6:
            words.insert(0, w)

    若是用 for w in words，将会是死循环

    遍历数字使用
    for i in range(5):
        print(i)
    0 1 2 3 4

    range(5, 10)
    range(0, 10, 3)
    list(range(5))

8.pass
    语句什么都不做

9.函数定义
    关键字参数、位置参数
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a,b = b, a+b
        print()
    
    fib(2000)

    函数打印默认值，只一次
        i = 5
        def f(arg=i):
            print(arg)
        i = 6
        f()
    
    默认值为可变对象时很重要（列表、字典、大多数类实例），函数会存储在后续调用中传递给它的参数
        def f(a, L=[]):
            L.append(a)
            return L

        print(f(1))
        print(f(2))
        print(f(3))

        [1]
        [1, 2]
        [1, 2, 3]

    若后续调用之间不共享内存
        def f(a, L=None):
            if L is None:
                L = []
            L.append(a)
            return L

    多扩展参数
        def cheeseshop(kind, *arguments, **keywords):
        * **

        解包参数
            range[3:6]
            range[*ar]

10.in
    测试序列包含某值

11.lambda 表达式，小的匿名函数
    def make_incrementor(n):
        return lambda x: x + n

12.文档字符串
    def my_function():
        """Do nothing, but document it.

        No, really, it doesn't do anything.
        """
        pass

    print(my_function.__doc__)
    Do nothing, but document it.

        No, really, it doesn't do anything.
```

9.数据结构
```python
1.列表
    list.append(e)
    list.extend(iterable)
    list.insert(i, e)
    list.remove(e)
    list.pop(i)，默认删除最后一个元素
    list.clear() <==> del a[:]
    list.index(e[, start[, end]])
    list.count(e)
    list.sort(Key=None, reverse=False)
    list.reverse()
    list.copy()  <==> a[:] //列表浅拷贝

2.栈
    用列表追加（append）实现栈压入元素，用弹出（pop）实现栈推出
    stack = [3, 4, 5]
    stack.append(6)
    stack.pop()

3.队列
    使用列表来实现效率很低，在列表开头添加元素会使其他元素向后移动，O(n)

    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    queue.append("")
    queue.popleft()

4.列表推倒式
    squares = []
    for x in range(10):
        squares.append(x**2)
    squares

    squares = list(map(lambda x: x**2, range(10)))
    squares = [x**2 for x in range(10)]

    花式操作
    [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x,y))

    [(x, y) for x in [1, 2, 3] if x != 1 for y in [3, 1, 4]]

    表达式，遍历，条件语句

5.嵌套列表
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    矩阵转置
    [[row[i] for row in matrix] for i in range(4)]
    
    zip  处理复杂的流程语句
    list(zip(*matrix))
    [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

6.del 语句，无返回值
    del a[0]
    del a[2:4]
    del a[:]

7.元组
    singleton = 'hello,
    t = 12345, 54321, 'hello!'
    k = ()

8.集合：不重复元素，无序集
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    'orange' in basket

    a = set('abracadabra')
    b = set('alacazam')
    a
    {'a', 'r', 'b', 'c', 'd'}
    b
    {'a', 'c', 'l', 'm', 'z'}

    a - b，差集
    {'r', 'd', 'b'}
    a | b，并集
    a & b，交集
    a ^ b，交集的补集

9.字典
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    list(tel)
    del tel['sape']
    sorted(tel)
    'guido' in tel

    构造函数创建
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    推导式
    {x: x**2 for x in (2, 4, 6)}
    关键字参数
    dict(sape=4139, guido=4127, jack=4098)

    key，value
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)

    索引，value
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

    zip 多序列循环使用
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

    逆序
    for i in reversed(range(1, 10, 2)):
        print(i)

    创建新的有序序列
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)

    深入条件控制
    in not in   是否在序列中
    is is not   是否同一个对象

    循环时修改列表内容，创建新列表比较简单且安全

    比较
    (1, 2, 3)              < (1, 2, 4)
    [1, 2, 3]              < [1, 2, 4]
    'ABC' < 'C' < 'Pascal' < 'Python'
    (1, 2, 3, 4)           < (1, 2, 4)
    (1, 2)                 < (1, 2, -1)
    (1, 2, 3)             == (1.0, 2.0, 3.0)
    (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)


```






问题
```python
1.什么是列表推导式

```