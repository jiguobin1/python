# coding：utf-8
#author：jiguobin
import random
import string

print(random.choice(['a','b','c','df']))#随机取一个集合中的元素
res = random.sample(string.digits,3) #随机取3个数字元素,返回一个列表
print(''.join(res))   #讲列表转为str

print(random.randint(1,199))#1-199随机取一个整数
print(random.uniform(1,9))#随机取1-9之间的浮点数
print(round(8.842111571877215,2))
print(random.random()) #取0-1之间随机小数
s = ['a','b','c','d','e']
random.shuffle(s) #洗牌，打乱顺序，只能传list
print(s)