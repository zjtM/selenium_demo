import unittest
from io import StringIO

#每一个用例执行时，都会调用一次 seup和teardown
class lesson(unittest.TestCase):
    def setUp(self):
        self.f = StringIO()
        print("创建StringIO")

    def tearDown(self):
        s = self.f.getvalue()
        print('读取StringIO：',s)
    
    def test_case1(self):
        self.f.write('test case 1')
        print('写入 test case 1')
    
    def test_case2(self):
        self.f.write('test case 2')
        print('写入 test case 2')

'''
if __name__ == "__main__":
    #直接搜索所有以test开头的测试用例
    #unittest.main() 
    #使用测试套件进行管理
    suite = unittest.TestSuite() #实例化suite
    suite.addTest(lesson('test_case1')) #添加测试用例
    suite.addTest(lesson('test_case2'))
    runner = unittest.TextTestRunner() #实例化执行器
    runner.run(suite) #执行套件
'''