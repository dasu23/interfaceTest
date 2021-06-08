import json_tools
import logging
from common.AssertTest import AssertTest
from common.Basedate import Basedata
from common.DataProcess import DataProcess


# 数据处理初始化
from config.configHttp import basedata

basedate = Basedata();
dataProcess = DataProcess();


class DataContrast():


    # ------------------------------------ 数据对比 ------------------------------------
    expecteddict = {
        "difference": []
        , "实际结果增加项": []
        , "实际结果删除项": []
       }

    # 路径、json key名称完全一致对比2个json
    def contrastjson(self, expectedJson, actualJson):
        '''
        :param expectedJson: 期待结果
        :param actualJson: 实际结果
        :return: 对比结果
        '''

        # 先将key全部转为小写
        expectedJson = dataProcess.lower_json(expectedJson)
        actualJson = dataProcess.lower_json(actualJson)

        diffresult = json_tools.diff(expectedJson, actualJson)

        finaldict = {"difference": [], "实际结果增加项": [], "实际结果删除项": []}
        replaceindex = 0;
        addindex = 0;
        removeindex = 0;

        for resultone in diffresult:
            if 'replace' in resultone:
                finaldict['difference'].append(resultone)
                replaceindex + 1
            elif 'add' in resultone:
                # 实际结果中增加了xxx
                finaldict['实际结果增加项'].append(resultone)
                removeindex + 1
            else:
                # 实际结果中删除了xxx（期待结果中多出的字段不做校验）
                finaldict['实际结果删除项'].append(resultone)
                addindex+ 1
        return finaldict


    # 路径、json key名称完全一致对比2个json（
    # V2版，增加remark
    # 如果完全一致返回True，否则返回False & 差异结果
    def contrastjsonV2(self, expectedJson, actualJson, remark = "没有说明备注~"):
        finaldict = self.contrastjson(expectedJson, actualJson)
        if finaldict == self.expecteddict:
            return True,remark
        else:
            return False,remark,finaldict


    # 根据路径替换名称后进行批量对比
    # 路径样式还需要完全一致
    # jsonarry暂时无法替换
    def contrastjsonV3(self, path, expectedJson, actualJson, remark = "没有说明备注~"):

        dataProcess.change_json_Key(path,actualJson)
        return self.contrastjsonV2(expectedJson, actualJson, remark)




    # ------------------------------------ 根据指定路径对象对比2组数据 ------------------------------------
    # 根据对比路径进行匹配对比
    # 路径格式pythonPathDict = {"['info'][0]['Uid']": "['name222']","['info']['stuName']":"['info'][stuName]"}
    def contrastByPythonPath(self, pythonPathDict, expectedJson, actualJson):
        assertTest = AssertTest();
        print(basedate.get_nowtime(), ':', "-------------------------------- 对比开始 --------------------------------")
        assFlag = True;
        try:
            # 根据对比路径进行对比断言
            for k, v in pythonPathDict.items():
                expected = eval('expectedJson' + k);
                actual = eval('actualJson' + v);
                msg = "对比错误，期待结果key：" + str(k) + "，实际结果key：" + str(v)
                # 判断是否是时间，转为19位长度str格式进行比较
                if basedate.isVaildDate(expected) or basedate.isVaildDate(actual):
                    result = assertTest.verifyEqual(str(expected)[0:19], str(actual)[0:19], msg)
                    # 如果断言结果为失败，则打便签结果为失败
                    if result == False:
                        assFlag = False
                else:
                    result = assertTest.verifyEqual(expected, actual, msg)
                    if result == False:
                        assFlag = False
        except:
            print(basedata.get_nowtime(),": 路径错误，期待结果key：" + str(k) + "，实际结果key：" + str(v))
            assFlag = False;
        print(basedate.get_nowtime(), ':', "-------------------------------- 对比结束 --------------------------------")
        return assFlag;



    # 根据对比路径进行匹配对比
    # 路径格式{"info.Uid": "name222", "info.stuName": "info.stuName2"}
    def contrastByJsonPath(self, jsonPathDict, expectedJson, actualJson):

        pythonPathDict = dataProcess.replacepathjson(jsonPathDict);
        return self.contrastByPythonPath(pythonPathDict, expectedJson, actualJson)


    # 测试报告专用
    # 批量断言失败，抛出异常
    def contrastByJsonPathRaise(self, jsonPathDict, expectedJson, actualJson):

        flag = self.contrastByJsonPath(jsonPathDict, expectedJson, actualJson)

        if flag == False:
            raise Exception("批量断言结束，测试用例fail")




if __name__ == '__main__':

    dataContrast = DataContrast();

    dict1 = {"id": "5031", "Name": "A班级优化", "test": "A班级优化", "info": {"Uid": "2017", "stuName": ["张三", "赵五"]}}
    dict2 = {"id": "503", "name222": "A班级优化1", "info": {"uid": "2017", "stuName": ["张三", "赵五"]}}

    # # 路径、名称完全一致对比
    # aa = dataContrast.contrastjsonV2(dict1,dict2,"校验测试")
    # print(aa)
    #
    # # 路径完全一致对比
    # pathdict = {"Name": "name222"}
    # bb = dataContrast.contrastjsonV3(pathdict, dict1, dict2, "校验测试");
    # print(bb)

    pythonPathdict = {"['info']['Uid']": "['name222']","['info']['stuName']":"['info']['stuName2']"}
    jsonPathdict = {"info.Uid": "name222", "info.stuName": "info.stuName2"}

    # dataContrast.contrastByPythonPath(pythonPathdict, dict1, dict2)


    dataContrast.contrastByJsonPath(jsonPathdict, dict1, dict2)


