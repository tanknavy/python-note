'''
Mock替代或者模拟指定的python对象
MagicMock是Mock的子类，多了一些实现的magic method，
前后端联调：比如前端开发支付页面，根据后端的支付结果，返回成功页，失败页，展示失败页
单元测试：有依赖关系的函数a和b,b需要调用a返回结果作为数据，a已经测试完成
第三方接口：自己写一个mock-server来模拟接口的返回数据
MagicMock比Mock相比多了默认实现的方法
'''
import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

def payment(): # 后端支付功能在开发中，需要返回结果如下
    '''
    支付成功返回：{"result":"success","reason":"null"}
    支付失败返回：{"result":"failed","reason":"insufficient balance"}
    '''
    pass

def payment_status(payment): # 前端展示支付效果
    result = payment() # 前端调用后端支付接口
    print(result)
    try:
        if result["result"] == "success":
            return "success"
        elif result["result"] == "failed":
            print("payment failed: %s"  % result["reason"])
            return "failed"
        else:
            return "unknown payment error"
    except :
        return "unknown server error"

class TestPayment(unittest.TestCase):
    def test_01(self): # 测试支付成功的方法，使用mock模拟功能返回结果
        payment = MagicMock(return_value={"result":"success","reason":"null"})
        status = payment_status(payment)
        print(status)
        self.assertEqual(status,"success")

    def test_02(self): # 测试支付失败的方法
        payment = Mock(return_value={"result":"failed","reason":"insufficient balance"})
        status = payment_status(payment)
        print(status)
        self.assertEqual(status,"failed")

class SomeThing: # 呆开发类
    pass
thing = SomeThing()
thing.method = MagicMock(return_value=3)
thing.method(1,2,3,key='value') # 给类添加未实现功能的返回值
thing.method.assert_called_with(1,2,3,key='value') # mock的方法被调用

if __name__ == "__main__":
    unittest.main()

