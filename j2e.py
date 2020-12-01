# coding:utf-8
# author caturbhuja
# date   2020/11/24 2:43 下午 
# wechat chending2012 
import json
import os
from json2excel.handlers.export_handler import ExportHandler
from inspect import isfunction, isclass


class Json2Excel:
    """"""

    def __init__(self, format_handler=None, export_handler=ExportHandler, export_dir='', head_name_cols=None, **kwargs):
        """
        :param format_handler:  自定义格式转换器，把格式转换成预定格式如下。
            format_handler 要求转出文件格式：
            接受参数实例，注意，一定需要转换成这种格式[dict, dict ....]，才能正常工作。
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
        :param export_handler:  保存文件参数。支持自定义
        :param export_dir: 存放文件地址，需要绝对路径
        :param head_name_cols: list 指定 excel 表头参数排列顺序
        """
        def check_handler_type(handler):
            if handler is not None:
                if isfunction(handler):
                    new_handler = handler
                elif isclass(handler):
                    new_handler = handler(**kwargs)
                else:
                    raise TypeError(f"not support handler type:{type(handler)}")
            else:
                new_handler = None
            return new_handler

        self._format_handler = check_handler_type(format_handler)
        self._export_handler = export_handler(export_dir, head_name_cols, **kwargs)

    @staticmethod
    def _format_prepare(data) -> dict:
        """如果传入是路径，则解析出数据
        warning: 如果传入是路径， 一定需要有路径分割符，例如：./test.json，否则可能导致解析报错
        """
        if isinstance(data, str):
            if os.sep in data:
                with open(data, 'r') as f:
                    data = f.read()
            data = json.loads(data)
        return data

    def run(self, data, file_name=None):
        """
        :param data: dict or path or str
        :param file_name:
        data_list: [dict, dict]
        """
        data_list = self._format_prepare(data)
        if self._format_handler is not None:
            data_list = self._format_handler(data_list)
        file_path = self._export_handler(data_list, file_name)
        return file_path
