#coding=utf-8
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def retry(func):
    def warp(*a,**b):
        for i in range(1,3):
            try:
                func()
            except:
                # with open('mianshi.txt','w') as f:
                f=open('mianshi.txt','w')
                if i ==1:
                    print '打开一次浏览器'
                    traceback.print_exc(file=f)
                else:
                    print '打开第二次浏览器'
                    traceback.print_exc(file=f)
            else:
                print '打开浏览器成功'
                print i
                f=open('mianshi.txt','w')
                if i ==1:
                    print '打开一次浏览器'
                    traceback.print_exc(file=f)
                else:
                    print '打开第二次浏览器'
                    traceback.print_exc(file=f)
    return warp

@retry
def open_browser():
    dr=webdriver.Chrome()
    dr.maximize_window()
    dr.get('http://www.baidu.com')
    # time.sleep(2)
    # res=dr.find_element_by_id('kw')
    # res.send_keys( u'中国')
    # print res
    wait=WebDriverWait(dr,10)
    loctor=(By.ID,'kw')
    wait.until(EC.presence_of_element_located(loctor),u'chaoshi')
    dr.find_element_by_id('kw').send_keys(u'ni的')

def func1(fun):
    print 111
    fun()
    print 333
    # return fun

@func1
def func2():
    return 222


if __name__ == '__main__':
    # open_browser()
    # func2()
    import unittest
    import os
    from HTMLTestRunner import HTMLTestRunner
    pypath=os.path.dirname(__file__)
    print 000,pypath
    suit=unittest.defaultTestLoader.discover(pypath,pattern='jd*.py')

    report=pypath
    now=time.strftime('%y_%m_%d %H_%M_%S')
    name=pypath+'\\'+now+'report.html'
    f=open(name,'wb')
    runner=HTMLTestRunner(stream=f,title=u'京东')
    runner.run(suit)
#driver.save_screenshot(u'C:\\Users\chen\Desktop\linshi\\test000.png')













