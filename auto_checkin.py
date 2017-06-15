#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
from random import randint
from selenium import webdriver


a = randint(10,1680)    #random from 10s to 28minute
print("Sleeping " + str(a) + " seconds...")
time.sleep(a)

req_url = "http://jdwe.jd.com/"

browser = webdriver.Chrome()
print "Visit %s ..." %(req_url)
browser.get(req_url)

browser.find_element_by_id("username").send_keys("zhukun22")
browser.find_element_by_id("password").send_keys("Zk6238475*()")
browser.find_element_by_class_name("formsubmit_btn").click()

time.sleep(2)
#browser.find_element_by_class_name("step_close").click()
def isElementExist(element):
  flag=True
  try:
    browser.find_element_by_class_name(element)
    return flag
  except:
    flag=False
    return flag


if isElementExist("step_close"): 
  browser.find_element_by_class_name("step_close").click()

browser.find_element_by_id("clockLink").click()

time.sleep(3)

browser.close()
browser.quit()

#if __name__ == '__main__':
