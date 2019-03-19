# coding：utf-8
#author：jiguobin
import sys
print(sys.path) #环境变量
print(sys.platform) #看当前系统是什么
print(sys.version)#看python的版本
val = sys.stdin.readline()[:-1]  #获取输入的值
print(val)