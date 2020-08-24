[pretty_errors](https://pypi.org/project/pretty-errors/)
[try](https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-try-statement)
[with](https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-with-statement)
[with 语句上下文管理器](https://docs.python.org/zh-cn/3.7/reference/datamodel.html#with-statement-context-managers)


1. 异常捕获与处理
```python

Traceback
1. LookupError 下的 IndexError 和 KeyError
2. IOError
3. NameError
4. TypeError
5. AttributeError
6. ZeroDivisionError


try:
  1/0
except (Exception) as e:
  try:
    1/0
    print(e)
  except (Exception) as e1:
    print(e1)


当一段程序中有多个异常，在一个 try/catch 中捕获了一个异常，其他的异常就不再被捕获，是一个程序的陷阱
------------------------------------------------------------
自定义异常
# 通常集成BaseException，自定义需要集成 Exception
class UserInputEr(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

userinput = 'a'

try:
    if (not userinput.isdigit()):
        # raise 抛出异常
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    # 将变量所占用的内存释放掉
    del userinput

美化异常，优化异常结果、打开文件异常
import pretty_errors
def foo():
    1/0

foo()
# 展示的结果更清晰，并带有彩色字样
```

2. 使用PyMySQL进行数据库操作
```python
# 一般流程
# 开始-创建connection-获取cursor-CRUD（查询并获取数据）-关闭cursor-关闭connection-结果
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'test'
}

sqls = ['select 1', 'select VERSION()']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['prot']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

    def run(self):
        # 除了下方的再添加哪些信息，关键字如何写，如何找到这些信息
        # 1.PyMySQL 官方帮助
        # 2.ctrl + 左键，python对传入的参数都会当做对象处理，写的类型主要是提示作用（Type Hint），好处是更灵活，缺点是传准确
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事务
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()
    
    if __name__ == "main":
        db = ConnDB(dbInfo, sqls)
        db.run()
        print(result)
        
------------------------------------------------------------
# 工作中真正使用 MySQL
# 为了支持表情等信息，使用 utf8mb4
import pymysql

conn = pymysql.connect(host = 'localhost',
                      port = 3306,
                      user = 'root',
                      password = '123456',
                      database = 'python',
                      charset = 'utf8mb4'
                      )

# 获得cursor游标对象
con1 = conn.cursor()

# 操作的行数，获得的返回结果不是查询内容，还需要再处理
count = con1.execute('select * from tb1;')
print(f'查询到 {count} 条记录')

# 获得一条查询结果
result = con1.fetchone()
print(result)

# 获得所有查询结果
print(con1.fetchall())

con1.close()
conn.close()

# 执行批量插入
values = [(id, 'testuser'+str(id)) for id in range(4, 21)]
cursor.executemany('INSERT INTO ' + TABLE_NAME + ' values(%s, %s)', values)
```
3. 反爬虫：模拟浏览器的头部信息
```python
反爬虫
    1.根据基本的请求做判断，比较好做反反爬虫
    2.根据用户的行为做判断，反反爬虫效率可能会降低

容易识别
头部信息：
    1.User-Agent、Referer等
        网络上搜索大量的 User-Agent 信息
        通过 f12 进行抓包，将抓包的 Header 复制下来
        每次请求带有不同的浏览器头部
        Referer 是跨站的
        通过 WebDriver 方式进行请求
    2.带cookies（包含加密的用户名、密码验证信息）
        账户名、密码


模拟 User-Agent 
form fake_useragent import UserAgent
# 防止被浏览器因为 ssl 验证不过而被封 IP
ua = UserAgent(verify_ssl=False)

# 模拟不同浏览器
print(f'Chrome浏览器：{ua.chrome}')
print(f'Safari浏览器：{ua.safari}')
print(f'IE浏览器：{ua.ie}')

# 随机返回头部信息，推荐使用
print(F'随机浏览器：{ua.random}')

浏览器提取最新版本的 User-Agent 信息，F12 复制

有的网站会验证 User-Agent、Host、Referer 等信息，有些网站会自己定义一些数据（如：x-client-data）

```

4. 反爬虫：cookies验证
```python
很多网站直接复制 cookie 信息是可以的，但是大型爬虫系统就显得繁琐（每次启动爬虫都需要复制 cookie）

模拟用户登录

scrapy start_urls 中，刚好和模拟一次 post 登录请求相吻合

登录成功后，有的浏览器通过 Referer 跳转，有的通过很长的带有参数名的地址进行跳转
# 会话对象：在同一个 Session 实例发出的所有的请求之间保持 cookie
# 期间使用：urllib3 的 connection pooling 功能
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升
s = requests.Session()

form_data = {
    'ck': '',
    'name': '',
    'password': '',
    'remember': 'false',
    'ticket': ''
}
# 浏览器关注的是账户密码，而 Request 会关注所有应该出现的参数

```
5. 使用WebDriver模拟浏览器行为
```python
js 加密了信息
python 调用 webDriver 操作浏览器中间过程可能更复杂


```

6. 验证码识别
```python
opencv等
```
7. 爬虫中间件&系统代理IP
```python
请求 IP
{
    "origin": "14.123.254.1"
}

加载引擎  Twisted
加载配置文件
加载扩展信息和中间件
    加载下载中间件
    加载 SPirder 下载中间件
得到结果
显示 Download 信息

# 无日志显示
scrapy crawl httpbin --nolog

1.支持代理
2.增加代理的相关设置
3.通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理

打开 DOWNLOAD_MIDDLEWARES  注释在 settings.py 中进行设置
    执行顺序，根据后面的数字，数字小优先级高，改成 None 变成不用了
```

8. 自定义中间件&随机代理IP
```python
希望爬虫足够健壮，异常的处理交给各自的模块，如：Download middleware 的自带的异常处理模块

整个功能不需要我们全部重写
1.从配置文件中读取配置项
2.设置到代理上去即可

先将 HttpProxyMiddleware 这个中间件引入进来
然后继承 HttpProxyMiddleware 这个类，然后编写自己的方法

1.将对应配置传入进方法，然后进行解析
2.学的时候最有效的方式就是学一下系统，通过 print 方法
```
9. 分布式爬虫
```python
redis
分布式爬虫需要解决的问题
1.队列问题
2.管道共享问题
```

10. job1 
```python
1.创建 scrapy 项目
    scrapy startproject iptomysql
    cd iptomysql
    cd iptomysql
    # 如果使用 scrapy genspider iptomysql douban.com，则不会创建 spiders/iptomysql.py
    scrapy genspider movies douban.com
   
2.编写 movies.py文件
    1.首次请求网也信息，获取请求头
        def start_requests(self):
            url = f'https://maoyan.com/films?showType=3'
            yield = scrapy.Request
```