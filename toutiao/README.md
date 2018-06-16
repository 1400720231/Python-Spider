---
title: 2018-6-16今日头条图片进程爬取 

---

 - ajax请求分析,获取主页面所有详情页链接
 - 对详情页链接html正则匹配出图片链接
 - 下载图片

**关键代码:**

``` if __name__ == '__main__':
    # 线程池
    pool = Pool(4)
    groups = [x * 20 for x in range(0,21)]
    # 映射线程
    pool.map(main, groups)
    pool.close()
    pool.join()
```
