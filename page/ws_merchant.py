# coding=utf-8
#author：jiguobin
from base.actionMethod import ActionMethod
class WsPage(ActionMethod):
    def ws(self,id,type):
        self.Incoming(id,type)




w=WsPage()
w.ws('EW_N6268478142','网商')

