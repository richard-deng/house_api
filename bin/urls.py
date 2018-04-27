# coding: utf-8
from handler import (
    ping,
    box,
)

urls = (
    ('^/ping$', ping.Ping),
    ('^/v1/api/box/list', box.BoxListHandler),
)