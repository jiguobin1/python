# coding=utf-8
#author：jiguobin
import xlrd
import xlwt
from xlutils.copy import copy
class Ecxel(object):
    def __init__(self,file_name,index):
        self.sheet=self.get_excel(file_name,index)
    def get_excel(self,file_name,index):
        book = xlrd.open_workbook(file_name) #打开一个excel
        sheet = book.sheet_by_index(index) #根据顺序获取sheet
        return sheet
    def get_excel_value(self,row):
        l=self.sheet.row_values(row)
        return l

if __name__ == '__main__':
    file_name='D:\pythonTest.xlsx'
    excel=Ecxel(file_name,0)
    print(excel.get_excel_value(1))
    pass





