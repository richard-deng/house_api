# coding: utf-8
import base64
import traceback
from zbase.web import core
from zbase.web import template

import logging
import tools
from house_base.response import error, RESP_CODE

log = logging.getLogger()


class PageTextDetail(core.Handler):
    def GET(self):
        try:
            params = self.req.input()
            log.debug('PageTextDetail|params=%s', params)
            text_id = params.get('text_id')
            data = tools.get_text_content(text_id)
            if data:
                # 有可能是老数据不用base64处理
                # 有可能是新数据用base64处理
                content_str = data.get('content')
                try:
                    content = base64.b64decode(content_str)
                except Exception:
                    log.warn(traceback.format_exc())
                    content = content_str
            return self.write(template.render('text_demo.html', content=content))
        except Exception:
            log.warn(traceback.format_exc())
            return self.write(errcode=RESP_CODE.SERVERERR)