# coding: utf-8
import logging
import config

from house_base.response import success, error, RESP_CODE
from house_base.weixin import GenOpenid, Precreate, Query
from house_base.trade import TradeOrder
from house_base.base_handler import BaseHandler
from zbase.web.validator import (
    with_validator_self, Field, T_INT, T_STR,
)

log = logging.getLogger()


class GenOpenidHandler(BaseHandler):

    _get_handler_fields = [
        Field('js_code', T_STR, False)
    ]
    
    @with_validator_self
    def _get_handler(self):
        data = {}
        params = self.validator.data
        js_code = params['js_code']
        g = GenOpenid(config.APPID, config.SECRET, config.MCH_ID, config.API_KEY)
        openid, msg = g.run(js_code)
        if not openid:
            return error(RESP_CODE.UNKOWNERR, respmsg=msg)
        data['openid'] = openid
        return success(data)


class PrecreateHandler(BaseHandler):

    _post_handler_fields = [
        Field('openid', T_STR, False),
        Field('consumer_name', T_STR, True),
        Field('consumer_mobile', T_STR, True),
        Field('order_name', T_STR, False),
        Field('order_desc', T_STR, True),
        Field('txamt', T_INT, False),
    ]

    @with_validator_self
    def _post_handler(self):
        params = self.validator.data
        # check txamt
        txamt = params['txamt']
        openid = params['openid']
        consumer_name = params['consumer_name']
        consumer_mobile = params['consumer_mobile']
        order_name = params['order_name']
        # order_desc是个json串带空格, validator返回的是个列表，存的有问题
        # order_desc = params['order_desc']
        order_desc = self.req.input().get('order_desc', '')
        p = Precreate(config.APPID, config.SECRET, config.MCH_ID, config.API_KEY)
        flag, msg, result = p.run(
            openid=openid, txamt=txamt, consumer_name=consumer_name,
            consumer_mobile=consumer_mobile, order_name=order_name,
            order_desc=order_desc 
        )
        if not flag:
            return error(RESP_CODE.UNKOWNERR, resperr=msg, respmsg=msg)
        return success(data=result)


class QueryHandler(BaseHandler):

    _get_handler_fields = [
        Field('syssn', T_STR, False)
    ]

    @with_validator_self
    def _get_handler(self):
        params = self.validator.data
        syssn = params['syssn']
        q =Query(config.APPID, config.SECRET, config.MCH_ID, config.API_KEY)
        result = q.run(syssn)
        return success(data=result)


class TradeListHandler(BaseHandler):

    _get_handler_fields = [
        Field('openid', T_STR, False)
    ]

    @with_validator_self
    def _get_handler(self):
        params = self.validator.data
        openid = params['openid']
        data = TradeOrder.load_by_openid(openid)
        return success(data=data)
