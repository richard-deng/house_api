# coding: utf-8
import logging
import config

from house_base.response import success, error, RESP_CODE
from house_base.box_list import BoxList
from house_base.order import Order
from house_base import define
from house_base.base_handler import BaseHandler
from zbase.web.validator import (
    with_validator_self, Field, T_INT, T_STR
)

log = logging.getLogger()


class BoxListHandler(BaseHandler):

    def _get_handler(self):
        data = {'box_list': []}
        box = BoxList.load_all()
        if box:
            for item in box:
                icon_name = item['icon']
                item['icon'] = config.BASE_URL + icon_name
            data['box_list'].extend(box)
        return success(data=data)


class BoxInfoHandler(BaseHandler):

    _get_handler_fields = [
        Field('box_id', T_INT, False),
    ]

    @with_validator_self
    def _get_handler(self):
        data = {}
        params = self.validator.data
        box_id = params.get('box_id')
        box = BoxList(box_id)
        box.load()
        if not box.data:
            return error(errcode=RESP_CODE.DATAERR)
        box_type = box.data.get('box_type')
        data['box_type'] = box_type
        if box_type == define.BOX_TYPE_ORDER:
            order = Order.load_by_box_id(box_id)
            data['info'] = order.data if order.data else {}
        return success(data=data)

