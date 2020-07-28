import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from lib import HTMLTestRunner

class SuitTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        #初始化
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    
    def test1(self):
        ipt = self.driver.find_element_by_id('kw')
        ipt.send_keys('禅道')
        btn = self.driver.find_element_by_id('su')
        ActionChains(self.driver).click(btn).perform()
    
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()        

class SuitTest2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    
    def test2(self):
        test = self.driver.find_element_by_id("kw")
        test.send_keys('translate')
        btn = self.driver.find_element_by_id('su')
        ActionChains(self.driver).click(btn).perform()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()   

if __name__ == "__main__":
    # test1 = unittest.TestLoader.loadTestsFromTestCase(SuitTest1)
    # test2 = unittest.TestLoader.loadTestsFromTestCase(SuitTest2)

    # unittest.TestSuite.run([test1,test2])

    TestSuite = unittest.TestSuite() #实例化测试套件
    TestSuite.addTests([SuitTest1('test1'), SuitTest2('test2')]) 
    fp = open(r"./selenium_demo/result.html","wb") #创建测试报告
    #unittest.TextTestRunner(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试') #输出测试报告
    runner.run(TestSuite)