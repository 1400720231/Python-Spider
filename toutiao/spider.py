import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import os
import json
from urllib.request import urlretrieve
from multiprocessing import Pool
from hashlib import md5

# 街拍图片的主页面解析
def get_page_index(offset,keywords):
    data = {'offset':offset,
    'format': 'json',
    'keyword': keywords,
    'autoload': 'true',
    'count': 20,
    'cur_tab': 3,
    'from': 'gallery'}
    params = urlencode(data)
    url = 'https://www.toutiao.com/search_content/?'+params
    try:
        response = requests.get(url)
        if response.status_code ==200:
            data = response.json()
            if data and 'data' in response.text:
                for i in data['data']:
                    # 吧一个页面的所有详情页链接返回生成器
                    yield 'https://www.toutiao.com/a'+i['group_id']
    except ConnectionError:
        print('Error occurred')
        return None


# 处理单个页面详情,找到所有图图片链接
def get_page_detail(url):
    html = requests.get(url).text
    # 正则表达式是这个详情页爬虫的关键
    images_pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    result = re.search(images_pattern, html)
    # print(result)
    # if result:
    data = json.loads(result.group(1).replace('\\', ''))
    if data and 'sub_images' in data.keys():
        sub_images = data.get('sub_images')
        images = [item.get('url') for item in sub_images]
        # for image in images: download_image(image)
        return images

# 下载图片
def download_images(images):
    # file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    for image in images:
        file_path = '/home/padna/env352/Spider_codes/toutiao/'+md5(image.encode('utf8')).hexdigest()+'.jpg'
        urlretrieve(image,file_path)
        


def main(offset):
    urls = get_page_index(offset,'街拍')
    for url in urls:
        # print(url)
        images = get_page_detail(url=url)
        # print(images)
        download_images(images)



if __name__ == '__main__':
    # 线程池
    pool = Pool(4)
    groups = [x * 20 for x in range(0,21)]
    # 映射线程
    pool.map(main, groups)
    pool.close()
    pool.join()