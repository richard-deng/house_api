# coding: utf-8
from handler import (
    page,
    ping,
    box,
)

urls = (
    ('^/ping$', ping.Ping),
    ('^/v1/api/box/list', box.BoxListHandler),
    ('^/v1/api/box/info', box.BoxInfoHandler),


    # 页面
    ('^/v1/page/text/detail$', page.PageTextDetail),
)