import unittest
from lesson_uinttest.lesson_test_fixtuer1 import lesson

'''
使用makeSuite（）把类下的所有测试方法加载在测试套件中。
以包的形式引入
'''
suite = unittest.TestSuite(unittest.makeSuite(lesson))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)