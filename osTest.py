# coding=utf-8
#author：jiguobin
from selenium import webdriver
import os

print(os.name)
print(os.environ)  #在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ.get('PATH'))  #要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.popen('ipconfig').read()) #用来执行操作系统命令,并且获取到返回结果.read
print(os.getcwd()) #取当前工作目录  D:\liantuo\seleniumTest\util
print(os.listdir('d://'))  # 列出一个目录下的所有文件
print(os.path.abspath(__file__))  # 获取绝对路径，能自动识别当前系统  D:\liantuo\seleniumTest\util\osTest.py
print(os.path.dirname("D:\\liantuo\\seleniumTest\\util\\osTest.py"))  # 获取父目录
os.mkdir("D:/test1")  # 创建文件夹
# os.rename("D:/test1", "D:/test2")  # 重命名
print(os.path.exists("d://test2"))  # 目录/文件是否存在
os.remove("D:/test1/d.txt")  # 删除文件,不能删文件夹。
print(os.path.isfile(r"d:\test2"))#判断是否是一个文件 ，r 转译特殊字符，当成普通字符对待（如\t）
print(os.path.isdir(r"d:\test2"))#是否是一个文件夹
os.rmdir("d:/test2")  # 只能删除空文件夹

