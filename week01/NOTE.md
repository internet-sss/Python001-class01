1. 爬虫基本技术
```python
1. requests 获取原始网页内容
  import requests
  user_agent = ''
  header = {'user-agent' : user_agent}
  myurl = ''
  response = requests.get(myurl, headers=header)
  print(response.text)
  print(f'返回码是: {response.status_code}')

2. requests 获取原始网页内容，BeautifulSoup 框架进一步过滤处理
  import requests
  # 为了更好处理获取过来的网页内容
  from bs4 import BeautifulSoup as bs
  user_agent = ''
  header = {'user-agent' : user_agent}
  myurl = ''
  response = requests.get(myurl, headers=header)
  # 较版本 1 进一步处理
  bs_info = bs(response.text, 'html.parser')
  for tags in bs_info.find_arr('div', attrs={'class': 'hd'}):
      for a_tag in tags.find_all('a'):
          # 获取所有链接
          print(atag.get('href'))
          # 获取电影名字
          print(atag.find('span').text)

3. requests 获取原始网页内容，BeautifulSoup 框架进一步过滤处理
  import requests
  # Xpath 方式处理网页内容，配合网页上的 Xpath
  import lxml.etree
  url = ''
  user_agent = ''
  header = {}
  header['user-agent'] = user_agent
  response = requests.get(url, headers=header)
  # xml 化处理
  selector = lxml.etree.HTML(response.text)
  # 根据网页不同 XPath
  film_name = selector.xpath('网页Xpath/text()')
  # f-->字符串中嵌入变量或表达式
  # r-->防止字符串中字符转义
  print(f'电影名称：{film_name}')
  plan_date = selector.xpath('')
  print(f'上映日期：{plan_date}')
  rating = selector.xpath('')
  print(f'评分：{rating}')

  # 将内容聚合在一起
  mylist = [film_name, plan_date, rating]
  # 将数据存储为文件
  import pandas as pd
  movie1 = pd.DataFrame(data = mylist)
  # windows 需要使用 gbk 字符集
  movie1.to_csv('./movie1.csv', encoding='utf8', index=false, header=false)

4. requests 获取原始网页内容，BeautifulSoup 框架进一步过滤处理，再根据网站规律进行分页处理
  import requests
  from bs4 import BeautifulSoup as bs
  # 定义函数，
  def get_url_name(myurl):
      user_agent = ''
      header = {'user-agent' : user_agent}
      response = requests.get(myurl, headers=header)
      bs_info = bs(response.text, 'html.parser')

      for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
          for a_tag in tags.find_all('a'):
              print(a_tag.get('href'))
              print(a_tag.get('span').text)

  # 生成包含所有页面的元组
  urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))
  print(urls)
  # 控制请求的频率，引入了 time 模块
  from time import sleep
  sleep(10)
  for page in urls:
      get_url_name(page)
      sleep(5)

```


2. http 协议
```python
浏览器传输的信息
  1.网页内容
  2.控制的信息
    network
      header（请求头）
        General
          Request URL: https://movie.douban.com/celebrity/1047973/
          Request Method: GET
          Status Code: 200 OK
          Remote Address: 154.8.131.172:443
          Referrer Policy: unsafe-url

          通过机器判断 Status Code == 200 来判断是否正常响应
          500，是不是爬虫请求频率过高，被对方服务器发现了

          除了 GET，还有POST（用户登录时）

        Response Headers
          Cache-Control: must-revalidate, no-cache, private
          Connection: keep-alive
          Content-Encoding: br
          Content-Type: text/html; charset=utf-8
          Date: Wed, 12 Aug 2020 11:55:52 GMT
          Expires: Sun, 1 Jan 2006 01:00:00 GMT
          Keep-Alive: timeout=30
          Pragma: no-cache
          Server: dae
          Transfer-Encoding: chunked
          Vary: Accept-Encoding
          Vary: Accept-Encoding
          X-Content-Type-Options: nosniff
          X-DAE-App: movie
          X-DAE-Instance: default
          X-Douban-Mobileapp: 0
          X-Xss-Protection: 1; mode=block

          

        Request Headers
          Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
          Accept-Encoding: gzip, deflate, br
          Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
          Connection: keep-alive
          Cookie: bid=fs8Qlc-UDKQ; douban-fav-remind=1; ll="118146"; __utmz=223695111.1587651779.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=0m0FdpFz9h9tYRN7dbz1KsdBNWPcXq73; _vwo_uuid_v2=DB36D80132C1976297FACD38DA0534FF1|8ff4d0cc2f064d3a14262fad89b82e14; gr_user_id=60183601-dce5-46f9-904a-3e68171ea8d7; viewed="26353219_26821357_34907497_24722612_27062586"; __utmz=30149280.1596727739.11.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1597196075%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; __utma=30149280.1867033382.1577427438.1596727739.1597196075.12; __utmc=30149280; __utma=223695111.60008701.1587651779.1587715410.1597196075.5; __utmc=223695111; _pk_id.100001.4cf6=e7c77f859c1aef86.1587651779.5.1597196078.1587715412.; __gads=ID=8888267a54e85b6c:T=1597224876:S=ALNI_MaRJlXVrnMhQnLcCYqajSlTNVGR7A
          Host: movie.douban.com
          Referer: https://movie.douban.com/subject/1292052/
          Sec-Fetch-Dest: document
          Sec-Fetch-Mode: navigate
          Sec-Fetch-Site: same-origin
          Sec-Fetch-User: ?1
          Upgrade-Insecure-Requests: 1
          User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36


          重点关心----> 
            Cookie：
              登录成功时，cookie中包含了用户名和密码的信息
            User-Agent：
              鉴别浏览器类型
              反爬虫：模拟Cookie、User-Agent（最基本的）

```

