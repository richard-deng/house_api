# -*- coding: utf-8 -*-
import logging
from house_base.define import TOKEN_HOUSE_CORE
from house_base.text_detail import TextDetail
from zbase.base.dbpool import get_connection_exception


log = logging.getLogger()


def get_text_content(text_id):
    d = TextDetail.load_by_text_id(text_id)
    if d.data:
        return d.data
    return {}
