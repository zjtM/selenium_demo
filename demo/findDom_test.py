#定位元素
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#print(type(driver)) # type() --> 类型查看  type(driver) --> driver

driver.get('http://www.baidu.com')
#el = driver.find_element_by_id("kw") 
#print(type(el)) # --> webelement

'''
find_element find_elements 的区别
find_element 返回符合条件的第一个元素标签
find_elements 以数组的形式返回符合条件的所有元素标签
'''
el = driver.find_element_by_tag_name('input')
els = driver.find_elements(By.TAG_NAME, 'input') 
print(el.get_attribute('name'), el) #get_attribute --> 获取元素标签的属性值
print(len(els)) # len() --> 获取长度

'''
selenium 支持的定位元素的方法
driver.find_element(s)_by_id() ---> 通过元素id进行定位
driver.find_element(s)_by_class_name() --->通过元素className进行定位
driver.find_element(s)_by_name() --->通过元素name进行定位
driver.find_element(s)_by_tag_name() ---> 通过元素标签名定位
driver.find_element(s)_by_link_text() ---> 文字链接定位
driver.find_element(s)_by_partial_link_text() ---> 部分文字链接定位（模糊查询）
dirver.find_element(s)_by_xpath() ---> 使用xpath定位元素
driver.find_element(s)_by_css_selector() ---> 通过css选择器进行定位

以上定位都可以使用类(By)来定位, By需要通过 from selenium.webdriver.common.by import By 引入

find_element(By.ID,"id")
'''
driver.quit()