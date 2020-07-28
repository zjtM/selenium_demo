from selenium import webdriver

'''
使用CSSselect选择器对元素进行定位
'''
driver = webdriver.Chrome()
driver.get('http://pms.wumis.com/my/')
userName = driver.find_element_by_css_selector('#account')
userName.send_keys('zjt')
pwd = driver.find_element_by_css_selector('.form-control[name=password]')
pwd.send_keys('123456')
driver.quit()

