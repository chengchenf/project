#coding=utf-8
import time
import jd_0_config as jd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def denglu():
    "登录"

    global dr
    dr = webdriver.Chrome()
    dr.get('http://www.jd.com')
    dr.maximize_window()
    #点击首页的登录按钮
    wait = WebDriverWait(dr, 20)
    locator = (By.XPATH, '//*[@id="ttbar-login"]/a[1]')
    wait.until(EC.presence_of_element_located(locator), '超时超时')
    dr.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
    #点击登录的方式：选择帐号登录
    wait = WebDriverWait(dr, 20)
    locator = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/a')
    wait.until(EC.presence_of_element_located(locator), '超时超时')
    dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
    wait = WebDriverWait(dr, 20)
    locator = (By.ID, 'loginname')
    wait.until(EC.presence_of_element_located(locator), '超时超时')
    dr.find_element_by_id('loginname').send_keys(jd.username) #输入登录帐号
    wait = WebDriverWait(dr, 20)
    locator = (By.ID, 'nloginpwd')
    wait.until(EC.presence_of_element_located(locator), '超时超时')
    dr.find_element_by_id('nloginpwd').send_keys(jd.passwd) #输入登录密码
    wait = WebDriverWait(dr, 20)
    locator = (By.ID, 'loginsubmit')
    wait.until(EC.presence_of_element_located(locator), '超时超时')
    dr.find_element_by_id('loginsubmit').click() #点击登录按钮
    time.sleep(7) #在7秒之内，进行滑动验证


def wait(args, elem):
    "显式等待"

    # 等待元素出现
    wait = WebDriverWait(dr, 20)
    locator = (args, elem)
    wait.until(EC.presence_of_element_located(locator), '超时超时')


















