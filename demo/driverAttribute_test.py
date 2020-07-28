'''
driver的属性值
'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

#print(driver.page_source)
print(driver.current_url) #获取页面的当前地址
print(driver.name)  # 获取浏览器的名称
print(driver.title) #获取当前页面的title值
print(driver.window_handles) #获取浏览器的所有句柄，得到一个数组
print(driver.current_window_handle) #获取当前页面的句柄 
'''
浏览器窗口的属性用句柄（handle）来识别
可以根据句柄来切换窗口页面
'''
driver.quit()