# 1.导入相关模块
import requests
from bs4 import BeautifulSoup

# 2.发送请求获取疫情首页内容
response =requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page =response.content.decode()
#print(home_page)
# 3.使用BeautifulSoup提取疫情数据
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(attrs={'id': 'getListByCountryTypeService2true'})
# text = script.text  用老师的方法拿不到,不知道为啥
text = script.string #看了评论区用的string类型拿到了
print(text)
