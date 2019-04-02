# coding=utf-8
#author：jiguobin
from base.actionMethod import ActionMethod
from selenium.webdriver.common.by import By as by
import random
import string
class WsPage(ActionMethod):
    def wsIncoming(self,row,sheet=0):
        data=(dict(zip(self.get_excel_value(0,0), self.get_excel_value(sheet,row-1))))
        print(data)
        self.login_ms(url=data['环境'],name=data['代理商登录账号'],password=data['代理商登录密码'])#登录

        self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/a')   #商户管理
        self.sleep_time(0.5)
        #判断是商户还是门店进件
        if data['商户id']!='':
            self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/ul/li[2]/a')   #商户总部
            self.switch_frame('contframe')
            self.input(by.ID,'searchContent',data['商户id'])
            self.click(by.ID,'searchContent')
        elif data['门店id']!='':
            self.click(by.XPATH,'//*[@id="togglemenu"]/li[1]/ul/li[3]/a')   #商户门店
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
        self.click(by.ID,'addBankConfigureForWS')
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
        self.click(by.LINK_TEXT,data['支付宝商户费率名称'])   #支付宝费率名称
        self.click(by.ID,'noSelcetWechatRateName')
        self.click(by.LINK_TEXT,data['微信商户费率名称'])   #微信费率名称
        self.input(by.ID,'configureRemark',data['配置备注'])
        self.clear(by.ID,'fullNameCn')
        #商户基本信息
        self.input(by.ID,'fullNameCn',data['商户名称'])#商户名称
        self.click(by.ID,'noSelectBusinessCategory')
        self.click(by.LINK_TEXT,data['经营类目']) #经营类型
        if data['商户类型']=='个人':   #判断商户类型
            self.click(by.ID,'shoptype1')
        elif data['商户类型']=='个体':
            self.click(by.ID,'shoptype2')
        else:
            self.click(by.ID,'shoptype3')
        self.click(by.ID,'next')
        self.sleep_time(0.5)
        #商户详细信息
        self.clear(by.ID,'nameCn')
        self.input(by.ID,'nameCn',data['商户简称'])
        #个人没有营业执照编号
        if data['商户类型']=='个体':  #个体的营业执照编号不能重复
            self.input(by.ID,'businessLicenseNo',''.join(random.sample(string.ascii_letters+string.digits,18)))
        elif data['商户类型']=='企业':
            self.input(by.ID,'businessLicenseNo',data['营业执照编号'])
        self.click(by.XPATH,'//*[@id="province"]/a/label')
        self.click(by.LINK_TEXT,data['省'])
        self.click(by.XPATH,'//*[@id="city"]/a/label')
        self.click(by.LINK_TEXT,data['市'])
        self.click(by.XPATH,'//*[@id="country"]/a/label')
        self.click(by.LINK_TEXT,data['区'])
        self.clear(by.ID,'address')
        self.input(by.ID,'address',data['商户详细地址'])
        self.input(by.ID,'customerPhone',str(data['负责人电话']))
        self.input(by.ID,'contactName',data['负责人'])
        self.input(by.ID,'wechatPublicNo',data['推荐关注微信APPID'])
        #银行账户信息
        self.input(by.ID,'bankName',data['开户银行'])
        self.sleep_time(1)
        self.click(by.XPATH,'//*[@id="hotSelect"]/dl/dd')
        self.input(by.ID,'cardNo',data['银行卡号/对公账号'])
        if data['商户类型']!='企业':
            self.input(by.ID,'accountHolder',data['开户人'])
            self.input(by.ID,'certificateHolderNo',data['结算人身份证号码'])
            self.input(by.ID,'cardholderAddress',data['结算人身份证地址'])
        else:
            self.input(by.ID,'companyCorporation',data['法人'])
            self.input(by.ID,'certificateNo',data['法人证件号'])
        #进件资料图片  火狐不可传空 谷歌可以传空
        if data['商户类型']!='个人':
            self.input(by.ID,'multipartFile0',data['营业执照照片'])
        if data['商户类型']=='企业':
            self.input(by.ID,'multipartFile1',data['开户许可证'])
        self.input(by.ID,'multipartFile2',data['身份证正面'])
        self.input(by.ID,'multipartFile3',data['身份证反面'])
        self.input(by.ID,'multipartFile4',data['门头照'])
        self.input(by.ID,'multipartFile5',data['店内环境照'])


        #     self.input(by.ID,'multipartFile6',data['开户许可证'])
        # self.input(by.ID,'multipartFile1',data['身份证正面'])
        # self.input(by.ID,'multipartFile2',data['身份证反面'])
        # self.input(by.ID,'multipartFile3',data['门头照'])
        # self.input(by.ID,'multipartFile4',data['店内环境照'])
        # # self.input('id','multipartFile6',self.data['银行卡'])
        # # self.input('id','multipartFile7',self.data['其他照片'])







