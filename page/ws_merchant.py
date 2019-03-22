# coding=utf-8
#author：jiguobin
from base.actionMethod import ActionMethod
class WsPage(ActionMethod):
    #共用数据部分
    def __init__(self,id,file_name,sheet,row):
        '''
        :param id: 指定进件的商户id
        :param file_name: 进件用到的数据excel
        :param sheet: excel中的页码
        :param row: excel中的哪行数据
        :data:excel中的数据
        :return:
        '''
        self.id=id
        self.file_name=file_name
        self.sheet=sheet
        self.row=row
        self.data=self.get_excel_value(self.file_name,self.sheet,self.row)

    #商户类型判断添加缺少字段方法
    def ws(self):
        self.Incoming(self.id)
        self.public()

    #网商进件的公共部分
    def public(self):
        print(self.data)
        self.click('id','addBankConfigureForWS')
        self.input('id','configureRemark','ceshi')
        pass


file_name='D:\pythonTest.xlsx'
w=WsPage('EW_N6268478142',file_name,0,1)
w.ws()

