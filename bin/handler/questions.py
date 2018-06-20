# coding: utf-8
import logging
import config

from house_base.response import success, error, RESP_CODE
from house_base.questions import Questions
from house_base import define
from house_base.base_handler import BaseHandler
from zbase.web.validator import (
    with_validator_self, Field, T_INT, T_STR
)

log = logging.getLogger()


class QuestionSingleHandler(BaseHandler):

    _get_handler_fields = [
        Field('parent', T_INT, False),
    ]

    @with_validator_self
    def _get_handler(self):
        data = {}
        params = self.validator.data
        parent = params.get('parent')
        ret = Questions.load_by_parent_single(parent)
        data['children'] = ret if ret else []
        return success(data=data)