3. Scrapy 框架
```python
想要爬虫更智能
  1.控制爬虫时间
  2.存储为json或者其他格式的文件，想要存到数据库

核心组件
  1.引擎（Engine）
    “大脑”，只会其他组件系统工作。
    数据下载、数据处理都会流向这里，高效处理并行的爬取数据的
  2.调度器（Scheduler）
    调度器接收引擎发过来的请求，按照先后顺序，压入队列中，同时去除重复的请求。
    把引擎发过的请求进行先后的排序，去掉重复的请求
  3.下载器（Downloader）
    下载器（Downloader） 下载器用于下载网页内容，并返回给爬虫。
  4.爬虫（Spiders）
    爬虫（Spiders） 用于从特定的网页中提取需要的信息，即所谓的实体（Item）
    两个处理逻辑
      1.类似于 BeautifulSoup ，解析完成后将结果进行返回，如果请求的是url，可以通过引擎发起下一次请求，更方便的编写大型爬虫
      2.
  5.项目管道（Item Pipelines）
    用户也可以从中提取出链接，让 Scrapy 继续抓取下一个页面。
    将爬取的信息通过管道存入到响应介质中，如文件、数据库等，也可同时存入文件和数据库
  6.下载器中间件（Downloader Middlewares）
    项目管道（Item Pipelines） 项目管道负责处理爬虫从网页中抽取的实体。
  7.爬虫中间件（Spider Middlewares）
    主要的功能是持久化实体、验证实体的有效性、清除不需要的信息等。


不同组件都与引擎相连
1.Spider：引擎通过配置去找需要爬取的域名，进而找到域名爬取的爬虫（Spiders提供）。一个 Engine 可以配置多个 Spider。如果找到相应的 Spider 呢，通过域名就可以准确找到对应的 Spider 组件，找到对应的 Spider 组件后，Spider 就会对对应的 url 进行爬取
2.Scheduler：Spider 将准备爬取的这个工作交给 Scheduler，调度器根据我们放入的 Spider 请求先后，进行一遍去重处理，根据去重后的先后顺序，将 Scheduler 发给引擎，引擎找到 Downloader
3.Downloader：Downloader 向互联网发起真正的请求，请求成功或者失败都有对应的返回，Downloader 接收返回信息，返回信息依然回到引擎中，无论发起下载请求还是下载返回信息都会经过 Downloader Middlewares ，下载器中间件可以是过滤、增加或者减少相应的东西，这也是下载中间件非常强大的地方
4.Spiders：数据回来继续交给引擎，引擎把数据交给 Spiders，我们还可以对信息做一遍过滤或者增加相应的东西。Spider 会做两方面的流出
  Item Pipeline
    数据爬取结束，进行保存的时候交给 items，通过 Pipeline 交给 items
  Scheduler
    如：爬取到的电影，获得的信息包含链接，需要再点击，再构建请求处理。Scrapy 框架处理的流程是，将信息中的 url 再交给 Engine ，Engine 再将请求交给 Scheduler


```
4. Scrapy 实战
```python
pip install -r requestments.txt
scrapy startproject spriders
cd spiders
cd spiders
# 以实际需要爬取的网站为关联命名
# 项目名：movies   域名：douban.com
scrapy genspider movies douban.com
# spriders.spriders.movies  这样的方式使用 basic  模块

默认创建的文件详情
第一层
  scrapy.cfg
    [settings]
    default = spiders.settings  # 整个爬虫框架的设置下载 spiders.settings 这个文件中
第二层
  settings.py 
    # 以 python 的语法写入，默认情况下先不动，如果返回 4??  对方网站可能做了反爬虫处理，这时需要设置 user_agent
  
第三层
  movies.py # 我们电影爬虫项目需要些的文件
    类首字母建议大写，驼峰法，方法首字母建议小写
    # 运行爬虫时，我们传入的名字一定是 movies
    name = 'movies'
    # 限制爬虫爬取网页的范围，不能无限制的爬取
    allowed_domains = ['douban.com']
    # 第一次发起请求的域名
    # 为什么要去做第一次发起请求呢
    # 有框架的原因，也有 http 协议的原因
    #   1.里面用到了一个 Twisted 的异步框架，异步框架要想启动的话必须先发起一次请求才能启动，所以配置了 start_urls ，表示第一次向谁先去发起启动
    #   2.Scrapy 在底层事先写好了 HTTP 的头，第一次发起请求的时候就获取了头部信息，所以我们没有设置头部信息
    start_urls = ['http://douban.com/']
    # 上面的几行代码是必须要写的，不然爬虫没办法运行

    # 真正要爬取内容了
    # self 对象本身
    # response，start_urls 去通过调度器、下载器发起了一次请求，请求回来之后我们得到的第一个返回信息
    def parse (self, response)
```

