# '''
# 界面自动化测试
# 框架 selenium
# 需要浏览器驱动 
# '''
# from selenium import webdriver

# #实例化浏览器驱动
# #driver = webdriver.Chrome() #
# driver = webdriver.Firefox()
# #driver = webdriver.Ie() #使用ie驱动打开ie浏览器，需要将浏览器的保护模式配置成一致的（都启用或者都禁用）
# #打开浏览器及网站
# driver.get('http://wcrmmanagement.weixin.wuerp.com/Login/Index')
# #selenium 定位元素的方法
# '''
# driver.find_element(s)_by_id() ---> 通过元素id进行定位
# driver.find_element(s)_by_class_name() --->通过元素className进行定位
# driver.find_element(s)_by_name() --->通过元素name进行定位
# driver.find_element(s)_by_tag_name() ---> 通过元素标签名定位
# driver.find_element(s)_by_link_text() ---> 文字链接定位
# driver.find_element(s)_by_partial_link_text() ---> 文字链接定位（模糊查询）
# dirver.find_element(s)_by_xpath() ---> 使用xpath定位元素
# driver.find_element(s)_by_css_selector() ---> 通过css选择器进行定位
# '''


from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

input_element = driver.find_element_by_id('kw')
input_element.send_keys('test')
driver.quit()