# interfaceTest

接口自动化测试框架，可与Jenkins持续集成系统结合。

安装依赖

1.使用Python3

2.pip install -r requirements.txt


目录

<br> 

**项目结构** 
```

├── com
│   ├── panli
│   │   └── www
│   │       ├── service     #接口封装
│   │       │   ├── xxx_Service.py  
│   │       └── testcase    #测试用例
│   │           └── xxx_Testcase.py
├── common  
│   ├── AssertTest.py       #基础断言封装
│   ├── Basedate.py         #基础数据生成
│   ├── DataContrast.py     #批量对比数据断言封装
│   ├── DataProcess.py      #数据处理方法封装
│   ├── DbHandle.py         #数据库DB封装
│   ├── HTMLTestRunner_PY3.py   
│   ├── TestRunner.py           #测试用例执行入口
│   └── business                #业务相关
│       ├── DataFactory.py
│       ├── DataFactory_fulu.py
│       ├── DataFactory_yg.py
│       ├── OrderContrast.py
│       └── get_token.py
├── sql                     #数据库连接
│   ├── mysql
│   │   └── panli_order
│   │       └── MySql_TableName.py
│   └── sqlserver
│       ├── panli
│       │   └── Sql_TableName.py
│       └── shoppingcart
├── config                  #配置相关
│   ├── casepath_properties.ini
│   ├── configDB.py
│   ├── configEmail.py
│   ├── configHttp.py
│   └── testdata_properties.py
├── Main.py     Jenkins入口
├── requirements.txt
└── result                  #测试报告

```

<br> 
