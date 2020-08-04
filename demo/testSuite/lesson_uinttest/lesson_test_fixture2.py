import unittest
from io import StringIO

class lesson(unittest.TestCase):
    @classmethod #使用装饰器可以值调用一次 setup 和teardown
    def setUpClass(cls):
        cls.f = StringIO()
        print('创建StringIO')
    
    @classmethod
    def tearDownClass(cls):
        s = cls.f.getvalue()
        print('读取stringIO',s)

    def test_case1(self):
        self.f.write('test case 1')
        print('写入 test case 1')

    def test_case2(self):
        self.f.write('test case 2')
        print('写入test case 2')

if __name__ == "__main__":
    unittest.main()