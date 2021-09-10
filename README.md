# interfaceTest

接口自动化测试框架，可与Jenkins持续集成系统结合。

**安装依赖** 

1.使用Python3

2.pip install -r requirements.txt

<br> 
**框架特点** 
1.批量断言（DataContrast.py）
  - 支持判断不同类型的空值，比如'',' ',null,NULL,None，int 0，byte 0 ，只有当期待值与实际值都为空是才会断言为True
  - 支持不同数据类型之间的断言，比如decimal与int，string和uuid
  - 时间的断言只精确到分钟，防止接口秒级误差的误报
  - 可通过标记期待结果和实际结果的路径来进行对比，或者两个结构类似的json之间相互对比
  - 案例：
    ```
    expected = {"id": "5031", "Name": "A班级优化", "test": "A班级优化", "info": {"Uid": "2017", "stuName": ["张三", "赵五"]}}
    actual = {"id": "503", "name222": "A班级优化1", "info": {"uid": "2017", "stuName": ["张三", "赵五"]}}
    #设定对比路径
    Pathdict = {"info.Uid": "name222", "info.stuName": "info.stuName2"}
    DataContrast().contrast(pythonPathdict, expected, actual)
    #以期待结果为路径模板进行对比
    DataContrast().contrastByExpected(expected, actual)
    #以实际结果为路径模板进行对比
    DataContrast().contrastByActual(expected, actual)
    ```

<br> 

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
