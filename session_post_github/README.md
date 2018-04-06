# 用session　获取token值，构建表单登录github#


----------
##环境：

 - ubuntu 16.04
 - python 3.5.2
 - requests库和BeautifulSoup库


----------


###1、打开github登录页面，输入一个错的账号密码，发现表单数据为下面这样
![这里写图片描述](https://img-blog.csdn.net/20180407003046353?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21pbmlfcGFuZGE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
###也就是说我们需要post过去的数据为这样子的：

```
data = {
		'authenticity_token':"XXXX", # 一串不知道什么的值
		'commit':'Sign+in',
		'login':'1400720231',
		'password':'账号的密码',
		'utf8':'✓'
	}
```
###观察登录页面的html找到这个值的出处：
![这里写图片描述](https://img-blog.csdn.net/20180407003341478?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21pbmlfcGFuZGE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
###２、所以思路是，先获取这个值，然后再把这个数据填充到data数据中，再去post登录
####　　获取这个token的值：

```
import requests
from bs4 import BeautifulSoup
url = 'https://github.com/session' 
s = requests.session()
res = s.get(url)
html = BeautifulSoup(res.text, 'html.parser')
token = html.find('input',{'name':'authenticity_token'})['value']  # 获取到token的值
```
###　　构建表单去post：

```
data = {
		'authenticity_token':token,
		'commit':'Sign+in',
		'login':'1400720231',
		'password':'自己的密码',
		'utf8':'✓'
	}
```

###３、完整的过程：

```
# coding:utf-8
import requests
from bs4 import BeautifulSoup
url = 'https://github.com/session' 
s = requests.session()
res = s.get(url)
html = BeautifulSoup(res.text, 'html.parser')
token = html.find('input',{'name':'authenticity_token'})['value'] # 获取token值
login_url = 'https://github.com/session'

# 构建data表单
data = {
		'authenticity_token':token,  # 在这里赋值
		'commit':'Sign+in',
		'login':'1400720231',
		'password':'自己的密码',
		'utf8':'✓'
	}

res2 = s.post(login_url, data=data)  # 拿着表单书数据去post
a = BeautifulSoup(res2.text,'html.parser')
res2 = s.post(login_url, data=data)
a = BeautifulSoup(res2.text,'html.parser')
for i in a.find_all('span',{'class':'text-bold repo'}):  #匹配我的仓库名字
	print(i.string)
#结果：
# Django-Projects
# Python-Spider
# ArticleSpider
# Python_Codes
```
###＼４、结果对比：
![这里写图片描述](https://img-blog.csdn.net/20180407004211901?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21pbmlfcGFuZGE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



