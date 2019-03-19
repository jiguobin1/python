# coding：utf-8
#author：jiguobin
import xlrd
import xlwt
from xlutils.copy import copy

# book = xlrd.open_workbook('D:\pythonTest.xlsx') #打开一个excel
# sheet = book.sheet_by_index(0) #根据顺序获取sheet
# # sheet2 = book.sheet_by_name('2') #根据sheet页名字获取sheet
# print(sheet.cell(1,2).value)  #指定行和列获取数据
# # print(sheet2.cell(0,1).value)
# print(sheet.ncols) #获取excel里面有多少列
# print(sheet.nrows) #获取excel里面有多少行
# l=sheet.row_values(1)#取第几行的数据,如果数据是int类型  转换一下
# print(' '.join([str(x) for x in l]))
# print(sheet.col_values(1)) #取第几列的数据
# #获取excel中所有的数据
# for i in range(sheet.nrows): # 获取excel中有多少行
#     print(sheet.row_values(i))
    # print(' '.join([str(x) for x in sheet.row_values(i)])) #转换str
#--------------------------------------------------------------------


# book = xlwt.Workbook()  #新建一个excel
# sheet = book.add_sheet('sheet1')  #添加一个sheet页
# sheet.write(0,0,'姓名')#一行一行写入
# sheet.write(0,1,'性别')
# sheet.write(0,2,'年龄')
# book.save('D:\pythonExcel.xls') #微软的office不能用xlsx结尾的，wps随意


# stus = [
#       ['姓名','年龄','性别','分数'],
#        ['mary', 20, '女', 89.9],
#       ['mary', 20, '女', 89.9],
#       ['mary', 20, '女', 89.9],
#       ['mary', 20, '女', 89.9]
#         ]
# book = xlwt.Workbook()  #新建一个excel
# sheet = book.add_sheet('info')  #添加一个sheet页
# raw=0
# for stu in stus:
#     col=0
#     for s in stu:
#         sheet.write(raw,col,s)
#         col+=1
#     raw+=1
# book.save('D:\Excel.xls')
#--------------------------------------------------------------------



book1 = xlrd.open_workbook('D:\Excel.xls')
book2 = copy(book1)  #拷贝一份原来的excel
sheet = book2.get_sheet(0) #获取第几个sheet页
sheet.write(1,3,0)#写入需要修改的行、列及修改后的值
sheet.write(1,0,'小黑')
book2.save('D:\Excel.xls')



