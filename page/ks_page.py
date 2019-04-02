# coding：utf-8
#author：jiguobin
from base.actionMethod import ActionMethod
class KsPage(ActionMethod):
    def ksIncoming(self,row,sheet=1):
        print(By.LINK_TEXT,By.CLASS_NAME,By.ID)
        data=(dict(zip(self.get_excel_value(0,0), self.get_excel_value(sheet,row-1))))
        print(data)
        self.login_ms(url=data['环境'],name=data['代理商登录账号'],password=data['代理商登录密码'])#登录
        self.click('xpath','//*[@id="togglemenu"]/li[1]/a')   #商户管理
        self.sleep_time(0.5)
        #判断是商户还是门店进件
        if data['商户id']!='':
            self.click('xpath','//*[@id="togglemenu"]/li[1]/ul/li[2]/a')
            self.switch_frame('contframe')
            self.input('id','searchContent',data['商户id'])
            self.click('id','searchContent')
        elif data['门店id']!='':
            self.click('xpath','//*[@id="togglemenu"]/li[1]/ul/li[3]/a')
            self.switch_frame('contframe')
            self.input('id','storeContent',data['门店id'])
            self.click('id','storeContent')
        else:
            print('excel取值不正确')
        self.sleep_time(2)
        self.click('class_name','item') #选中指定商户
        self.click('id','query')        #查找商户
        self.sleep_time(1)
        self.click('id','details')
        self.click('id','addBankConfigureForKS')
        #如果文本中填写了配置名称，那么就清空原有信息，并输入
        if data['配置名称'] =='':
            pass
        else:
            self.clear('id','configureName')
            self.input('id','configureName',data['配置名称'])
        self.click('id','noSelcetPassTypeName')
        self.click('link_text',data['通道名称'])  #选择通道名称
        self.sleep_time(0.5)
        self.click('id','noSelcetAlipayRateName')
        self.click('link_text',data['支付宝商户费率名称'])
        self.click('id','noSelcetWechatRateName')
        self.click('link_text',data['微信商户费率名称'])
        self.input('id','configureRemark',data['配置备注'])
        self.clear('id','fullNameCn')
        self.input('id','fullNameCn',data['商户名称'])
        self.clear('id','nameCn')
        self.input('id','nameCn',data['商户简称'])
        self.click('class_name','tradechoisecont')



    pass


k=KsPage()
k.ksIncoming(4)