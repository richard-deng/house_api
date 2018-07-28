# coding: utf-8
from handler import (
    page,
    ping,
    box,
    questions,
    rate,
    notify,
    weixin,
)

urls = (
    ('^/ping$', ping.Ping),
    ('^/v1/api/box/list', box.BoxListHandler),
    ('^/v1/api/box/info', box.BoxInfoHandler),
    ('^/v1/api/question/children/info', questions.QuestionSingleHandler),
    ('^/v1/api/rate/lpr/info$', rate.LoanPrimeRateInfoHandler),

    # 微信的异步通知
    ('^/v1/api/weixin/notify$', notify.PrecreateNotify),
    # 获取微信的openid
    ('^/v1/api/weixin/openid$', weixin.GenOpenidHandler),
    # 微信预下单
    ('^/v1/api/weixin/precreate$', weixin.PrecreateHandler),


    # 页面
    ('^/v1/api/page/text/detail.html$', page.PageTextDetail),
)
