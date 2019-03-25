# coding：utf-8
#author：jiguobin
from page.ws_page import WsPage
if __name__ == '__main__':
    #网商进件
    w=WsPage()
    w.login_ms('test','f')
    w.incoming(6)
    pass

