import unittest #单元测试

#每次新增一个用例，测试资源器都需要刷新一次，才会重新获取新的用例

class MytestCase(unittest.TestCase): #定义测试类，需要继承unittest里的TestCase
    # def setUp(self) -> None:
    #     super().setUp()
    #     print('setUp')

    # def tearDown(self) -> None:
    #     super().tearDown()
    #     print('tearDown')
    '''
    #不使用class的方式，每一个测试用例都会执行一次 setUp和teardown，按写的顺序执行。
    def setUp(self):
        super().setUp()
        print('setup')
    
    def test1(self):
        self.assertEqual(3, 1+2, "第一个参数和第二个参数相等")
        print('test1')
    
    def test2(self):
        self.assertIn(1, [1,2,3])
        print("test2")

    def tearDown(self):
        super().tearDown()
        print('tearDown')
    '''
    #使用class实例化，不会每个测试用例都执行一次setUp和tearDown，按顺序执行
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print('setUpClass')
                                                                          
    def test1(self):
        self.assertEqual(3, 1+2, "第一个参数和第二个参数相等")
        print('test1')

    def test3(self):
        self.assertNotEqual(1, 2+3)
        print('test3')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        print('tearDownClass')