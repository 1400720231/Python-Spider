# coding:utf-8
# author:1400720231
"""
叫高铁管家下面的铁友网：http://www.tieyou.com/zixun/39489.html
获取某个的url的班车次数
"""
import requests
from bs4 import BeautifulSoup
# 有班次
# url = 'http://www.tieyou.com/daigou/nanning-guilin.html?date=2018-01-24&utm_source=tieyou&is_local=1'
# 没班次
# url2 ='http://www.tieyou.com/daigou/baise-fangchenggangbei.html?date=2018-01-24&utm_source=tieyou&is_local=1'


def get_times(url):
    res = requests.get(url)
    html = BeautifulSoup(res.text.encode('iso-8859-1').decode('gbk'))
    data = html.find_all('div', {'class': 'list_tit'})
    a = data[0].find('small')
    b = a.find('b')
    return b.string