5. 将 requests 爬虫改写为 Scrapy 爬虫
```python
运行爬虫  scrapy crawl douban
requests 流程： 先去打开单页，在单页中获取名称和链接，再去实现翻页功能
scrapy 流程：
  前置逻辑：先让爬虫能够翻页，需要先写一个在 pass 之前能够运行一页的东西

yield：暂时当做 return 理解即可
scrapy.Request：调用真的 Downloader 发起请求了
  这个请求的头文件没有设置，可以在 settings 中进行设置，请求延时也没有设置，可以在 settings 中设置
  
# 在文件 ../items.py 中进行设置
item = DoubanmovieItem()
# 没有保存，为了解耦，返回的 items 会在 ../pipelines.py 中进行处理
# 每一次的爬虫请求都在 ../pipelines.py 进行一次处理，即 process_item 函数被调用一次
return items

额外的处理：settings.py 中进行
  USER_AGENT：为了防止反爬虫，可以设置随机的 USER_AGENT
  DOWNLOAD_DELAY = 1
  请求连接数量、下载连接数量、ip等设置

```

6. Scrapy爬取信息
```python
# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from doubanmovie.items import DoubanmovieItem


class DoubanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    # 起始URL列表
    start_urls = ['https://movie.douban.com/top250']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 10):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'hd'})
        #for i in range(len(title_list)):
        # 在Python中应该这样写
        for i in title_list:
            # 在items.py定义
            item = DoubanmovieItem()
            title = i.find('a').find('span').text
            link = i.find('a').get('href')
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    # 解析具体页面
    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item

```

7. Xpath
```python
import scrapy
from doubanmovie.items import DoubanmovieItem
# from bs4 import BeautifulSoup
from scrapy.selector import Selector
# 直接传 response
movies = Selector(response=response).xpath('//div[@class="hd"]')
# xpath 路径匹配，前导符号
# /     最上层开始寻找，即从 html 开始寻找，通常出现系统自动匹配情况
# //    从最上面的 div 向下依次寻找 div，并且带有 class="hd" 这样的属性
# .     从当前的位置继续向下寻找。如果从头去寻找涉及效率的问题
# ..    寻找同级的。如果它们的下级出现同名，则不好匹配，但是同级可能名字不同，然后再向下依次寻找
#       通常寻找都会找一个容易找到的、独特的标签或者属性，然后以这里为相对路径进行寻找

# @  属性，text() 内容   [1]  [2]  第几个标签等，  < = > 等


extract()  将元组中的元素全部释放出来
extract_first()  释放元组中第一个元素
strip  去掉空格

dont_filter  影响  allow_domain  整个属性，相当于屏蔽掉该属性
```

8. yield
```python
return 
  1.一次性将内容全部返回，如果用爬虫爬取数据，一次性将大量网页内容返回，都保存在内存中，占用过多
  2.返回的可能是柱子、字典、字符串等不同类型的数据格式
yield 
  1.一个一个返回
  2.返回的是一个单独的值，不用去考虑数据类型
  3.next(y) 单个提取数值，list(y) 全部提取数值，空了后 next(y)  StopIteration 异常


vscode 调试， shift + enter --> 执行选择的代码
--------------------------------------------------
推导式
  通常用来生成列表、字典、集合的，创建新的元素的。 for in 等

  # 列表推导式
  mylist2 = [i**2 for i in range(1, 11) if i > 5]

  # 循环嵌套
  mylist = [str(i) + j for i in range(1, 6) for j in 'ABCDE']

  # 用推导式将字典转换为列表
  mydict = {'key1': 'value1', 'key2': 'value2'}
  mylist2 = [key + ':' + value for key, value in mydict.items()]

  # 推导式生成字典
  mydict = {i: i*i for i in (5, 6, 7)}

  # 推导式实现字典的k-v互换
  {value: key for key, value in mydict.items()}

  # 推导式生成集合
  myset = {i for i in 'HarryPotter' if i not in 'er'}

  # 推导式生成 生成器（刚才通过 yield 生成的结果，而非 return），tuple需要显示指定
  mygenerator = (i for i in range(0, 11))
  print(mygenerator)
  print(list(mygenerator))
```

9.scrapy 选择器
```python


```