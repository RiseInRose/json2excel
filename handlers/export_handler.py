# coding:utf-8
# author caturbhuja
# date   2020/11/24 4:05 下午 
# wechat chending2012 
import os
import time
import inspect
from openpyxl import Workbook


class ExportHandler:
    """
    接受参数实例，注意，一定需要转换成这种格式，才能正常保存。
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

    def __init__(self, export_dir=None, head_name_cols=None, **kwargs):
        """
        :param export_dir: 存放文件地址，需要绝对路径
        :param head_name_cols: 自定义表头
        """
        path = os.path.dirname(inspect.stack()[2].filename)
        self._export_dir = export_dir or f"{path}{os.sep}files"
        self._check_path_exist()
        self._wb = Workbook()
        self._ws = self._wb.active
        self._head_name_cols = head_name_cols or list()  # 表头

    def _check_path_exist(self):
        if not os.path.exists(self._export_dir):
            os.mkdir(self._export_dir)

    def __call__(self, data: (list, dict), file_name=None):
        """额， 原本规定，如果只有一条数据，也需要使用 [dict] 这个格式即可。不过最后还是支持， 直接输入dict 也可以"""
        if isinstance(data, list):
            pass
        elif isinstance(data, dict):
            data = [data]
        else:
            raise TypeError(f'not support type {type(data)}')
        self._add_head_name(data)
        for each_dict in data:
            self._add_row(each_dict)
        return self._save(file_name)

    def _add_head_name(self, data: list):
        """确保能拿到所有的 head_name """
        [self._head_name_cols.append(key) for each in data for key in each.keys() if key not in self._head_name_cols]
        self._ws.append(list(self._head_name_cols))  # 添加某一行

    def _add_row(self, dict_):
        row = list()
        for head_name in self._head_name_cols:
            row.append(dict_.get(head_name, ''))
        self._ws.append(row)

    def _save(self, file_name=None):
        file_name = file_name or f"{str(time.time())}.xls"
        file_path = f"{self._export_dir}{os.sep}{file_name}"
        self._wb.save(file_path)
        return file_path
