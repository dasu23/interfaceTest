import decimal
import re



class DataProcess():


    # ------------------------------------ 数据处理 ------------------------------------
    # 转换路径
    # 转换为python可识别的json路径
    # 将【Data.Shoppingcarts.Sellers[0].Products[0].LinkUrl】转换为【['Data']['Shoppingcarts']['Sellers'][0]['Products'][0]['LinkUrl']】
    def replacepath(self, path):
        bb = re.split('[.[\]]', path)
        finalpath = ''
        for cc in bb:
            # 判断是否是数字
            if cc.isdigit():
                dd = '[' + cc + ']'
                finalpath = finalpath + dd;
            # 去空
            elif cc is None or cc == None or cc == '':
                pass
            else:
                dd = '[\'' + cc + '\']'
                finalpath = finalpath + dd;
        return finalpath;


    # 转换json路径
    # {"info.Uid": "name222", "info.stuName": "info.stuName2"}
    # 将上面的路径转换为如下路径
    # {"['info']['Uid']": "['name222']","['info']['stuName']":"['info']['stuName2']"}
    def replacepathjson(self, jsonpath):

        pythonPathDict = {}
        for k, v in jsonpath.items():
            k = self.replacepath(k);
            v = self.replacepath(v);
            pythonPathDict[k] = v

        return pythonPathDict;



    # 将json中的key全部转为小写
    def lower_json(self, json_info):

        if isinstance(json_info, dict):
            for key in list(json_info.keys()):
                if key.islower():
                    self.lower_json(json_info[key])
                else:
                    key_lower = key.lower()
                    json_info[key_lower] = json_info[key]
                    del json_info[key]
                    self.lower_json(json_info[key_lower])

        elif isinstance(json_info, list):
            for item in json_info:
                self.lower_json(item)

        return json_info


    # 根据路径修改json的key
    def change_json_Key(self, path, json_info):
        for k, v in path.items():
            json_info[k] = json_info.pop(v)

        return json_info



    # 判断strparam是否存在于allstr中
    # time_letter = [":", "."]
    # if self.hasinstr(time_letter, date):
    #     print(date)
    def hasinstr(self, strparam, allstr):
        flag = False;
        for s in str(allstr):
            if strparam.count(s):
                flag = True
        return flag


    # 获取json的key，组合kv都为一样的pathjson
    def composepathjson(self,json):
        pathjson = {}
        for k, v in json.items():
            pathjson[k] = k
        return pathjson

    # 如果参数是bytes，则转换为int
    def changebyte2int(self, param):
        if type(param) is bytes:
            param = int.from_bytes(param,'little')
        return param


    #转换类型为str
    def change2str(self, param):
        if type(param) is bytes:
            param = int.from_bytes(param,'little')
        return str(param)


    # 判断参数是否为空
    def isempty(self, param):
        if param is None:
            return True
        elif type(param) is str:
            param = param.strip()
            if ''==param or 'Null'==param or 'NULL'==param or 'null'==param:
                return True
            else:
                return False
        elif type(param) is dict or type(param) is list or type(param) is tuple:
            if len(param) == 0 :
                return True
            else:
                return False
        # 如果参数为0，也判定为null
        elif type(param) is int:
            if param == 0 :
                return True
            else:
                return False
        elif type(param) is bytes:
            if self.changebyte2int(param) == 0 :
                return True
            else:
                return False
        else:
            return False


    # 将python格式的json 转换为 普通json
    def replacejson(self, json):
        strjson = str(json).replace("true", "True").replace("false", "False").replace("null", "None").replace("'", "\"").replace(" ", "")
        return strjson


    # 去除decimal末尾无用小数
    def remove_exponent(self,decimalnum):
        if type(decimalnum) is decimal.Decimal:
            return decimalnum.to_integral() if decimalnum == decimalnum.to_integral() else decimalnum.normalize()
        else:
            return decimalnum




if __name__ == '__main__':
    dataProcess = DataProcess()
    # aa = dataProcess.replacepath("Data.Shoppingcarts.Sellers[0].Products[0].LinkUrl")
    # print(aa)



    time_letter = [":", "."]
    print(dataProcess.hasinstr(time_letter, "2021-09-09 18:02:41.123"))