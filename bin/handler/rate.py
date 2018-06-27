# coding: utf-8
import logging

from house_base.response import success
from house_base.rate import RateInfo
from house_base.base_handler import BaseHandler
from zbase.web.validator import (
    with_validator_self
)

log = logging.getLogger()

class RateInfoHandler(BaseHandler):

    @with_validator_self
    def _get_handler(self):
        data = {'rates': []}
        rates = RateInfo.load_all()
        data['rates'].extend(rates)
        return success(data=data)
