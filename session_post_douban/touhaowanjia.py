# coding:utf-8
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
s = requests.session()
login_url = 'https://accounts.douban.com/login'
get_url = 'https://movie.douban.com/subject/4920389/comments?start=480&limit=20&sort=new_score&status=P&percent_type=' 

res =s.get(login_url)
html = BeautifulSoup(res.text,'html.parser')
# 验证码图片地址
href_tagert = html.find_all('img',{'id':'captcha_image'})

#如果有验证码存在就用构建一个有验证码信息的data,没有就构建另一个
if len(href_tagert)==0:
	data = {
	'source':'movie',
	'redir':'https://movie.douban.com/',
	'form_email': '18778331181',
	'form_password': '250onion????',
	'login':'登录'}
else:
	solution_href = href_tagert[0]['src']
	urlretrieve(solution_href)  # 下载到本地默认的图片下载保存地址了
	solution = input('输入你的验证码：')
	captcha_id = html.find_all('input',{'name':'captcha-id'})[0]['value']
	data = {
	'captcha-id':captcha_id,
	'captcha-solution':solution,  # 验证码的值
	'source':'movie',
	'redir':'https://movie.douban.com/',
	'form_email': '你的帐号',
	'form_password': '你的密码',
	'login':'登录'
	}
# 图片链接
# print(href)
print(captcha_id)
print(solution)
# source: movie
# redir: https://movie.douban.com/
# form_email: xxxxxxxxx
# form_password: 250onion????
# captcha-solution: prison
# captcha-id: GxO4oH5kxjtVOQGbI913iZpE:en
# login: 登录
headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
res = s.post(login_url,headers=headers,data=data)
res = s.get(get_url)
html = BeautifulSoup(res.text, 'html.parser')
comments = html.find_all('div', {'class':'comment-item'})
for i in comments:
	print(i.find('p').string)