#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
from selenium import webdriver

req_url = "http://erp.jd.com"


browser = webdriver.Chrome()
print "Visit %s ..." %(req_url)
browser.get(req_url)

time.sleep(3)

browser.find_element_by_id("username").send_keys("zhukun22")
browser.find_element_by_id("password").send_keys("Zk6238475!@#")
browser.find_element_by_class_name("formsubmit_btn").click()

time.sleep(3)

browser.close()
browser.quit()

#if __name__ == '__main__':