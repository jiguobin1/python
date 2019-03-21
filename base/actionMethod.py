# coding=utf-8
#author：jiguobin
from selenium import webdriver
from base.find_element import FindElement
import time
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
class ActionMethod:
    #打开浏览器
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

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
    def login_ms(self):
        #file_name='D:\image_code.png'
        self.open_browser('chrome')
        self.get_url('http://192.168.19.103:8000/ms/login.in')
        self.element_send_keys('LoginElement','user_name','csdls')
        self.element_send_keys('LoginElement','user_password','111qqq')
        # self.get_code_image(file_name)
        # code_text=self.code_online(file_name)
        # self.element_send_keys('code_text',code_text)
        self.sleep_time(5)
        self.click_element('LoginElement','submit')
        self.sleep_time(1)

    #登录cms
    def login_cms(self):
        #file_name='D:\image_code.png'
        self.open_browser('chrome')
        self.get_url('http://192.168.19.25:8000/cms/login.in')
        self.element_send_keys('LoginElement','user_name','jrpt')
        self.element_send_keys('LoginElement','user_password','111qqq')
        # self.get_code_image(file_name)
        # code_text=self.code_online(file_name)
        # self.element_send_keys('code_text',code_text)
        self.sleep_time(5)
        self.click_element('LoginElement','submit')
        self.sleep_time(1)

    #选择进件的商户和类型
    def Incoming(self,id,type):
        '''
        :param id: 进件的商户
        :param type: 进件的类型
        '''
        if type=='网商':
            types='addBankConfigureForWS'
        elif type=='客商':
            types='addBankConfigureForKS'
        elif type=='微信官方':
            types='addWechatConfigure'
        self.login_ms()
        self.click('link_text','商户管理')
        self.click('link_text','商户总部（一般）')
        self.switch_frame('contframe')
        self.input('id','searchContent',id)
        self.click('id','searchContent')
        self.sleep_time(2)
        self.click('class_name','item')
        self.click('id','query')
        self.sleep_time(1)
        self.click('id','details')
        self.click('id',types)

