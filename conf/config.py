# -*- coding: utf-8 -*-
import os
HOME = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'bin')
rtenv = 'product'

LOGFILE = {
    'root': {
        'filename': {
            'DEBUG': os.path.join(HOME, '../log/house_api.log'),
            'ERROR': os.path.join(HOME, '../log/house_api.error.log'),
        }
    }
}
# LOGFILE = 'stdout'

database = {
    'house_core':{
        'engine': 'pymysql',
        'passwd': '123456',
        'charset': 'utf8',
        'db': 'house_core',
        'idle_timeout': 10,
        'host': '127.0.0.1',
        'user': 'xuncheng',
        'port': 3306,
        'conn': 6
    },

}

# web config
# URLS配置
URLS = None
# 静态路径配置
STATICS = {'/static/':'/static/'}
# 模板配置
TEMPLATE = {
    'cache': True,
    'path': '',
    'tmp': os.path.join(HOME, '../tmp'),
}
# 中间件
MIDDLEWARE = ()
# WEB根路径
DOCUMENT_ROOT = HOME
# 页面编码
CHARSET = 'UTF-8'
# APP就是一个子目录
APPS = ()
DATABASE = {}
# 调试模式: True/False
# 生产环境必须为False
DEBUG = True
# 模版路径
template = os.path.join(HOME, 'template')

# 服务地址
HOST = '0.0.0.0'
# 服务端口
PORT = 8085
# 图标链接基地址
MIS_DOMAIN = 'mis.xunchengfangfu.com'
MIS_PORT = ''
MIS_STATIC_PATH = '/mis/static/upload/icon/'
# BASE_URL = 'http://' + MIS_DOMAIN + ':' + str(MIS_PORT) + MIS_STATIC_PATH
BASE_URL = 'http://' + MIS_DOMAIN + MIS_STATIC_PATH
TEXT_DETAIL_PREFIX_URL = '/v1/api/page/text/detail.html'
# 个人公积金贷款利率名称
ACCUMULATION_LOAN = u'公积金贷款利率'
# 商业贷款利率名称
BUSINESS_LOAN = u'商业贷款利率'
TEXT_DETAIL_PREFIX_URL = '/v1/api/page/text/detail.html'
# 支付参数
API_KEY = ''
APPID = ''
MCH_ID = ''
SECRET = ''
# 协议文件
AGREEMENT = '/home/xunchengfangfu/house/house_mis_v2/data/agreement.html'
# 滚动文字文案
BANNER_TEXT = '/home/xunchengfangfu/house/house_mis_v2/data/banner.txt'
# 下载文件前缀
DOWNLOAD_FILE_PREFIX = 'https://' + MIS_DOMAIN + '/mis/static/upload/file/'
