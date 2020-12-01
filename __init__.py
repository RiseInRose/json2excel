# coding:utf-8
# author caturbhuja
# date   2020/11/24 2:43 下午
# wechat chending2012
from json2excel.j2e import Json2Excel

__version__ = '1.0.1'


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


VERSION = tuple(map(int_or_str, __version__.split('.')))

__all__ = [
    'Json2Excel',
]