# /usr/bin/env python
# coding:utf-8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "XVV7N17A25000859"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["platformVersion"] = "6.0"
caps["autoGrantPermissions"] = "true"


driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
'''
def always_allow(driver, number=5):

    for i in range(number):
        loc = ("xpath", "//*[@text='始终允许']")
        try:
            e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except:
            pass

if __name__ == "__main__":
    always_allow(driver)
'''
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
driver.implicitly_wait(10)
el3 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn")
el3.click()
'''
def always_allow(driver, number=2):

    for i in range(number):
        loc = ("xpath", "//*[@text='下次再说']")
        try:
            e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except:
            pass

if __name__ == "__main__":
    always_allow(driver)
'''
#driver.quit()