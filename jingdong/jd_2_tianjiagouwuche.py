#coding=utf-8
import time
import unittest
import jd_0_dl
from jd_0_dl import wait
from selenium.webdriver.common.by import By
from zhuangshiqi import retry

class Gouwutian(unittest.TestCase):
    "添加商品到购物车"
    @retry
    def test_gouwutian(self):
        print 222
        #拿前一个模块jd_1_dl的句柄
        dr=jd_0_dl.dr
        time.sleep(2)
        #点击首页的秒杀链接
        wait(By.XPATH, '//*[@id="navitems-group1"]/li[1]/a')
        dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[1]/a').click()
        #切换窗口，下拉滚条
        dr.switch_to.window(dr.window_handles[1])
        dr.execute_script('window.scrollTo(0,800)')
        time.sleep(2)
        #跳转页面之后，点击可以秒杀的商品//*[@id="super_seckill"]/div/ul/li[2]/a/img
        wait(By.XPATH, '//*[@id="super_seckill"]/div/ul/li[2]/div/a')
        dr.find_element_by_xpath('//*[@id="super_seckill"]/div/ul/li[2]/div/a').click()
        #切换窗口，下拉滚条
        dr.switch_to.window(dr.window_handles[2])
        dr.execute_script('window.scrollTo(0,500);')
        time.sleep(2)
        #点击添加购物车按钮
        wait(By.XPATH, '//*[@id="InitCartUrl"]')
        dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()

















