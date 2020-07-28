'''
webElement 的方法和属性
属性
tag_name  -->  获取标签名
text      -->  获取文本
size      -->  获取标签大小(height,width)

方法
send_keys() --> 键盘输入
clear() --> 清除输入的数据
click() --> 点击
get_attribute('attribute_name') --> 获取元素属性
is_selected() -->是否被选中
is_enabled() -->是否可用
is_displayed() -->是都隐藏
value_of_css_property('property_name') -->获取css属性
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

ipt = driver.find_element_by_css_selector('#kw')
print(ipt.tag_name)
print(ipt.text)
print(ipt.size)
print(ipt.value_of_css_property('font'))

driver.quit()