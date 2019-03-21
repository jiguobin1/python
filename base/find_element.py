#coding=utf-8
#author：jiguobin
'''
定位元素封装
'''
from util.read_ini import ReadIni
from selenium import webdriver


class FindElement(object):
    def __init__(self,driver):
        self.driver=driver
    #定位元素
    def get_element(self,node,key):
        read_ini=ReadIni(node=node)
        data=read_ini.get_value(key)
        by=data.split('>')[0]   #定位方式
        value=data.split('>')[1]  #定位值
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by =='className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'text':
                return self.driver.find_element_by_link_text(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None

# d=webdriver.Chrome()
# d.get('http://192.168.19.103:8000/ms/login.in')
# f=FindElement(d)
# print(f.get_element('LoginElement','submit'))


