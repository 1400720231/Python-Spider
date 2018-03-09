# coding:utf-8
# author:1400720231
from xpinyin import Pinyin

"""
把始发站中文转化成英文 深圳-茂名  —---> shenzhen-maoming
str传进来是这这种格式：str = '深圳-茂名'
"""


def chinese_into_letters(str):
    a = Pinyin()
    res = a.get_pinyin(str)
    res2 = res.replace('---', '*')
    return ''.join(res2.split('-')).replace('*', '-')




