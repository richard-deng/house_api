# coding: utf-8
import logging

from house_base.response import success, error, RESP_CODE
from house_base.rate import RateInfo
from house_base.base_handler import BaseHandler
from zbase.web.validator import (
    with_validator_self
)
import config

log = logging.getLogger()

class LoanPrimeRateInfoHandler(BaseHandler):

    @with_validator_self
    def _get_handler(self):
        data = {'business_loan_rate': 0, 'accumulation_fund_loan_rate': 0}
        rate = RateInfo.name_to_value()
        log.info('class=LoanPrimeRateInfoHandler|rate=%s', rate)
        if not rate:
            return error(RESP_CODE.DATAERR)
        data['accumulation_fund_loan_rate'] = rate.get(config.ACCUMULATION_LOAN).get('rate')
        data['business_loan_rate'] = rate.get(config.BUSINESS_LOAN).get('rate')
        return success(data=data)
