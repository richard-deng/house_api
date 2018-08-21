# coding: utf-8
import base64
import logging
import config

from house_base.response import success, error, RESP_CODE
from house_base.base_handler import BaseHandler
from house_base.banner import Banners
from zbase.web.validator import (
    with_validator_self, Field, T_INT, T_STR
)

log = logging.getLogger()


class BannerHandler(BaseHandler):

    _get_handler_fields = []


    @with_validator_self
    def _get_handler(self):
        data = {'banner': {}}
        ret = Banners.load_recent()
        if ret:
            content = ret['content']
            content_str = base64.b64decode(content)
            ret['content'] = content_str
            data['banner'] = ret
        return success(data=data)

