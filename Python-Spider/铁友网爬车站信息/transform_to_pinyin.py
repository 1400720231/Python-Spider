# conding:utf-8
# author:panda
from xpinyin import Pinyin

"""
把始发站中文转化成英文 南宁-桂林  —---> nanning-guilin
str传进来是这这种格式：str = '南宁-桂林'
"""


def chinese_into_letters(str):
    a = Pinyin()
    res = a.get_pinyin(str)
    res2 = res.replace('---','*')
    return ''.join(res2.split('-')).replace('*', '-')




