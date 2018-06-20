# coding: utf-8
from handler import (
    page,
    ping,
    box,
    questions,
)

urls = (
    ('^/ping$', ping.Ping),
    ('^/v1/api/box/list', box.BoxListHandler),
    ('^/v1/api/box/info', box.BoxInfoHandler),
    ('^/v1/api/question/children/info', questions.QuestionSingleHandler),


    # 页面
    ('^/v1/api/page/text/detail.html$', page.PageTextDetail),
)
