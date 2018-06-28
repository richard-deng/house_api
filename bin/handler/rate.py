# coding: utf-8
import logging

from house_base.response import success, error, RESP_CODE
from house_base.rate import RateInfo
from house_base.base_handler import BaseHandler
from zbase.web.validator import (
    with_validator_self
)

log = logging.getLogger()

class LoanPrimeRateInfoHandler(BaseHandler):

    @with_validator_self
    def _get_handler(self):
        data = {'rate': 0}
        rate = RateInfo.load_by_name('lpr')
        log.info('class=LoanPrimeRateInfoHandler|rate.data=%s', rate.data)
        if not rate.data:
            return error(RESP_CODE.DATAERR)
        data['rate'] = rate.data.get('rate')
        return success(data=data)
