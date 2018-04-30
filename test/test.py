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
        self.host = '127.0.0.1'
        self.port = 8083
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

    # @unittest.skip("skipping")
    def test_merchant_list(self):
        self.url = '/v1/api/box/list'
        ret = self.client.get(self.url, self.send)
        log.info(ret)
        respcd = json.loads(ret).get('respcd')
        self.assertEqual(respcd, '0000')


suite = unittest.TestLoader().loadTestsFromTestCase(TestHouseApiInstrument)
unittest.TextTestRunner(verbosity=2).run(suite)