# 1. requests 框架获取网页整体内容
#   设置用户代理
#   设置请求头
#   设置请求路径
#   构建请求，并获得响应对象
#   打印信息并存储，防止多次获取信息被限制
#   使用 BeautifulSoup 对信息进行初处理，制定解析器。html.parser、lxml-xml、xml、lxml等
#   
# 2. BeatifulSoup 框架处理获取后的网页内容
#   先锁定明显特征，筛选出初步操作列表
#   根据 select、select_one、find、find_all等方法
#       筛选条件：css选择器等
#       后续操作：.text、.next_sibling、.strip()等
#
# 3. Pandas 将筛选好的数据存入相应文件
#   pd.DataFrame 构建二维表
#   将二维表存入文件：to_csv、to_excel、to_json、to_html等
# 4. 将操作步骤存放到方法中
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# 浏览器类型、操作系统及版本、CPU类型、浏览器渲染引擎、浏览器语言、浏览器插件等

# Mozilla/5.0                           固定写法（历史遗留问题？），很少  Mozilla/4.0
# (Macintosh; Intel Mac OS X 10_15_1)   操作系统
# AppleWebKit/537.36                    浏览器内核
# (KHTML, like Gecko)                   排版引擎
# Chrome/78.0.3904.108                  浏览器类型与版本
# Safari/537.36                         浏览器类型与版本

# Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
# Mozilla/5.0 (Linux; U; Android 7.0;m2 note Build/LMY47D) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/5.0.2


# user_agent = 'Mozilla/5.0 Linux; U;Android 7.0;m2 note Build/LMY47D) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/5.0.2'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
url = 'https://maoyan.com/films?showType=3'
header = {'user-agent': user_agent}
response = requests.get(url, headers=header)
print(response)
bs_info = bs(response.text, 'html.parser')
print(bs_info)

count = 0
list_info = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
    temp = []
    i = 0
    if count < 10:
        tags_info = tags.find_all('div', attrs={'class': 'movie-hover-title'})
        # 匹配属于父元素的特定类型的第 n 个子元素的每个元素
        temp.append('电影名称: ' + tags_info[0].select_one("span:nth-of-type(1)").text)
        temp.append(tags_info[1].find('span').text + ' ' + tags_info[1].find('span').next_sibling.strip())
        temp.append(tags_info[3].find('span').text + ' ' + tags_info[1].find('span').next_sibling.strip())
        count = count + 1
        list_info.append(temp)

print(list_info)

movie1 = pd.DataFrame(data=list_info)
movie1.to_csv('./movie.csv', encoding='utf8', index=False, header=False)
