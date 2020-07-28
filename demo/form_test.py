from selenium import webdriver
from time import sleep
import random 
import string
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://www.sahitest.com/demo/formTest.htm')

sleep(3)

#弹窗

'''
switch_to.alert  切换到alert弹窗
1.text：返回alert/confirm/prompt中的文字信息。
2.accept()：接受现有警告框。
3.dismiss()：解散现有警告框。
4.send_keys(keysToSend)：发送文本至警告框。 keysToSend：将文本发送至警告框。
'''
alert = driver.switch_to.alert #切换到alert弹窗
alert.accept() # 确认弹窗


#表单输入框
inputs = driver.find_elements_by_css_selector('table input')

letters = string.ascii_letters
i = 0
letter = ''

#每个可用输入框随机输入3个字母
for item in inputs:
    # num = random.randint(0,10)
    # if item.get_attribute('disabled') or item.get_attribute('readonly'): 
    #     continue 
    # item.send_keys(num)
    if item.get_attribute('disabled') or item.get_attribute('readonly'): 
        continue 
    while i < 3:
        letter += random.choice(letters)
        i += 1
    item.send_keys(letter)
    letter = "" #清空输入内容，否则会叠加
    i = 0 #计数需要初始化，不然二次循环会直接跳出



#多选框
check_boxs = driver.find_elements_by_css_selector('input[type=checkbox]')

#is_selected 查询元素是否选中
# 取消最后一个选中
#driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

#随机勾选
for check, index in enumerate(check_boxs):
    length = +len(check_boxs)
    num = random.randint(0,length-1)
    print(num)
    if check_boxs[num].is_selected():
        continue
    else:
        check_boxs[num].click()


#单选框
#判断是否选中 is_selected
radios_list = driver.find_elements_by_name('r1')
for radio in radios_list:
    if radio.get_attribute('value') == 'rv2':
        radio.click()


sleep(3)

driver.quit()