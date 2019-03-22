# coding=utf-8
#author：jiguobin
from base.actionMethod import ActionMethod
class WsPage(ActionMethod):
    #共用数据部分
    def __init__(self,id,sheet,row):
        '''
        :param id: 指定进件的商户id
        :param file_name:这是一个默认参数，可传可不传 进件用到的数据excel
        :param sheet: excel中的页码
        :param row: excel中的哪行数据
        :data:excel中的数据  根据数据中的商户类型决定进什么件
        :return:
        '''
        self.id=id
        self.sheet=sheet
        self.row=row
        self.data=self.get_excel_value(self.sheet,self.row)   #获取excel数据

    #商户类型判断添加缺少字段方法
    def ws(self):
        self.Incoming(self.id)
        self.public()

    #网商进件的公共部分
    def public(self):
        print(self.data)
        self.click('id','addBankConfigureForWS')
        #如果文本中填写了配置名称，那么就清空原有信息，并输入
        if self.data[1] =='':
            pass
        else:
            self.clear('id','configureName')
            self.input('id','configureName',self.data[1])
        self.click('id','noSelcetPassTypeName')
        self.click('link_text',self.data[2])
        self.click('id','noSelcetAlipayRateName')
        self.click('link_text',self.data[3])
        self.click('id','noSelcetWechatRateName')
        self.click('link_text',self.data[4])
        self.input('')
        pass


w=WsPage('EW_N6268478142',0,2)
w.ws()

