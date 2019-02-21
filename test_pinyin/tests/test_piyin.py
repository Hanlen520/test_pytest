# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 15:44
# @Author  : WangJuan
# @File    : test_piyin.py

import pytest
from xpinyin import Pinyin

p = Pinyin()

print(p.get_initial("国"))
print(p.get_initials("国家", '+'))


def test_get_pinyin():
    pytest.assume(p.get_pinyin() == 'ni-hao')
    pytest.assume(p.get_pinyin("国家") == 'guo-jia')
    pytest.assume(p.get_pinyin("123") == '123')

    pytest.assume(p.get_pinyin("国家", "+") == 'guo+jia')

    pytest.assume(p.get_pinyin("国家", "", "", "capitalize") == 'GuoJia')
    pytest.assume(p.get_pinyin("国家", "", "", "upper") == 'GUOJIA')

    pytest.assume(p.get_pinyin("国家", "", "numbers", "lower") == 'guo2jia1')
    pytest.assume(p.get_pinyin("国家", "", "marks", "lower") == 'guójiā')

    pytest.assume(p.get_pinyin("国家", "+", "numbers", "capitalize") == 'Guo2+Jia1')
    pytest.assume(p.get_pinyin("国家", "+", "marks", "upper") == 'GUÓ+JIĀ')


def test_get_initial():

    pytest.assume(p.get_initial("你") == 'N')
    pytest.assume(p.get_initial("1") == '1')


def test_get_initials():
    print(p.get_initials(""))

    pytest.assume(p.get_initials("你好") == 'N-H')

    pytest.assume(p.get_initials("123") == '1-2-3')
    pytest.assume(p.get_initials("国家", "+") == 'G+J')

