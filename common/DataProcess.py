import re


class DataProcess():


    # ------------------------------------ 数据处理 ------------------------------------
    # 转换路径
    # 转换为python可识别的json路径
    # 将【Data.Shoppingcarts.Sellers[0].Products[0].LinkUrl】转换为【['Shoppingcarts']['Sellers'][0]['Products'][0]['Title']】
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



    # 判断instr是否存在于allstr中
    # time_letter = [":", "."]
    # if self.hasinstr(time_letter, date):
    #     print(date)
    def hasinstr(self,instr, allstr):
        flag = False;
        for s in str(allstr):
            if instr.count(s):
                flag = True
        return flag



