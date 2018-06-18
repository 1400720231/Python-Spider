---
title: 2018-6-18selenium + Chrome 模拟浏览器爬淘宝信息
---
**环境配置：**
 1. ubuntu16.04
 2. python3.5.2 
 3. Chrome浏览器版本 67.0.3396.87（正式版本） （64 位）
 4.  chromedriver 2.40



**安装所需工具:**

 - 1 selenium三方库安装

``` nginx
pip install selenium  # 安装selenium库
```

 - 2 chromedriver安装

chromedriver官网地址: http://chromedriver.storage.googleapis.com/index.html 
选择合适的版本安装,解压,把解压的文件放入/usr/bin/目录下即可:

``` nginx
mv chromedriver /usr/bin/
```

 - python下测试chromedriver:
``` stylus
from selenium import webdriver  # 引入驱动对象
driver = webdriver.Chrome()  　# 生成谷歌浏览器对象
driver.get('http://www.baidu.com')  #访问百度
```
**重点：**
 - **selenium的语法**
 

``` stylus
　　 send_keys() :在input输入框内输入内容
　　 click(): 模仿鼠标点击
 　　page_source: 当前页面的网页html源码
```
**博客地址：**[enter description here](https://blog.csdn.net/mini_panda/article/details/80725187)