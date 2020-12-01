# coding:utf-8
# author caturbhuja
# date   2020/11/24 4:19 下午 
# wechat chending2012 
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
