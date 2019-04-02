# coding：utf-8
#author：jiguobin
from base.actionMethod import ActionMethod
from selenium.webdriver.common.by import By as by
class KsPage(ActionMethod):
    def ksIncoming(self,row,sheet=1):
        data=(dict(zip(self.get_excel_value(sheet,0), self.get_excel_value(sheet,row-1))))
        print(data)
        self.login_ms(url=data['环境'],name=data['代理商登录账号'],password=data['代理商登录密码'])#登录
        self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/a')   #商户管理
        self.sleep_time(0.5)
        #判断是商户还是门店进件
        if data['商户id']!='':
            self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/ul/li[2]/a')
            self.switch_frame('contframe')
            self.input(by.ID,'searchContent',data['商户id'])
            self.click(by.ID,'searchContent')
        elif data['门店id']!='':
            self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/ul/li[3]/a')
            self.switch_frame('contframe')
            self.input(by.ID,'storeContent',data['门店id'])
            self.click(by.ID,'storeContent')
        else:
            print('excel取值不正确')
        self.sleep_time(2)
        self.click(by.CLASS_NAME,'item') #选中指定商户
        self.click(by.ID,'query')        #查找商户
        self.sleep_time(1)
        self.click(by.ID,'details')
        self.click(by.ID,'addBankConfigureForKS')
        #如果文本中填写了配置名称，那么就清空原有信息，并输入
        if data['配置名称'] =='':
            pass
        else:
            self.clear(by.ID,'configureName')
            self.input(by.ID,'configureName',data['配置名称'])
        self.click(by.ID,'noSelcetPassTypeName')
        self.click(by.LINK_TEXT,data['通道名称'])  #选择通道名称
        self.sleep_time(0.5)
        self.click(by.ID,'noSelcetAlipayRateName')
        self.click(by.LINK_TEXT,data['支付宝商户费率名称'])
        self.click(by.ID,'noSelcetWechatRateName')
        self.click(by.LINK_TEXT,data['微信商户费率名称'])
        self.input(by.ID,'configureRemark',data['配置备注'])
        #商户基本信息
        self.clear(by.ID,'fullNameCn')
        self.input(by.ID,'fullNameCn',data['商户名称'])
        self.clear(by.ID,'nameCn')
        self.input(by.ID,'nameCn',data['商户简称'])
        #商户详细信息
        self.click(by.CLASS_NAME,'tradechoisecont')
        self.click(by.XPATH,'//*[@id="normalShopType"]/p/div/dl[3]/dd[1]')
        self.input(by.ID,'customerPhone',str(data['客服电话']))
        self.click(by.XPATH,'//*[@id="province"]/a/label')
        self.click(by.LINK_TEXT,data['商户省'])
        self.click(by.XPATH,'//*[@id="city"]/a/label')
        self.click(by.LINK_TEXT,data['商户市'])
        self.click(by.XPATH,'//*[@id="country"]/a/label')
        self.click(by.LINK_TEXT,data['商户区'])
        self.clear(by.ID,'address')
        self.input(by.ID,'address',data['商户详细地址'])
        self.input(by.ID,'businessLicenseNo',data['营业执照编号'])
        self.input(by.ID,'contactPhone',data['联系人电话'])
        self.input(by.ID,'contactEmail',data['联系人邮箱'])
        self.input(by.ID,'remark',data['备注'])
        #银行账户信息
        self.click(by.ID,'noSelectAccountType')
        self.click(by.LINK_TEXT,data['账户类型'])
        self.input(by.ID,'bankName',data['开户银行'])
        self.sleep_time(1)
        self.click(by.XPATH,'//*[@id="hotSelect"]/dl/dd')
        if data['账户类型']=='企业':
            self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div[1]/div[1]/div/a/label')
            self.click(by.LINK_TEXT,data['开户省'])
            self.click(by.XPATH,'/html/body/div[1]/form[3]/div[4]/div/div[18]/div[1]/div[2]/div/a/label')
            self.click(by.LINK_TEXT,data['开户市'])
            self.input(by.ID,'subbranchName',data['开户支行名称'])
            self.input(by.ID,'cardNo',data['对公账号'])
            self.input(by.ID,'accountHolder',data['企业名称'])
            self.input(by.ID,'legalPersonName',data['法人姓名'])
            self.input(by.ID,'certNo',data['法人身份证号码'])
            self.input(by.ID,'file3',data['开户许可证照片'])
        else:
            self.input(by.ID,'cardNo',data['银行卡号'])
            self.input(by.ID,'accountHolder',data['开户人'])
            self.input(by.ID,'certNo',data['持卡人身份证号码'])
            self.input(by.ID,'mobile',str(data['银行预留手机号']))
        self.input(by.ID,'file0',data['营业执照照片'])
        self.input(by.ID,'file1',data['法人身份证照片(人像)'])
        self.input(by.ID,'file2',data['法人身份证照片(国徽)'])


