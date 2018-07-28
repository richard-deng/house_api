# coding=utf-8
import logging
import json
import xmltodict
import traceback
from zbase.web import core


log = logging.getLogger()


class PrecreateNotify(core.Handler):

    def POST(self):
        try:
            self.set_headers({'Content-Type': 'text/xml; charset=UTF-8'})
            params = self.req.postdata()
            log.info("%s %s params: %s", self.__class__.__name__, 'POST', params)
            obj = xmltodict.parse(params, 'utf-8')
            obj = obj['xml']
            if 'out_trade_no' not in obj:
                return
            query_str = json.dumps({
                'notify': params,
                'syssn': obj['out_trade_no']
            })
            log.info('func=%s|query_str=%s', self.__class__.__name__, query_str)
            # 如果成功返回'SUCCESS'
            return self.write('SUCCESS')
        except Exception:
            log.warn(traceback.format_exc())
            return self.write('fail')
