#coding=utf-8
import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=='__main__':
    baogaopath=r'C:\Users\chen\Desktop\linshi\\'
    shijian=time.strftime('%Y_%m_%d %H_%M_%S')
    baogaoming=baogaopath+shijian+u'report.html'

    #添加测试套件
    dangqianmulu=os.path.abspath('')
    # print dangqianmulu
    testsuit=unittest.defaultTestLoader.discover(dangqianmulu,pattern='jd*.py')
    fp=open(baogaoming,'wb')
    #输出报告
    runner=HTMLTestRunner(stream=fp,title=u'京东自动化测试报告',description=u'win10系统')
    runner.run(testsuit)
    fp.close()































