# coding: utf-8
import json
import unittest
from zbase.base import logger
from zbase.base.http_client import RequestsClient
from zbase.server.client import HttpClient

log = logger.install('stdout')


class TestHouseApiInstrument(unittest.TestCase):
    def setUp(self):
        self.url = ''
        self.send = {}
        self.host = 'api.xunchengfangfu.com'
        self.port = 80
        self.timeout = 2000

        # self.headers = {'sessionid': 'ea74f0cb-8f38-4325-88bf-1669314285be'}
        # self.cookie = self.headers
        self.server = [
            {
                'addr': (self.host, self.port),
                'timeout': self.timeout
            }
        ]
        self.client = HttpClient(self.server, client_class=RequestsClient)

    @unittest.skip("skipping")
    def test_box_list(self):
        self.url = '/v1/api/box/list'
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_box_info(self):
        self.url = '/v1/api/box/info'
        self.send.update({
            # 订单
            # 'box_id': 6399172705714754862
            # 文本
            # 'box_id': 6399187464367428911
            # 分类
            'box_id': 6427527416620543622

        })
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_text_detail_page(self):
        self.url = '/v1/api/page/text/detail?text_id=6408215217259503060'
        ret = self.client.get(self.url)
        log.info(ret)

    @unittest.skip("skipping")
    def test_question_children(self):
        self.url = '/v1/api/question/children/info'
        self.send.update({
            # 'parent': -1
            'parent': -1
        })
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    # @unittest.skip("skipping")
    def test_rate_info(self):
        self.url = '/v1/api/rate/lpr/info'
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_precreate_notify(self):
        import requests
        method = "POST"
        url = 'http://api.xunchengfangfu.com:80/v1/api/weixin/notify'
        headers = {'Content-Type': 'text/xml; charset=UTF-8'}
        req_str = "<xml><out_trade_no>123456</out_trade_no><trade_state>SUCCESS</trade_state></xml>"
        resp = requests.request(method, url, data=req_str, verify=False, headers=headers)
        log.info('status_code=%s|content=%s', resp.status_code, resp.content)

    @unittest.skip("skipping")
    def test_weixin_openid(self):
        self.url = '/v1/api/weixin/openid'
        self.send.update({
            'js_code': '0335UKIV1lvgYU0Rz2LV16BEIV15UKIs'
        })
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_weixin_precreate(self):
        self.url = '/v1/api/weixin/precreate'
        self.send.update({
            'openid': 'oOKQM5EhGzdh-1x1krU5VCw-CDnM',
            'txamt': 1,
            'consumer_name': '李三',
            'consumer_mobile': '18215630018',
            'order_name': '商品一',
            'order_desc': '商品描述',
        })
        ret = self.client.post(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_weixin_order_query(self):
        self.url = '/v1/api/weixin/order/query'
        self.send.update({
            'syssn': '201807310013408870'
        })
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_weixin_trade_list(self):
        self.url = '/v1/api/weixin/trade/list'
        self.send.update({
            'openid': 'oOKQM5EhGzdh-1x1krU5VCw-CDnM'
        })
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_agreement(self):
        self.url = '/v1/api/agreement/content'
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_banner(self):
        self.url = '/v1/api/banner/content'
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')

    @unittest.skip("skipping")
    def test_carousel_list(self):
        self.url = '/v1/api/carousel/list'
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')


suite = unittest.TestLoader().loadTestsFromTestCase(TestHouseApiInstrument)
unittest.TextTestRunner(verbosity=2).run(suite)
