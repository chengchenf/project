#coding=utf-8
import time
import traceback
import unittest
import jd_0_dl
from jd_0_dl import denglu

"出错重试的装饰器"
def retry(func):
    def warp(*a,**b):
        for i in range(1,3):
            try:
                func(*a,**b)
            except:
                fl = open('jd_log.txt', 'a')
                if i ==1:
                    print '第一次没有通过，等待3秒重跑'
                    time.sleep(3)
                    traceback.print_exc(file=fl)
                else:
                    print '第二次也没通过'
                    traceback.print_exc(file=fl)
                    dr=jd_0_dl.dr
                    dr.save_screenshot(u'C:\\Users\chen\Desktop\\test000.png')
                    raise Exception('用例重试失败！')

            else:
                print '首次执行通过'
                break
    return warp









































