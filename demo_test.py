# coding:utf-8
# author caturbhuja
# date   2020/11/24 6:16 下午 
# wechat chending2012 
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
        {
            "student_no": 1003,
            "name": "Jane",
            "score": 100,
            "class": "A-3",
            "rank": 3
        },
        {
            "student_no": 1004,
            "name": "Rone",
            "score": 50,
            "class": "A-3",
            "rank": 4
        },
        {
            "student_no": 1005,
            "name": "Bill",
            "score": 44,
            "class": "A-3",
            "rank": 5
        },
        {
            "student_no": 1006,
            "name": "Lily",
            "score": 81,
            "class": "A-2",
            "rank": 6
        }
    ]
    print(json2excel.run(jsons))
