# coding: utf-8
import logging
import config

from house_base.response import success, error, RESP_CODE
from house_base.base_handler import BaseHandler
from zbase.web.validator import (
    with_validator_self, Field, T_INT, T_STR
)

log = logging.getLogger()


class BannerHandler(BaseHandler):

    _get_handler_fields = []


    @with_validator_self
    def _get_handler(self):
        data = {'content': ''}
        with open(config.BANNER_TEXT, 'rb') as f:
            content = f.read()
        data['content'] = content
        return success(data=data)

