# interfaceTest

接口自动化测试框架，可与Jenkins持续集成系统结合。

安装依赖

1.使用Python3

2.pip install -r requirements.txt


目录

.
├── com

│   ├── panli

│   │   └── www

│   │       ├── service

│   │       │   ├── xxx_Service.py  #接口基础封装

│   │       └── testcase

│   │           └── xxx_Testcase.py #测试用例

├── common

│   ├── AssertTest.py               

│   ├── Basedate.py

│   ├── DataContrast.py

│   ├── DataProcess.py

│   ├── DbHandle.py

│   ├── HTMLTestRunner_PY3.py

│   ├── TestRunner.py

│   └── business

│       ├── DataFactory.py

│       ├── DataFactory_fulu.py

│       ├── DataFactory_yg.py

│       ├── OrderContrast.py

│       └── get_token.py

├── sql

│   ├── mysql

│   │   └── panli_order

│   │       └── MySql_TableName.py

│   └── sqlserver

│       ├── panli

│       │   └── Sql_TableName.py

│       └── shoppingcart

├── config

│   ├── casepath_properties.ini

│   ├── configDB.py

│   ├── configEmail.py

│   ├── configHttp.py

│   └── testdata_properties.py

├── Main.py

├── requirements.txt

└── result

