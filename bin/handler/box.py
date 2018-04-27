# coding: utf-8
import logging

from house_base.response import success
from house_base.box_list import BoxList
from house_base.base_handler import BaseHandler

log = logging.getLogger()


class BoxListHandler(BaseHandler):

    def _get_handler(self):
        data = {'box_list': []}
        box = BoxList.load_all()
        if box:
            data['box_list'].extend(box)
        return success(data=data)
