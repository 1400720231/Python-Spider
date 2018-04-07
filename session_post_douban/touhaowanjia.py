# coding:utf-8
import requests
from bs4 import BeautifulSoup


url = 'https://github.com/session' 
s = requests.session()
res = s.get(url)
html = BeautifulSoup(res.text, 'html.parser')
token = html.find('input',{'name':'authenticity_token'})['value']
login_url = 'https://github.com/session'

data = {
		'authenticity_token':token,
		'commit':'Sign+in',
		'login':'1400720231',
		'password':'250onion????',
		'utf8':'✓'
	}

res2 = s.post(login_url, data=data)
a = BeautifulSoup(res2.text,'html.parser')
for i in a.find_all('span',{'class':'text-bold repo'}):
	print(i.string)
res3 = s.get('https://github.com/1400720231/Django-Projects')
html = BeautifulSoup(res3.text, 'html.parser')
a = html.find_all('td', {"class":'content'})
print(a)