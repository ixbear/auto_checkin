#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
from selenium import webdriver

req_url = "http://www.baidu.com"


browser = webdriver.Chrome()
print "Visit %s ..." %(req_url)
browser.get(req_url)

time.sleep(5)
browser.close()
browser.quit()

#if __name__ == '__main__':