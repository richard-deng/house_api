# coding: utf-8
import logging
import config

from house_base.response import success, error, RESP_CODE
from house_base.carousel import Carousel
from house_base.base_handler import BaseHandler
from zbase.web.validator import (
    with_validator_self, Field, T_INT
)

log = logging.getLogger()


class CarouselHandler(BaseHandler):

    _get_handler_fields = []


    @with_validator_self
    def _get_handler(self):
        data = {'carousel': []}
        records = Carousel.load_three_carousel()
        if records:
            for record in records:
                icon_name = record['icon']
                record['icon'] = config.BASE_URL + icon_name
            data['carousel'] = records
        return success(data=data) 
