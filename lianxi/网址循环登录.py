# #coding=utf-8
# filedu=open(u'C:\\Users\chen\Desktop\linshi\网址循环登录文本.txt','r')#文件里网址横着排列
# read1=filedu.read()
# result=chardet.detect(read1)
# print result
# read2=read1.decode('utf16').encode('utf8')
# print read2
# read3=read2.split(',')
# print read3
# for line in read3:
#     from selenium import webdriver
#     dr = webdriver.Chrome()
#     dr.get('http://'+line)
#     dr.maximize_window()
#     time.sleep(2)
#     dr.quit()
import time,chardet
import unittest
from test.shiyanzhuangshiqi import retry
class B():
    # @retry
    def test_chucuochongshi(self):

        try:
            filedu=open(u'C:\\Users\chen\Desktop\linshi\网址循环登录文本1.txt','r')#文件里网址竖着排列
            read1=filedu.read()
            print '以下是read1:','\n',read1
            result=chardet.detect(read1)
            print '文件字符编码是：',result
            read2=read1.decode('utf16').encode('utf8')
            print '以下是read2:','\n',read2
            read3=read2.split('\r\n')
            print read3
            for line in read3:
                print '开始登录的网址是：',lin
                from selenium import webdriver
                dr = webdriver.Chrome()
                dr.get('https://'+line)
                dr.maximize_window()
                time.sleep(2)
                dr.quit()
        # except Exception as e:
        except:
            # print '脚本出错了',e
            print '脚本出错了'
            # raise Exception('脚本出错了')
            # print 11111111111111111111111111111111



if __name__=='__main__':
    t=B()
    t.test_chucuochongshi()





