#!/usr/bin/env python

import configparser
import os
import sys



class ConfigEnv():

    # 获取项目根目录地址
    def getrootpath(self):
        global rootpath
        rootpath = os.getcwd()[0:os.getcwd().rfind('interfaceTest')] + 'interfaceTest'
        sys.path.append(str(rootpath))
        return rootpath

    # 根据文件名，读取config文件
    def getConfigFile(self, filename):
        rootpath = self.getrootpath()
        # 读取测试用例路径配置文件
        cf = configparser.ConfigParser()
        configpath = rootpath + "/config/" + str(filename)
        cf.read(configpath)
        return cf

    # 获取当前环境变量（config/env.ini文件）
    def getEnv(self):
        cf = self.getConfigFile("env.ini");
        env = cf.get("path", 'env')
        return str(env)

    def setEnv(self, newEnv):
        cf = self.getConfigFile('env.ini');
        cf.set('path', 'env', str(newEnv))
        configpath = rootpath + '/config/' + 'env.ini'
        cf.write(open(configpath, "r+", encoding="utf-8"))


if __name__ == '__main__':
    configEnv = ConfigEnv()
    configEnv.setEnv("pro")

