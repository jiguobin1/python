# coding=utf-8
#author：jiguobin
from base.actionMethod import ActionMethod
class WsPage(ActionMethod):
    #共用数据部分
    def __init__(self,sheet,row):
        '''
        :param file_name:这是一个默认参数，可传可不传 进件用到的数据excel
        :param sheet: excel中的页码
        :param row: excel中的哪行数据
        :data:excel中的数据  根据数据中的商户类型决定进什么件
        :return:
        '''
        self.id=id
        self.sheet=sheet
        self.row=row-1
        self.data=(dict(zip(self.get_excel_value(0,0), self.get_excel_value(self.sheet,self.row))))
              #获取excel数据

    #商户类型判断添加缺少字段方法
    def ws(self):
        self.login_ms()
        print(self.data)
        #判断是商户进件还是门店进件
        if self.data['商户id']!='':
            self.click('link_text','商户管理')
            self.click('link_text','商户总部（一般）')
            self.switch_frame('contframe')
            self.input('id','searchContent',self.data['商户id'])
            self.click('id','searchContent')
            self.sleep_time(2)
            self.click('class_name','item') #选中指定商户
            self.click('id','query')        #查找商户
            self.sleep_time(1)
            self.public()

        elif self.data['门店id']!='':
            self.click('link_text','商户管理')
            self.sleep_time(1)
            self.click('link_text','商户门店（一般）')
            self.switch_frame('contframe')
            self.input('id','storeContent',self.data['门店id'])
            self.click('id','storeContent')
            self.sleep_time(2)
            self.click('class_name','item') #选中指定商户
            self.click('id','query')        #查找商户
            self.sleep_time(1)
            self.public()
        else:
            print('excel取值不正确')

    #网商进件的公共部分
    def public(self):
        self.click('id','details')
        self.click('id','addBankConfigureForWS')
        #如果文本中填写了配置名称，那么就清空原有信息，并输入
        if self.data['配置名称'] =='':
            pass
        else:
            self.clear('id','configureName')
            self.input('id','configureName',self.data[1])
        self.click('id','noSelcetPassTypeName')
        self.click('link_text',self.data['通道名称'])  #选择通道名称
        self.sleep_time(0.5)
        self.click('id','noSelcetAlipayRateName')
        self.click('link_text',self.data['支付宝商户费率名称'])   #支付宝费率名称
        self.click('id','noSelcetWechatRateName')
        self.click('link_text',self.data['微信商户费率名称'])   #微信费率名称
        self.input('id','configureRemark',self.data['配置备注'])
        self.clear('id','fullNameCn')
        #商户基本信息
        self.input('id','fullNameCn',self.data['商户名称'])#商户名称
        self.click('id','noSelectBusinessCategory')
        self.click('link_text',self.data['经营类目']) #经营类型
        if self.data['商户类型']=='个人':   #判断商户类型
            self.click('id','shoptype1')
        elif self.data['商户类型']=='个体':
            self.click('id','shoptype2')
        else:
            self.click('id','shoptype3')
        self.click('id','next')
        self.sleep_time(0.5)
        #商户详细信息
        self.clear('id','nameCn')
        self.input('id','nameCn',self.data['商户简称'])
        if self.data['商户类型']!='个人':  #个人没有营业执照编号
            self.input('id','businessLicenseNo',self.data['营业执照编号'])
        self.click('xpath','//*[@id="province"]/a/label')
        self.click('link_text',self.data['省'])
        self.click('xpath','//*[@id="city"]/a/label')
        self.click('link_text',self.data['市'])
        self.click('xpath','//*[@id="country"]/a/label')
        self.click('link_text',self.data['区'])
        self.clear('id','address')
        self.input('id','address',self.data['商户详细地址'])
        self.input('id','customerPhone',str(self.data['负责人电话']))
        self.input('id','contactName',self.data['负责人'])
        self.input('id','wechatPublicNo',self.data['推荐关注微信APPID'])
        #银行账户信息
        self.input('id','bankName',self.data['开户银行'])
        self.sleep_time(1)
        self.click('xpath','//*[@id="hotSelect"]/dl/dd')
        self.input('id','cardNo',self.data['银行卡号/对公账号'])
        if self.data['商户类型']!='企业':
            self.input('id','accountHolder',self.data['开户人'])
            self.input('id','certificateHolderNo',self.data['结算人身份证号码'])
            self.input('id','cardholderAddress',self.data['结算人身份证地址'])
        else:
            self.input('id','companyCorporation',self.data['法人'])
            self.input('id','certificateNo',self.data['法人证件号'])
        #进件资料图片  火狐不可传空 谷歌可以传空
        if self.data['商户类型']!='个人':
            self.input('id','multipartFile0',self.data['营业执照照片'])
        if self.data['商户类型']=='企业':
            self.input('id','multipartFile1',self.data['开户许可证'])
        self.input('id','multipartFile2',self.data['身份证正面'])
        self.input('id','multipartFile3',self.data['身份证反面'])
        self.input('id','multipartFile4',self.data['门头照'])
        self.input('id','multipartFile5',self.data['店内环境照'])
        # self.input('id','multipartFile6',self.data['银行卡'])
        # self.input('id','multipartFile7',self.data['其他照片'])


w=WsPage(0,6)
w.ws()





