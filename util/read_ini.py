#coding=utf-8
#author：jiguobin

'''
读取配置文件的封装
'''
#D:\liantuo\seleniumTest\config\LocalElement.ini
# 参数中增添：encoding='UTF-8' 防止（UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 15: illegal multibyte sequence）

import configparser
import os

#基本用法
# cf=configparser.ConfigParser()
# cf.read('D:\liantuo\seleniumTest\config\LocalElement.ini',encoding='UTF-8')  #读取配置文件，直接读取ini文件内容
# print(cf.sections())#获取ini文件内所有的section，以列表形式返回
# print(cf.options("LoginElement"))  #获取指定sections下所有options ，以列表形式返回
# print(cf.items('LoginElement'))    #获取指定section下所有的键值对
# print(cf.get('LoginElement','user_name'))  #获取section中option的值，返回为string类型、

#重构封装
class ReadIni(object):
     # 构造函
    def __init__(self,file_name=None,node=None):
        '''
        :param file_name:配置文件地址
        :param node: 节点名
        '''
        #容错处理
        if file_name == None:
            #默认地址
            file_name = 'D:\liantuo\python\config\element.ini'
        else:
            self.file_name=file_name
        if node == None:
            #默认节点
            self.node = "LoginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf

    #获取value得值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

#
if __name__ == '__main__':
    #自定义
    path=r'E:\Pythonx\seleniumTest\config\testIni.ini'
    read_init = ReadIni(node='menu')   #传入新自定义配置文件地址、节点
    print(read_init.get_value('shanghu'))                   #获取value值
#     #默认
#     read_init = ReadIni()   #默认配置文件地址、节点
#     print(read_init.get_value('user_name'))  #获取value值



