#coding=utf-8
import shijian
from selenium import webdriver

#清除浏览器缓存
dr=webdriver.Chrome()
dr.get('http://www.baidu.com')

dr.get('chrome://settings/clearBrowserData')
dr.maximize_window()
shijian.sleep(2)
#定义js执行代码
# js_script='$("#clearBrowsingDataConfirm")[0].click()'
js_script='$("#clearBrowsingDataDialog")[0]'
shijian.sleep(5)
dr.execute_script(js_script)


# widow=dr.window_handles
# print widow
# current_window = dr.current_window_handle
# print current_window
# dr.find_element_by_id('clearBrowsingDataConfirm').click()
# dr.switch_to_default_content()
# dr.find_element_by_xpath('//*[@id="clearBrowsingDataConfirm"]').is_displayed()



















