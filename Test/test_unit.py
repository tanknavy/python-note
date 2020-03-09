'''
test-drive develepment
test fixture,test case,test suite, test runner
'''
import unittest
import sys
from Test import test_doc

# 测试方法
class TestMethods(unittest.TestCase):
    def test_equal(self): # 断言测试
        self.assertEqual(1,3-2)
        self.assertEqual(test_doc.cal(3),9) # 方法的返回值断言

    # skip测试skip,skipIf,skipUnless
    @unittest.skipUnless(sys.platform.startswith("win"),"requires windows")
    def test_windows_support(self): # windows下指定测试
        pass

# 被测试的类
class Widget:
    def __init__(self,name):
        self.name = name
        self.x = 50
        self.y=50

    def size(self):
        return self.x,self.y # 返回tuple，immutable不可变

    def resize(self,x,y):
        self.x = x
        self.y = y

# 测试类，包括test fixture
class WidgetTestCase(unittest.TestCase):
    def setUp(self): # 测试方法前准备，在每个测试类调用，还有setUpClass
        self.widget = Widget('The widget')
    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),  'incorrect default size')
    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),'wrong size after resize')
    def tearDown(self): # 每个测试方法后续调用，还有tearDownClass
        del self.widget

# 测试testsuite
def suite():
    test_suite = unittest.TestSuite() # 测试一组TestCase
    test_suite.addTests(WidgetTestCase('test_default_widget_size'),
                                  WidgetTestCase('test_widget_resize'))
    return test_suite

if __name__ == "__main__":
    unittest.main() # 或者如下
    #runner = unittest.TextTestRunner() # test runner
    #runner.run(suite()) # 跑测试runner，收集结果
    # python -m unittest -v TestMethods.py # 命令行测试module,class,method
    # python -m unittest discover # 自动发现测试目标module,class