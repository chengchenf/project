#coding=utf-8
import unittest
from jd_0_dl import denglu
from zhuangshiqi import retry

class Denglu(unittest.TestCase):
    @retry
    def test_denglu(self):
        "登录"
        print 111
        denglu()

















