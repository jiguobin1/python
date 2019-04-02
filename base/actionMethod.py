# coding=utf-8
#author：jiguobin
from selenium import webdriver
from base.find_element import FindElement
import time
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import xlrd
import pymysql
class ActionMethod:
    #打开浏览器
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    #输入地址
    def get_url(self,url):
        self.driver.get(url)

    #切换frame
    def switch_frame(self,frame):
        self.driver.switch_to.frame(frame)
        self.sleep_time(2)

    #定位元素
    def get_element(self,node,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(node,key)
        return element

    #输入元素
    def element_send_keys(self,node,key,value):
        self.get_element(node,key).send_keys(value)


    #点击元素
    def click_element(self,node,key):
        self.get_element(node,key).click()

    #清空文本
    def clear(self,type,value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).clear()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).clear()
        elif type == "id":
            self.driver.find_element_by_id(value).clear()
        elif type == "name":
            self.driver.find_element_by_name(value).clear()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).clear()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).clear()

    # 输入内容方法
    def input(self, type, value, inputvalue):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(inputvalue)
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).send_keys(inputvalue)
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(inputvalue)
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(inputvalue)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).send_keys(inputvalue)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)

     # 鼠标事件方法
    def click(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).click()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).click()
        elif type == "id":
            self.driver.find_element_by_id(value).click()
        elif type == "name":
            self.driver.find_element_by_name(value).click()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).click()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).click()

    #等待
    def sleep_time(self,times):
        time.sleep(times)

    #关闭浏览器
    def close_browser(self):
        self.driver.close()

    #获取title
    def get_title(self):
        title = self.driver.title
        return title


     #获取图片
    def get_code_image(self,fiel_name):
        self.driver.save_screenshot(fiel_name)
        code_element=self.driver.find_element_by_id('verifyCode')
        left=code_element.location['x']
        top=code_element.location['y']
        right=code_element.size['width']+left
        height=code_element.size['height']+top
        im=Image.open(fiel_name)
        img=im.crop((left,top,right,height))
        img.save(fiel_name)

    #解析图片获取验证码
    def code_online(self,file_name):
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId", "14")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        print(res.text)
        text = res.json()['showapi_res_body']['Result']
        return text

    #登录ms
    def login_ms(self,type=None,url=None,name=None,password=None):
        '''
        :param url: 环境url
        :param type: 浏览器类型
        :param name: 账户
        :param password: 密码
        :return:
        '''
        if type==None:
            types='chrome'
        elif type=='f':
            types='firefox'
        self.open_browser(types)
        #如果url=测试环境，账号和密码为默认
        if url=='测试':
            test_url='http://192.168.19.103:8000/ms/login.in'
            if name==None and password==None:
                test_name='csdls'
                test_password='111qqq'
            else:
                test_name=name
                test_password=password
            self.get_url(test_url)
            self.input('id','logInName',test_name)
            self.input('id','password',test_password)
        #如果url=灰度环境，账号和密码为默认
        elif url=='灰度':
            huidu_url='http://intms.51ebill.com/ms/login.in'
            if name==None and password==None:
                huidu_name='dlscs2'
                huidu_password='111qqq'
            else:
                huidu_name=name
                huidu_password=password
            self.get_url(huidu_url)
            self.input('id','logInName',huidu_name)
            self.input('id','password',huidu_password)
        #如果url=线上环境，账号和密码为默认
        elif url=='生产':
            online_url='http://ms.liantuobank.com/ms/login.in'
            if name==None and password==None:
                online_name='dlscs2'
                online_password='111qqq'
            else:
                online_name=name
                online_password=password
            self.get_url(online_url)
            self.input('id','logInName',online_name)
            self.input('id','password',online_password)
        file_name='D:\image_code.png'
        # self.get_code_image(file_name)
        # code_text=self.code_online(file_name)
        # self.input('id','verifyCodeInput',code_text)
        self.sleep_time(4)
        self.click('id','submitForm')
        # if self.driver.find_element_by_id('errorVerifyCode').text=='验证码输入错误':
        #     self.get_code_image(file_name)
        #     code_text=self.code_online(file_name)
        #     self.input('id','verifyCodeInput',code_text)
        #     self.click('id','submitForm')
        #     self.sleep_time(2)



    #登录cms
    def login_cms(self,url,type=None,name=None,password=None):
        '''
        :param url: 环境url
        :param type: 浏览器类型
        :param name: 账户
        :param password: 密码
        :return:
        '''
        if type==None:
            types='chrome'
        else:
            types=type
        self.open_browser(types)
        #如果url=测试环境，账号和密码为默认
        if url=='test':
            test_url='http://192.168.19.25:8000/cms/login.in'
            if name==None and password==None:
                test_name='jrpt'
                test_password='111qqq'
            else:
                test_name=name
                test_password=password
            self.get_url(test_url)
            self.input('id','logInName',test_name)
            self.input('id','password',test_password)
        #如果url=灰度环境，账号和密码为默认
        elif url=='huidu':
            huidu_url='http://intcms.51ebill.com/cms/login.in'
            if name==None and password==None:
                huidu_name='xuqiandls'
                huidu_password='111qqq'
            else:
                huidu_name=name
                huidu_password=password
            self.get_url(huidu_url)
            self.input('id','logInName',huidu_name)
            self.input('id','password',huidu_password)
        #如果url=线上环境，账号和密码为默认
        elif url=='online':
            online_url='http://cms.liantuobank.com/cms/login.in'
            if name==None and password==None:
                online_name='xuqiandls'
                online_password='111qqq'
            else:
                online_name=name
                online_password=password
            self.get_url(online_url)
            self.input('id','logInName',online_name)
            self.input('id','password',online_password)
        # file_name='D:\image_code.png'
        # self.get_code_image(file_name)
        # code_text=self.code_online(file_name)
        # self.input('id','verifyCodeInput',code_text)
        self.sleep_time(5)
        self.click('id','submitForm')
        self.sleep_time(2)


    #获取excel中哪一行的数据
    def get_excel_value(self,sheet,row,file_name=None):
        '''
        :param file_name:打开excel
        :param sheet: 获取页数
        :param row:
        '''
        if file_name == None:
            #默认地址
            file_name = 'D:\liantuo\python\config\ws.xlsx'
        else:
            self.file_name=file_name
        book = xlrd.open_workbook(file_name) #打开一个excel
        sheet = book.sheet_by_index(sheet)
        data=sheet.row_values(row)
        return data




