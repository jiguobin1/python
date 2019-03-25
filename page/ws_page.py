# coding=utf-8
#author：jiguobin
from base.actionMethod import ActionMethod
import random
import string
class WsPage(ActionMethod):
    def incoming(self,row,sheet=0):
        rows=row-1
        data=(dict(zip(self.get_excel_value(0,0), self.get_excel_value(sheet,rows))))
        print(rows)
        self.click('xpath','//*[@id="togglemenu"]/li[1]/a')
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
        self.click('id','addBankConfigureForWS')
        #如果文本中填写了配置名称，那么就清空原有信息，并输入
        if data['配置名称'] =='':
            pass
        else:
            self.clear('id','configureName')
            self.input('id','configureName',data[1])
        self.click('id','noSelcetPassTypeName')
        self.click('link_text',data['通道名称'])  #选择通道名称
        self.sleep_time(0.5)
        self.click('id','noSelcetAlipayRateName')
        self.click('link_text',data['支付宝商户费率名称'])   #支付宝费率名称
        self.click('id','noSelcetWechatRateName')
        self.click('link_text',data['微信商户费率名称'])   #微信费率名称
        self.input('id','configureRemark',data['配置备注'])
        self.clear('id','fullNameCn')
        #商户基本信息
        self.input('id','fullNameCn',data['商户名称'])#商户名称
        self.click('id','noSelectBusinessCategory')
        self.click('link_text',data['经营类目']) #经营类型
        if data['商户类型']=='个人':   #判断商户类型
            self.click('id','shoptype1')
        elif data['商户类型']=='个体':
            self.click('id','shoptype2')
        else:
            self.click('id','shoptype3')
        self.click('id','next')
        self.sleep_time(0.5)
        #商户详细信息
        self.clear('id','nameCn')
        self.input('id','nameCn',data['商户简称'])
        #个人没有营业执照编号
        if data['商户类型']=='个体':  #个体的营业执照编号不能重复
            self.input('id','businessLicenseNo',''.join(random.sample(string.ascii_letters+string.digits,18)))
        elif data['商户类型']=='企业':
            self.input('id','businessLicenseNo',data['营业执照编号'])
        self.click('xpath','//*[@id="province"]/a/label')
        self.click('link_text',data['省'])
        self.click('xpath','//*[@id="city"]/a/label')
        self.click('link_text',data['市'])
        self.click('xpath','//*[@id="country"]/a/label')
        self.click('link_text',data['区'])
        self.clear('id','address')
        self.input('id','address',data['商户详细地址'])
        self.input('id','customerPhone',str(data['负责人电话']))
        self.input('id','contactName',data['负责人'])
        self.input('id','wechatPublicNo',data['推荐关注微信APPID'])
        #银行账户信息
        self.input('id','bankName',data['开户银行'])
        self.sleep_time(1)
        self.click('xpath','//*[@id="hotSelect"]/dl/dd')
        self.input('id','cardNo',data['银行卡号/对公账号'])
        if data['商户类型']!='企业':
            self.input('id','accountHolder',data['开户人'])
            self.input('id','certificateHolderNo',data['结算人身份证号码'])
            self.input('id','cardholderAddress',data['结算人身份证地址'])
        else:
            self.input('id','companyCorporation',data['法人'])
            self.input('id','certificateNo',data['法人证件号'])
        #进件资料图片  火狐不可传空 谷歌可以传空
        if data['商户类型']!='个人':
            self.input('id','multipartFile0',data['营业执照照片'])
        if data['商户类型']=='企业':
            self.input('id','multipartFile1',data['开户许可证'])
        self.input('id','multipartFile2',data['身份证正面'])
        self.input('id','multipartFile3',data['身份证反面'])
        self.input('id','multipartFile4',data['门头照'])
        self.input('id','multipartFile5',data['店内环境照'])
        # self.input('id','multipartFile6',self.data['银行卡'])
        # self.input('id','multipartFile7',self.data['其他照片'])







