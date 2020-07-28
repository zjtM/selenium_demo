#xpath 定位元素
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

'''
xpath 快速使用方法 检查元素 --> 直接copy xpath路径
'''
e = driver.find_element_by_xpath('//*[@id="kw"]')

driver.quit()