from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import  sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.sahitest.com/demo/selectTest.htm')

#下拉框
'''
需要引入 Select 类
from selenium.webdriver.support.select import Select
下拉框的主要方法
select_by_index(self, index)    　　 #以index属性值来查找匹配的元素并选择；
select_by_value(self, value)        #以value属性值来查找该option并选择；
select_by_visible_text(self, text)  #以text文本值来查找匹配的元素并选择；
first_selected_option(self)         #选择第一个option 选项 ；
'''
#实例化Select
#单选下拉框
sel = driver.find_element_by_css_selector('#s1Id')
Select(sel).select_by_index(1)

#多选 select的 multiple 打开 需要和键盘事件配合使用
mult = Select(driver.find_element_by_id("s4Id"))
mult.select_by_index(2)
print(mult.first_selected_option)


sleep(3)
driver.quit()
