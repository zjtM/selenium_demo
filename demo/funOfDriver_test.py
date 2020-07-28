'''
diver的常用方法
driver.refresh()  --> 刷新页面
driver.back()     --> 后退
driver.forward()  -->前进
driver.close()    -->关闭 关闭当前窗口，如果是当前打开的最后一个窗口，则退出浏览器
driver.quit()     -->关闭 退出驱动，关闭所有相关的窗口

driver.switch_to.frame() --> 切换到frame
driver.switch_to.active_element --> 切换到有active的元素
driver.switch_to.alter -->切换到弹窗
driver.switch_to.default_content() -->切换到默认内容
drier.switch_to.window() -->切换到窗口


'''

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

text = driver.find_element_by_css_selector('kw')
text.send_keys('python')

btn = driver.find_element_by_css_selector('su')
btn.click()

sleep(3)
driver.refresh() #刷新页面
sleep(3)
driver.back() #后退
sleep(3)
driver.forward() #前进
sleep(2)
#driver.close() #关闭 关闭当前窗口，如果是当前打开的最后一个窗口，则退出浏览器
driver.quit() #关闭 退出驱动，关闭所有相关的窗口