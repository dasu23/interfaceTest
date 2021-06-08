import unittest

from config.configHttp import basedata


class AssertTest(unittest.TestCase):

    # 断言是否相等
    def verifyEqual(self, exp, act, msg=None):
        try:
            self.assertEqual(exp, act, msg)
            return True
        except Exception as e:
            print(basedata.get_nowtime(),": verifyEqual期待结果不相等:【"+ str(exp)+ "】不等于【"+ str(act)+ "】...备注："+ str(msg))
            return False

    # 断言是否不相等
    def verifyNotEqual(self, exp, act, msg=None):
        try:
            self.assertNotEqual(exp, act)
            return True
        except Exception as e:
            print(basedata.get_nowtime(),": verifyNotEqual断言结果相等（错误）:【" + str(exp) + "】等于【" + str(act) + "】...备注：" + str(msg))
            return False

    # 断言是否为True
    def verifyTrue(self, act, msg=None):
        try:
            self.assertTrue(act)
            return True
        except Exception as e:
            print(basedata.get_nowtime(),": verifyTrue断言结果不为True:【" + str(act)+ "】...备注："+ str(msg))
            return False

    # 断言是否为False
    def verifyFalse(self, act, msg=None):
        try:
            self.assertFalse(act)
            return True
        except Exception as e:
            print(basedata.get_nowtime(),": verifyFalse断言结果不为False（错误）:【"+ str(act)+ "】...备注："+ str(msg))
            return False

    # 断言是否为空
    def verifyIsNone(self, act, msg=None):
        try:
            self.assertIsNone(act)
            return True
        except Exception as e:
            print(basedata.get_nowtime(),": verifyIsNone期待结果不为空:【"+ str(act)+ "】...备注："+ str(msg))
            return False

    # 断言是否不为空
    def verifyIsNotNone(self, act, msg=None):
        try:
            self.assertIsNotNone(act)
            return True
        except Exception as e:
            print(basedata.get_nowtime(),": verifyIsNotNone期待结果为空（无措）:【"+ str(act)+ "】...备注："+ str(msg))
            return False

    # 断言是否包含
    def verifyIn(self, exp, act, msg=None):
        try:
            self.assertIn(exp, act)
            return True
        except Exception as e:
            print(basedata.get_nowtime(),": verifyIn期待结果不包含:【"+ str(exp)+ "】不包含【"+ str(act)+ "】...备注："+ str(msg))
            return False

    # 断言是否不包含
    def verifyNotIn(self, exp, act, msg=None):
        try:
            self.assertIn(exp, act)
            return True
        except Exception as e:
            print(basedata.get_nowtime(),": verifyIn期待结果包含（错误）:【"+ str(exp)+ "】包含【"+ str(act)+ "】...备注："+ str(msg))
            return False




if __name__ == "__main__":
    assertTest = AssertTest();
    a = assertTest.verifyEqual(1, 1)
    b = assertTest.verifyEqual(1, 3)
    print(a)
    print(b)