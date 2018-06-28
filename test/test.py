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
            'box_id': 6414765676824684757
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
            'parent': 1
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



suite = unittest.TestLoader().loadTestsFromTestCase(TestHouseApiInstrument)
unittest.TextTestRunner(verbosity=2).run(suite)
