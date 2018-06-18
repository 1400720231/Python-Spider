#coding:utf-8
import re
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 谷歌浏览器驱动对象
browser = webdriver.Chrome()
# selenium和PhantomJS分手了，现在可以用无头浏览器FireFox或者Chrome代替
# browser = webdriver.PhantomJS()
wait = WebDriverWait(browser, 10)


def search():
	try:
		browser.get('https://www.taobao.com/')
		# 等待10秒直到找到輸入框  通過css选择器语法来实现
		input_button = wait.until(
		    EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
		)
		# 等待10秒直到找到搜索按钮  通過css选择器语法来实现
		submmit = wait.until(
		    EC.presence_of_element_located((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"))
		    )
		# 用send_keys()方法輸入"美食"
		input_button.send_keys('美食')
		# 用click()方法点击搜索按钮
		submmit.click()
		# 关键词搜索出来在淘宝中的页数
		total = wait.until( EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total"))
		)
		return total.text
	# timeout报错 递归调用自己
	except TimeoutException:
		return search()


# 翻页函数
def next_page(page_number):
	try:
		# 等待10秒直到找到輸入框  通過css选择器语法来实现
		# 淘宝返回页下面的跳转的输入框: 第 [1] 页
		input_button = wait.until(
		    EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
		)
		# 等待10秒直到找到搜索按钮  通過css选择器语法来实现
		#　淘宝返回页下面的跳转按钮：第 [1] 页　确认
		submmit = wait.until(
		    EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
		    )
		# 清楚内容
		input_button.clear()
		# 输入跳转页码
		input_button.send_keys(page_number)
		# 点击跳转
		submmit.click()
		# 等待跳转后 高亮的页码数字是不是page_number,一定注意参数((By.CSS_SELECTOR,'css语法'),(text))
		wait.until(
			EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number))
			)
	except TimeoutException:
		next_page(page_number)


# 商品详情解析
def get_products():
	wait.until(
		    EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(1) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew"))
		    )
	res = browser.page_source
	html = BeautifulSoup(res, 'html.parser')
	# 每个上坪详情列表结果
	items= html.find_all('div',{'class':'ctx-box J_MouseEneterLeave J_IconMoreNew'})
	for item in items:
		print({
			'price':item.find('div',{'class':'price g_price g_price-highlight'}).find('strong').string,
			'pay_nums':item.find('div',{'class':'deal-cnt'}).string,
			'name':item.find('div',{'class':'row row-2 title'}).find('a').get_text().replace('\n','').replace(' ',''),
			'location':item.find('div',{'class':'location'}).string

			})


# 主函数
def main():
	total = search()
	#　返回的是字符串，正则匹配返回页码数字
	total = int(re.compile('(\d+)').search(total).group(1))
	# print(type(total))
	for i in range(2,total+1):
		get_products()
		next_page(i)



if __name__ == '__main__':
	main()