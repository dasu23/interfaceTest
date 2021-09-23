import unittest
import decimal
from common.DataProcess import DataProcess
from config.configHttp import basedata

dataProcess = DataProcess();

class AssertTest(unittest.TestCase):

    def __init__(self,  methodName='runTest'):
        super(AssertTest, self).__init__(methodName)
        self._testMethodName = methodName
        self.flag = 0
        self.failmsg = []

    def checkTestResult(self):
        """获取用例执行结果，断言flag是否为0，不为0说明测试用例中存在断言失败"""
        return self.assertEqual(self.flag, 0, "断言错误，测试失败："+str(self.failmsg))

    # 断言是否相等
    def verifyEqual(self, exp, act, msg=None):
        try:
            self.assertEqual(exp, act, msg)
            return True
        except Exception as e:
            failmsg = basedata.get_nowtime(),": verifyEqual期待结果不相等:【"+ str(exp)+ "】不等于【"+ str(act)+ "】...备注："+ str(msg)
            self.flag += 1
            self.failmsg.append(failmsg)
            print(failmsg)
            return False

    # 断言是否不相等
    def verifyNotEqual(self, exp, act, msg=None):
        try:
            self.assertNotEqual(exp, act)
            return True
        except Exception as e:
            failmsg = basedata.get_nowtime(),": verifyEqual期待结果不相等:【"+ str(exp)+ "】不等于【"+ str(act)+ "】...备注："+ str(msg)
            self.flag += 1
            self.failmsg.append(failmsg)
            print(failmsg)
            return False

    # 断言是否为True
    def verifyTrue(self, act, msg=None):
        try:
            self.assertTrue(act)
            return True
        except Exception as e:
            failmsg = basedata.get_nowtime(),": verifyTrue断言结果不为True:【" + str(act)+ "】...备注："+ str(msg)
            self.flag += 1
            self.failmsg.append(failmsg)
            print(failmsg)
            return False

    # 断言是否为False
    def verifyFalse(self, act, msg=None):
        try:
            self.assertFalse(act)
            return True
        except Exception as e:
            failmsg = basedata.get_nowtime(),": verifyFalse断言结果不为False（错误）:【"+ str(act)+ "】...备注："+ str(msg)
            self.flag += 1
            self.failmsg.append(failmsg)
            print(failmsg)
            return False

    # 断言是否为空
    def verifyIsNone(self, act, msg=None):
        try:
            self.assertIsNone(act)
            return True
        except Exception as e:
            failmsg = basedata.get_nowtime(),": verifyIsNone期待结果不为空:【"+ str(act)+ "】...备注："+ str(msg)
            self.flag += 1
            self.failmsg.append(failmsg)
            print(failmsg)
            return False

    # 断言是否不为空
    def verifyIsNotNone(self, act, msg=None):
        try:
            self.assertIsNotNone(act)
            return True
        except Exception as e:
            failmsg = basedata.get_nowtime(),": verifyIsNotNone期待结果为空（无措）:【"+ str(act)+ "】...备注："+ str(msg)
            self.flag += 1
            self.failmsg.append(failmsg)
            print(failmsg)
            return False

    # 断言是否包含
    def verifyIn(self, exp, act, msg=None):
        try:
            self.assertIn(exp, act)
            return True
        except Exception as e:
            failmsg = basedata.get_nowtime(),": verifyIn期待结果不包含:【"+ str(exp)+ "】不包含【"+ str(act)+ "】...备注："+ str(msg)
            self.flag += 1
            self.failmsg.append(failmsg)
            print(failmsg)
            return False

    # 断言是否不包含
    def verifyNotIn(self, exp, act, msg=None):
        try:
            self.assertIn(exp, act)
            return True
        except Exception as e:
            failmsg = basedata.get_nowtime(),": verifyIn期待结果包含（错误）:【"+ str(exp)+ "】包含【"+ str(act)+ "】...备注："+ str(msg)
            self.flag += 1
            self.failmsg.append(failmsg)
            print(failmsg)
            return False




    # ------------------------------------ 根据指定路径对象对比2组数据 ------------------------------------
    # 根据对比路径进行匹配对比
    # 路径格式：
    # pythonPathDict = {"['info'][0]['Uid']": "['name222']","['info']['stuName']":"['info'][stuName]"}
    def contrastByPythonPath(self, pythonPathDict, expectedJson, actualJson):
        print(basedata.get_nowtime(), ':', "-------------------------------- 对比开始 --------------------------------")
        assFlag = True;
        # 根据对比路径进行对比断言
        for k, v in pythonPathDict.items():
            try:
                # str拼装转换表达式，转换为expectedJson['info']['Uid']
                expected = eval('expectedJson' + k);
                actual = eval('actualJson' + v);
            except:
                print(basedata.get_nowtime(),": 路径错误，期待结果key：" + str(k) + "，实际结果key：" + str(v))
                assFlag = False;

            # 判断期待结果或实际结果是否为空
            # 过滤不同类型的空导致的误报错
            msg = "对比错误，期待结果key：" + str(k) + "，实际结果key：" + str(v)
            if dataProcess.isempty(expected) and dataProcess.isempty(actual):
                pass

            # 判断期待结果或实际结果是否为时间格式，
            # 转为16位长度str格式进行比较
            elif basedata.isVaildDate(expected) or basedata.isVaildDate(actual):
                result = self.verifyEqual(str(expected)[0:16], str(actual)[0:16], msg)
                # 如果断言结果为失败，则打标签结果为失败
                if result == False:
                    assFlag = False

            # 判断期待结果或实际结果类型是否相等
            elif type(expected) != type(actual):
                # 判断是否为decimal类型，清除末尾小数0
                if type(expected) is decimal.Decimal or type(actual) is decimal.Decimal:
                    expected = dataProcess.remove_exponent(expected)
                    actual = dataProcess.remove_exponent(actual)
                # 如果不相等则都转换为str类型之后在进行对比
                result = self.verifyEqual(dataProcess.change2str(expected), dataProcess.change2str(actual), msg)
                if result == False:
                    assFlag = False
            else:
                result = self.verifyEqual(expected, actual, msg)
                if result == False:
                    assFlag = False

        print(basedata.get_nowtime(), ':', "-------------------------------- 对比结束 --------------------------------")
        return assFlag;



    # 根据对比路径进行匹配对比
    # 路径格式：
    # {"info.Uid": "name222", "info.stuName": "info.stuName2"}
    def contrast(self, jsonPathDict, expectedJson, actualJson):

        pythonPathDict = dataProcess.replacepathjson(jsonPathDict);
        return self.contrastByPythonPath(pythonPathDict, expectedJson, actualJson)





    # ------------------------------------ 对比2组数据 ------------------------------------
    # 以期待结果为标准进行对比
    # 期待结果有，实际结果中没有路径报错；反之不报错
    # （只支持单层结构json，不支持多层结构json）
    def contrastByExpected(self, expected, actual):

        pathjson = dataProcess.composepathjson(expected);
        return self.contrast(pathjson,expected, actual)

    # 以实际结果为标准进行对比
    def contrastByActual(self, expected, actual):

        pathjson = dataProcess.composepathjson(actual);
        return self.contrast(pathjson,expected, actual)



if __name__ == '__main__':
    a = {"a": 1}
    a = {"a": 2}
