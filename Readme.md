[TOC]

### 介绍
json 转换成 excel 满足 报表业务需求，支持python3.6 +  

为什么需要这个模块：  

    1. 很方便的把json文件，转换成需要的excel
    2. 可能，真的很优雅。

注意：作者仅提供使用，作生产使用前，请自行测试。年轻人，望好自为之。
### 好的功能
    1. 简单，易用

### 安装方法    

    pip install json2excel

### 调用案例  
```python
from json2excel import Json2Excel

if __name__ == '__main__':
    json2excel = Json2Excel(head_name_cols=["rank", "name"])
    # print(json2excel.run('./test.json'))

    jsons = [
        {
            "student_no": 1001,
            "name": "James",
            "score": 10,
            "class": "A-1",
            "rank": 1
        },
        {
            "student_no": 1002,
            "name": "Tome",
            "score": 91,
            "class": "A-1",
            "rank": 2
        },
    ]
    print(json2excel.run(jsons))


```  

### 参数介绍
#### json2excel 控制参数  
```
    format_handler  非必须 function/class  自定义json格式化函数，强烈推荐自定义    
    export_handler  非必须 class           自定义json输出成excel函数，一般不需要修改    
    export_dir      非必须 str             文件输出 **绝对** 路径，推荐自定义    
    head_name_cols  非必须 list            自定义excel表头排序，推荐自定义    
    kwargs          非必须 空              其他参数    
```

### 自定义json转换函数说明  
FormatHandler 可以是 类，或者函数。最重要的是把数据转换成如下格式。  
```python
"""
输出目标格式：
注意，一定需要转换成这种格式，才能正常保存。
    [
        {
            "student_no": 1001,
            "name": "James",
            "score": 10,
            "class": "A-1",
            "rank": 1
        },
        {
            "student_no": 1002,
            "name": "Tome",
            "score": 91,
            "class": "A-1",
            "rank": 2
        },
    ]
"""
class FormatHandler:
    def __init__(self, **kwargs):
        """"""

    def __call__(self, data_list: (list, dict)):
        """"""
```

### todo


### 感谢

    感谢的人很多，我只不过在原本日志上做封装
    