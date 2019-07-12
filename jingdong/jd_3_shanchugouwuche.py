#coding=utf-8
import time
import unittest
import jd_0_dl
from jd_0_dl import wait
from selenium.webdriver.common.by import By
from zhuangshiqi import retry

class Gouwushan(unittest.TestCase):
    "删除购物车里的商品"
    @retry
    def test_gouwushan(self):
        print 333
        dr=jd_0_dl.dr
        # dr.get('https://www.jd.com/')
        #点击‘我的购物车’按钮
        wait(By.XPATH, '//*[@id="settleup-2014"]/div[1]/a')
        dr.find_element_by_xpath('//*[@id="settleup-2014"]/div[1]/a').click()
        #切换窗口，下拉滚条
        dr.switch_to.window(dr.window_handles[3])
        # dr.execute_script('window.scrollTo(0,1500)')
        #勾选要删除的购物车中商品
        # wait(By.XPATH, '//*[@id="product_5075546"]/div[1]/div[1]/div/input')
        # dr.find_element_by_xpath('//*[@id="product_5075546"]/div[1]/div[1]/div/input').click()
        #点击删除按钮
        wait(By.XPATH, '//*[@id="remove_10111726_42748065785_1"]')
        dr.find_element_by_xpath('//*[@id="remove_10111726_42748065785_1"]').click()
        #接收删除框
        wait(By.XPATH, '/html/body/div[8]/div[2]/div/div[2]/a[1]')
        dr.find_element_by_xpath('/html/body/div[9]/div[2]/div/div[2]/a[1]').click()














